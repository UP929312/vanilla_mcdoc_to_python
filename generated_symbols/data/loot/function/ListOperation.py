"""
Generated from symbols.json for ::java::data::loot::function::ListOperation
Local link to file: generated_symbols/data/loot/function/ListOperation.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from generated_symbols.base import GeneratedModel
from generated_symbols.data.loot.function.InsertListOperation import InsertListOperation
from generated_symbols.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation


class ListOperationAppend(GeneratedModel):
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class ListOperationInsert(InsertListOperation):
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class ListOperationReplaceAll(GeneratedModel):
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class ListOperationReplaceSection(ReplaceSectionListOperation):
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type ListOperation = Annotated[
    ListOperationAppend | ListOperationInsert | ListOperationReplaceAll | ListOperationReplaceSection,
    Field(discriminator='mode'),
]


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
