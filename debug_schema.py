import json
from typing import Any

from typed_models import KIND_TO_MODEL
from code_generation import make_python_file_content

RESOURCE_PATH = "::java::world::entity::mob::AttributeModifier"

with open('symbols.json', 'r', encoding='utf-8') as f:
    data: dict[str, Any] = json.load(f)['mcdoc'][RESOURCE_PATH]

class_type = KIND_TO_MODEL[data["kind"]]
model_obj = class_type(**data).remove_version_data()

print("==========================")
print("Model:")
print(model_obj)

python_code = make_python_file_content(RESOURCE_PATH, data, "BlockPredicateState")

print("==========================")
print(python_code)
