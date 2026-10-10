import json
from collections.abc import Iterable
from typing import Any

from context import SingleSymbolContext
from minecraft_registry import get_resource_lookup_map
from schema_resolution import get_schema_graph
from typed_models import KIND_TO_MODEL
from utils import (
    GENERATED_SYMBOLS_DIRECTORY,
    SETTINGS,
    STATIC_SYMBOLS_DIRECTORY,
    UPSTREAM_COMMITS,
    manage_directory_and_inits,
    minecraft_to_python_version,
    resource_path_to_python_path,
    symbol_path_to_import_string_and_name,
    write_file_if_changed,
)

# Filled in as each file is generated: for each module, the names it only imports under TYPE_CHECKING, and where from
TYPE_CHECKING_IMPORTS: dict[str, dict[str, tuple[str, str]]] = {}


def copy_static_files() -> None:
    """Copy the hand-written modules that generated code imports (e.g. base.py's GeneratedModel) into vanilla_mcdoc/,
    so the whole of vanilla_mcdoc/ can be deleted and regenerated."""
    manage_directory_and_inits(GENERATED_SYMBOLS_DIRECTORY)
    for path in STATIC_SYMBOLS_DIRECTORY.glob("*.py"):
        write_file_if_changed(GENERATED_SYMBOLS_DIRECTORY / path.name, path.read_text(encoding="utf-8"))


def make_init_content(symbol_paths: Iterable[str], included_prefixes: tuple[str, ...]) -> str:
    exports_by_name: dict[str, list[str]] = {}
    for symbol_path in symbol_paths:
        if not symbol_path.startswith(included_prefixes):
            continue
        module, name = symbol_path_to_import_string_and_name(symbol_path)
        if name not in exports_by_name:
            exports_by_name[name] = []
        exports_by_name[name].append(module)

    exports = {name: modules[0] for name, modules in exports_by_name.items() if len(modules) == 1}
    names = sorted(exports)

    lines = [
        '"""Exports for generated symbols."""',
        "",
        "\n".join(f"from {exports[name]} import {name}" for name in names),
        "",
        "__all__ = [",
        *(f'    "{name}",' for name in names),
        "]",
        "",
    ]
    return "\n".join(lines)


def make_init_files(symbol_paths: Iterable[str]) -> None:
    paths = tuple(symbol_paths)
    scopes = {
        "data": "::java::data::",
        "assets": "::java::assets::",
    }
    init_files = {
        GENERATED_SYMBOLS_DIRECTORY / "__init__.py": "\n".join([
            '"""Generated data and asset symbol packages."""',
            "",
            f'__version__ = "{minecraft_to_python_version(SETTINGS.minecraft_version)}"  # Read by pyproject.toml when building the package',
            f'__minecraft_version__ = "{SETTINGS.minecraft_version}"',
            # Which vanilla-mcdoc commit's symbols.json this was generated from (known when it was fetched by ci.py)
            *([f'__mcdoc_commit__ = "{UPSTREAM_COMMITS["vanilla-mcdoc"]}"'] if "vanilla-mcdoc" in UPSTREAM_COMMITS else []),
            "",
        ]),
    }
    for package, symbol_prefix in scopes.items():
        init_files[GENERATED_SYMBOLS_DIRECTORY / package / "__init__.py"] = make_init_content(paths, (symbol_prefix,))

    for output_path, file_contents in init_files.items():
        write_file_if_changed(output_path, file_contents)


def file_header(resource_type: str) -> list[str]:
    """The docstring at the top of every generated file, saying what it was generated from."""
    return [
        "\"\"\"",
        f"Generated from symbols.json for {resource_type}",
        f"Local link to file: {resource_path_to_python_path(resource_type).replace("\\", "/")}",
        "\"\"\"",
        "# ~~~ CODE ~~~"
    ]


def model_dump(resource_type: str, resource_data: dict[str, Any]) -> str:
    """The raw symbols.json data, for the bottom of the file, for reference (left out of builds for publishing, where it's 2/3 of the size)."""
    stringified_output = json.dumps({resource_type: resource_data}, indent=4).replace("true", "True").replace("false", "False")
    return f"\n\n# ~~~ MODEL DUMP ~~~\n_ = {stringified_output}\n"


def make_python_file_content(resource_type: str, resource_data: dict[str, Any], class_name: str) -> str:
    class_type = KIND_TO_MODEL[resource_data["kind"]]
    current_model = class_type(**resource_data).remove_version_data()

    ctx = SingleSymbolContext(current_symbol_path=resource_type, schema_graph=get_schema_graph(), resource_dir=get_resource_lookup_map().get(resource_type))
    body_lines = current_model.to_python_code(class_name, ctx)
    file_contents = "\n".join(file_header(resource_type) + ctx.to_python_code(body_lines)).rstrip() + "\n"
    if sources := ctx.type_checking_import_sources():
        TYPE_CHECKING_IMPORTS[symbol_path_to_import_string_and_name(resource_type)[0]] = sources
    return file_contents + (model_dump(resource_type, resource_data) if SETTINGS.include_model_dump else "")


def make_python_file_of_model(resource_type: str, resource_data: dict[str, Any]) -> None:
    path, name = symbol_path_to_import_string_and_name(resource_type)
    output_path = GENERATED_SYMBOLS_DIRECTORY.joinpath(*path.split(".")[1:-1], name).with_suffix(".py")
    manage_directory_and_inits(output_path.parent)
    file_contents = make_python_file_content(resource_type, resource_data, class_name=output_path.stem)
    write_file_if_changed(output_path, file_contents)


def make_type_checking_imports_file() -> None:
    """Writes vanilla_mcdoc/type_checking_imports.py: what each module only imports under TYPE_CHECKING (importing them
    for real would be circular), so base.py can import them for real when a model is first used."""
    lines = [
        '"""For each generated module, the names its annotations use that it only imports under `if TYPE_CHECKING:`, and where',
        "from (the module, and what it's called there). base.py imports them for real when a model is first used.\"\"\"",
        "",
        "TYPE_CHECKING_IMPORTS: dict[str, dict[str, tuple[str, str]]] = {",
    ]
    for module in sorted(TYPE_CHECKING_IMPORTS):
        lines.append(f"    {module!r}: {{")
        lines.extend(f"        {name!r}: {source!r}," for name, source in sorted(TYPE_CHECKING_IMPORTS[module].items()))
        lines.append("    },")
    write_file_if_changed(GENERATED_SYMBOLS_DIRECTORY / "type_checking_imports.py", "\n".join(lines + ["}", ""]))
