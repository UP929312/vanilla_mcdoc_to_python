"""
Generated from symbols.json for ::java::data::loot::function::ListOperation
Local link to file: generated_symbols/data/loot/function/ListOperation.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.loot.function.InsertListOperation import InsertListOperation
from generated_symbols.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation


@dataclass(kw_only=True)
class ListOperationAppend:
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class ListOperationInsert(InsertListOperation):
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class ListOperationReplaceAll:
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class ListOperationReplaceSection(ReplaceSectionListOperation):
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.


type ListOperation = ListOperationAppend | ListOperationInsert | ListOperationReplaceAll | ListOperationReplaceSection


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

