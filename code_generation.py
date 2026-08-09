import json
from typing import Any

from schema_resolution import SchemaGraph
from typed_models import KIND_TO_MODEL, TemplateSchema, RenderContext, Import
from utils import GENERATED_SYMBOLS_DIRECTORY, SYMBOLS_MAP, symbol_path_to_import_string_and_name, symbol_path_to_object_name, manage_directory_and_inits


SCHEMA_GRAPH = SchemaGraph.from_symbol_maps(SYMBOLS_MAP)


def make_python_file_content(resource_type: str, resource_data: dict[str, Any], class_name: str) -> str:
    class_type = KIND_TO_MODEL[resource_data["kind"]]
    current_model = class_type(**resource_data).remove_version_data()

    signature_lines: list[str] = []
    ctx = RenderContext(current_symbol_path=resource_type, schema_graph=SCHEMA_GRAPH)
    body_lines = current_model.to_python_code(class_name, ctx)

    # Add TypeVar declarations after rendering so discovered local type params are included.
    if ctx.local_type_params:
        ctx.required_imports.add(Import('typing', 'TypeVar', False, True))
        declared_paths = set(type_param.path for type_param in current_model.type_params) if isinstance(current_model, TemplateSchema) else set()
        declared_names = sorted(symbol_path_to_object_name(path) for path in declared_paths)
        discovered_names = sorted(path.split("::")[-1] for path in ctx.local_type_params if path not in declared_paths)
        for type_name in declared_names + discovered_names:
            signature_lines.append(f"{type_name} = TypeVar('{type_name}')")
        signature_lines.append("")

    # Build top-of-file imports from the final rendered import set.
    file_comment = [f"# Generated from symbols.json for {resource_type}"]
    file_contents = "\n".join(file_comment + Import.to_python_code(ctx.required_imports) + signature_lines + ctx.additional_dataclasses + body_lines).rstrip() + "\n"

    # Add the raw model at the bottom, for reference:
    stringified_output = json.dumps({resource_type: resource_data}, indent=4).replace("true", "True").replace("false", "False")
    file_contents += f"\n\n# ~~~ MODEL DUMP ~~~\n_ = {stringified_output}\n\n"
    return file_contents


def make_python_file_of_model(resource_type: str, resource_data: dict[str, Any]) -> None:
    # Converts something like: `::java::data::loot::LootTablePoolEntry`
    # Into `generated_symbols/data/loot/LootTablePoolEntry` (with `LootTablePoolEntry` as a class inside)
    path, name = symbol_path_to_import_string_and_name(resource_type)
    output_path = GENERATED_SYMBOLS_DIRECTORY.joinpath(*path.split(".")[1:-1], name).with_suffix(".py")
    manage_directory_and_inits(output_path.parent)
    file_contents = make_python_file_content(resource_type, resource_data, class_name=output_path.stem)

    # Simple change detection:
    old_exists = output_path.exists()
    old_contents = output_path.read_text(encoding="utf-8") if old_exists else None
    if file_contents != old_contents:
        print("File change detected:", output_path)
        output_path.write_text(file_contents, encoding="utf-8")
