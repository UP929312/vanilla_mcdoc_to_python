import json
from pathlib import Path
from typing import Any

from typed_models import KIND_TO_MODEL, TemplateSchema, RenderContext, Import
from utils import symbol_path_to_object_name, extract_child


def make_python_file_content(resource_type: str, resource_data: dict[str, Any], class_name: str) -> str:
    class_type = KIND_TO_MODEL[resource_data["kind"]]
    current_model = class_type(**resource_data).remove_version_data()

    signature_lines: list[str] = []
    ctx = RenderContext(current_symbol_path=resource_type)

    # Collect runtime imports for spread references (so we can inherit from them at runtime)
    # This is important because we can't have them in the TYPE_CHECKING block since they're required at runtime for inheritance.
    # For TemplateSchema, keep type params local
    if isinstance(current_model, TemplateSchema):  # Children are Structs or Lists
        # Add all the single var types, e.g. T | C | K | E | P | SPREAD
        ctx.local_type_params = set(type_param.path for type_param in current_model.type_params)

    body_lines = extract_child(current_model).to_python_code(class_name, ctx)

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
    file_contents = "\n".join(file_comment + ctx.imports_to_python_code() + signature_lines + body_lines).rstrip() + "\n"

    # Add the raw model at the bottom, for reference:
    stringified_output = json.dumps({resource_type: resource_data}, indent=4).replace("true", "True").replace("false", "False")
    file_contents += f"\n\n# ~~~ MODEL DUMP ~~~\n_ = {stringified_output}\n\n"
    return file_contents


def make_python_file_of_model(resource_type: str, resource_data: dict[str, Any], output_root: Path) -> None:
    # Converts something like: `::java::data::loot::LootTablePoolEntry`
    # Into `generated_symbols/data/loot/LootTablePoolEntry.py` (with `LootTablePoolEntry` as a class inside)
    *path_parts, name = resource_type.removeprefix("::java::").split("::")
    output_path = output_root.joinpath(*path_parts) / f"{name}.py"

    current = output_path.parent
    while current != output_root.parent and current != current.parent:
        init_file = current / "__init__.py"
        if not init_file.exists():
            init_file.parent.mkdir(parents=True, exist_ok=True)
            init_file.write_text("\n", encoding="utf-8")
        current = current.parent

    file_contents = make_python_file_content(resource_type, resource_data, class_name=output_path.stem)

    # Simple change detection:
    old_exists = output_path.exists()
    old_contents = output_path.read_text(encoding="utf-8") if old_exists else None
    if file_contents != old_contents:
        print(output_path)
        output_path.write_text(file_contents, encoding="utf-8")
