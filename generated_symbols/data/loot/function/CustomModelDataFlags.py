"""
Generated from symbols.json for ::java::data::loot::function::CustomModelDataFlags
Local link to file: generated_symbols/data/loot/function/CustomModelDataFlags.py
"""
# ~~~ CODE ~~~
from typing import Literal

from generated_symbols.base import GeneratedModel
from generated_symbols.data.loot.function.InsertListOperation import InsertListOperation
from generated_symbols.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation


class CustomModelDataFlagsAppend(GeneratedModel):
    values: list[bool]
    mode: Literal['minecraft:append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class CustomModelDataFlagsInsert(InsertListOperation):
    values: list[bool]
    mode: Literal['minecraft:insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class CustomModelDataFlagsReplaceAll(GeneratedModel):
    values: list[bool]
    mode: Literal['minecraft:replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class CustomModelDataFlagsReplaceSection(ReplaceSectionListOperation):
    values: list[bool]
    mode: Literal['minecraft:replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type CustomModelDataFlags = CustomModelDataFlagsAppend | CustomModelDataFlagsInsert | CustomModelDataFlagsReplaceAll | CustomModelDataFlagsReplaceSection


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

