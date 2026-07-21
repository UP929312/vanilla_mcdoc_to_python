# Generated from symbols.json for ::java::data::loot::function::CustomModelDataStrings
from dataclasses import dataclass
from generated_symbols.data.loot.function.ListOperation import ListOperation


@dataclass(kw_only=True)
class CustomModelDataStrings(ListOperation):
    values: list[str]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CustomModelDataStrings": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "values",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string"
                    }
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::ListOperation"
                }
            }
        ]
    }
}

