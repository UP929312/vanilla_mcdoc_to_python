# Generated from symbols.json for ::java::data::loot::function::CustomModelDataFlags
from dataclasses import dataclass
from generated_symbols.data.loot.function.ListOperation import ListOperation


@dataclass(kw_only=True)
class CustomModelDataFlags(ListOperation):
    values: list[bool]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CustomModelDataFlags": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "values",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "boolean"
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

