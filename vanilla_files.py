"""Puts vanilla's own data pack and resource pack files in vanilla_mcdoc/vanilla/, as Python, e.g. data/minecraft/recipe/tnt_minecart.json
is `from vanilla_mcdoc.vanilla.data.recipe import TNT_MINECART`, which is `RecipeCraftingShapeless(...)`."""
import importlib
import json
import keyword
import re
import shutil
import zipfile
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, TypeAdapter

from minecraft_registry import resource_symbol
from schema_resolution import get_schema_graph
from utils import GENERATED_SYMBOLS_DIRECTORY, VANILLA_ZIPS, symbol_path_to_import_string_and_name, write_file_if_changed

VANILLA_DIRECTORY = GENERATED_SYMBOLS_DIRECTORY / "vanilla"
LANGUAGES = {"en_us", "deprecated"}  # The other languages are another 90 MB, so just English (deprecated.json is its own type)
# e.g. mcmeta-26.3-data-json/data/minecraft/recipe/oak_boat.json, or one in a built-in pack, under data/minecraft/datapacks/<pack>/
FILE_PATTERN = re.compile(r"[^/]+/((?:data/minecraft/datapacks/[^/]+/)?(?:data|assets)/)([^/]+)/(.+)\.json")
LINE_LENGTH = 120  # Anything longer gets split over lines


def python_name(name: str) -> str:
    """A folder's name in Python, e.g. 1 is _1, and a keyword gets a _ after it, like fields do (from_)."""
    name = f"_{name}" if name[0].isdigit() else name
    return f"{name}_" if keyword.iskeyword(name) else name


def constant_name(name: str) -> str:
    """A file's name in Python, e.g. TNT_MINECART for tnt_minecart.json, or _11 for the jukebox song 11.json."""
    return f"_{name}" if name[0].isdigit() else name.upper()


def vanilla_files() -> dict[tuple[str, ...], tuple[str, str]]:
    """Each of vanilla's files that has a model, by where it is (its folders in Python, then its name), e.g. ("data",
    "recipe", "tnt_minecart"), with its model's symbol and the file itself. The minecraft namespace's folder is left out,
    but any other's isn't (realms)."""
    resources = get_schema_graph().dispatchers["minecraft:resource"]
    files: dict[tuple[str, ...], tuple[str, str]] = {}
    for zip_path in VANILLA_ZIPS:
        with zipfile.ZipFile(zip_path) as archive:
            for name in archive.namelist():
                if (match := FILE_PATTERN.fullmatch(name)) is None:
                    continue  # e.g. pack.mcmeta
                pack, namespace, path = match.groups()
                if path.startswith("lang/") and path.removeprefix("lang/") not in LANGUAGES:
                    continue
                if (symbol := resource_symbol(path, resources)) is None:
                    continue
                # e.g. data/ or (with the namespace in the middle left out) data/datapacks/trade_rebalance/data/
                pack_folders: list[str] = pack.replace("/minecraft/", "/").split("/")[:-1]
                namespace_folders: list[str] = [] if namespace == "minecraft" else [namespace]
                path_parts: list[str] = path.split("/")
                *folders, file_name = [*pack_folders, *namespace_folders, *path_parts]
                files[(*(python_name(folder) for folder in folders), file_name)] = symbol, archive.read(name).decode("utf-8")
    return files


def import_name(module: str, name: str, imports: dict[tuple[str, str], str]) -> str:
    """What something is called in the module it's used in, adding it to the imports, e.g. ItemStack (or ItemStack2 if a
    different ItemStack is already)."""
    if (module, name) not in imports:
        taken = set(imports.values())
        local_name, suffix = name, 2
        while local_name in taken:
            local_name, suffix = f"{name}{suffix}", suffix + 1
        imports[module, name] = local_name
    return imports[module, name]


def bracketed(opening: str, items: list[str], closing: str, indent: int) -> str:
    """e.g. [1, 2, 3], or if that's too long, one item per line."""
    inline = f"{opening}{', '.join(items)}{closing}"
    if indent + len(inline) <= LINE_LENGTH and "\n" not in inline:
        return inline
    return "".join([f"{opening}\n", *(f"{' ' * (indent + 4)}{item},\n" for item in items), f"{' ' * indent}{closing.removeprefix(',')}"])


def python_code(value: object, imports: dict[tuple[str, str], str], indent: int = 0) -> str:
    """The Python that makes a value (e.g. one of vanilla's files, loaded into its model), e.g. RecipeCraftingShapeless(...),
    adding the classes it uses to imports. A model is its class with the fields it was given, and any extra keys."""
    def code(item: object) -> str:
        return python_code(item, imports, indent + 4)

    if isinstance(value, BaseModel):
        model = type(value)
        arguments = [f"{name}={code(getattr(value, name))}" for name in model.model_fields if name in value.model_fields_set]
        if value.model_extra:  # Their keys might not be Python names, e.g. minecraft:custom_name. As dict[str, Any], else type
            # checkers check its values against each of the class's fields
            extra = code({key.value if isinstance(key, Enum) else key: item for key, item in value.model_extra.items()})
            arguments.append(f"**dict[str, {import_name('typing', 'Any', imports)}]({extra})")
        origin = model.__pydantic_generic_metadata__["origin"] or model  # e.g. MinMaxBounds, rather than MinMaxBounds[int]
        return bracketed(f"{import_name(origin.__module__, origin.__qualname__, imports)}(", arguments, ")", indent)
    if isinstance(value, Enum):
        return f"{import_name(type(value).__module__, type(value).__qualname__, imports)}.{value.name}"
    if isinstance(value, dict):
        return bracketed("{", [f"{code(key)}: {code(item)}" for key, item in value.items()], "}", indent)
    if isinstance(value, list):
        return bracketed("[", [code(item) for item in value], "]", indent)
    if isinstance(value, tuple):
        return bracketed("(", [code(item) for item in value], ",)" if len(value) == 1 else ")", indent)
    return repr(value)


def folder_module(folder: tuple[str, ...], constants: dict[str, str], imports: dict[tuple[str, str], str]) -> str:
    """A folder's __init__.py: each of its files as a constant, e.g. TNT_MINECART = RecipeCraftingShapeless(...)."""
    where = f"{'/'.join(folder)}/ files" if folder else "own files, e.g. `from vanilla_mcdoc.vanilla.data.recipe import TNT_MINECART`"
    names_by_module: dict[str, list[str]] = {}
    for (module, name), local_name in sorted(imports.items()):
        names_by_module.setdefault(module, []).append(name if local_name == name else f"{name} as {local_name}")
    assert not constants.keys() & set(imports.values()), f"A file in vanilla/{'/'.join(folder)} has the same name as a class it uses"
    return "\n".join([
        f'"""Vanilla\'s {where}"""',
        *(f"from {module} import {', '.join(names)}" for module, names in names_by_module.items()),
        "",
        *(f"{name} = {code}\n" for name, code in sorted(constants.items())),
    ])


def package_files(files: dict[tuple[str, ...], tuple[str, str]]) -> dict[Path, str]:
    """Each folder's __init__.py in vanilla/, from each file loaded into its model (so vanilla_mcdoc/ has to have been generated)."""
    folders = {location[:index] for location in files for index in range(len(location))}  # Including vanilla/ itself, ()
    constants: dict[tuple[str, ...], dict[str, str]] = {folder: {} for folder in folders}  # Each folder's files' names and code
    imports: dict[tuple[str, ...], dict[tuple[str, str], str]] = {folder: {} for folder in folders}
    adapters: dict[str, TypeAdapter[object]] = {}
    importlib.invalidate_caches()  # vanilla_mcdoc/ was only just written
    for location, (symbol, contents) in files.items():
        *parent, name = location
        if symbol not in adapters:
            module, identifier = symbol_path_to_import_string_and_name(symbol)
            adapters[symbol] = TypeAdapter(getattr(importlib.import_module(module), identifier))
        value = adapters[symbol].validate_python(json.loads(contents))
        constants[tuple(parent)][constant_name(name)] = python_code(value, imports[tuple(parent)])
    return {VANILLA_DIRECTORY.joinpath(*folder, "__init__.py"): folder_module(folder, constants[folder], imports[folder]) for folder in folders}


def make_vanilla_package() -> None:
    files = package_files(vanilla_files())
    for stale in [path.parent for path in VANILLA_DIRECTORY.rglob("__init__.py") if path not in files]:
        if stale.exists():  # Not already gone with a stale folder it's in
            shutil.rmtree(stale)  # From another version, e.g. worldgen/configured_carver/ is worldgen/carver/ since 26.3
    for path, contents in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        write_file_if_changed(path, contents)
