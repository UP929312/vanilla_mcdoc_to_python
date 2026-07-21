# Generated from symbols.json for ::java::data::loot::function::ListOperation
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.loot.function.ListOperationMode import ListOperationMode


@dataclass(kw_only=True)
class ListOperation:
    mode: ListOperationMode  # Determines how the existing list should be modified.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::ListOperation": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Determines how the existing list should be modified.",
                "key": "mode",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::ListOperationMode"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "mode"
                            ]
                        }
                    ],
                    "registry": "minecraft:list_operation"
                }
            }
        ]
    }
}

