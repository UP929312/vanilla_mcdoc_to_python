import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from context import Import, SingleSymbolContext
from minecraft_registry import get_resource_lookup_map
from schema_resolution import SchemaGraph
from typed_models import KIND_TO_MODEL
from utils import GENERATED_SYMBOLS_DIRECTORY, SYMBOLS_MAP, resource_path_to_python_path, symbol_path_to_import_string_and_name, symbol_path_to_object_name, manage_directory_and_inits, write_file_if_changed


SCHEMA_GRAPH = SchemaGraph.from_symbol_maps(SYMBOLS_MAP)
STATIC_SYMBOLS_DIRECTORY = Path("static_symbols")


def copy_static_files() -> None:
    """Copy the hand-written modules that generated code imports (e.g. base.py's GeneratedModel) into generated_symbols/,
    so the whole of generated_symbols/ can be deleted and regenerated."""
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
        "generated_symbols.data": "::java::data::",
        "generated_symbols.assets": "::java::assets::",
    }
    init_files = {GENERATED_SYMBOLS_DIRECTORY / "__init__.py": '"""Generated data and asset symbol packages."""\n'}
    for package, symbol_prefix in scopes.items():
        relative_package = package.removeprefix(f"{GENERATED_SYMBOLS_DIRECTORY.name}.")
        output_path = GENERATED_SYMBOLS_DIRECTORY.joinpath(*relative_package.split("."), "__init__.py")
        init_files[output_path] = make_init_content(paths, (symbol_prefix,))

    for output_path, file_contents in init_files.items():
        write_file_if_changed(output_path, file_contents)


def make_python_file_content(resource_type: str, resource_data: dict[str, Any], class_name: str) -> str:
    class_type = KIND_TO_MODEL[resource_data["kind"]]
    current_model = class_type(**resource_data).remove_version_data()

    signature_lines: list[str] = []
    ctx = SingleSymbolContext(current_symbol_path=resource_type, schema_graph=SCHEMA_GRAPH, resource_dir=get_resource_lookup_map().get(resource_type))
    body_lines = current_model.to_python_code(class_name, ctx)

    # Add TypeVar declarations after rendering so discovered local type params are included.
    if ctx.local_type_params:
        ctx.required_imports.add(Import('typing', 'TypeVar', False))
        # Includes a template's declared type params, since TemplateSchema.to_python_code adds them to the ctx
        for type_name in sorted({symbol_path_to_object_name(path) for path in ctx.local_type_params}):
            signature_lines.append(f"{type_name} = TypeVar('{type_name}')")
        signature_lines.append("\n")  # Two blank lines before the classes, like the imports

    # Build top-of-file imports from the final rendered import set.
    file_comment = [
        "\"\"\"",
        f"Generated from symbols.json for {resource_type}",
        f"Local link to file: {resource_path_to_python_path(resource_type).replace("\\", "/")}",
        "\"\"\"",
        "# ~~~ CODE ~~~"
    ]
    file_contents = "\n".join(file_comment + Import.to_python_code(ctx.required_imports) + signature_lines + ctx.additional_dataclasses + body_lines).rstrip() + "\n"

    # Add the raw model at the bottom, for reference:
    stringified_output = json.dumps({resource_type: resource_data}, indent=4).replace("true", "True").replace("false", "False")
    file_contents += f"\n\n# ~~~ MODEL DUMP ~~~\n_ = {stringified_output}\n"
    return file_contents


def make_python_file_of_model(resource_type: str, resource_data: dict[str, Any]) -> None:
    path, name = symbol_path_to_import_string_and_name(resource_type)
    output_path = GENERATED_SYMBOLS_DIRECTORY.joinpath(*path.split(".")[1:-1], name).with_suffix(".py")
    manage_directory_and_inits(output_path.parent)
    file_contents = make_python_file_content(resource_type, resource_data, class_name=output_path.stem)
    write_file_if_changed(output_path, file_contents)
