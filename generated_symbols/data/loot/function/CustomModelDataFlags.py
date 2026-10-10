"""
Generated from symbols.json for ::java::data::loot::function::CustomModelDataFlags
Local link to file: generated_symbols/data/loot/function/CustomModelDataFlags.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from generated_symbols.base import GeneratedModel
from generated_symbols.data.loot.function.InsertListOperation import InsertListOperation
from generated_symbols.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation


class CustomModelDataFlagsAppend(GeneratedModel):
    values: list[bool]
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class CustomModelDataFlagsInsert(InsertListOperation):
    values: list[bool]
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class CustomModelDataFlagsReplaceAll(GeneratedModel):
    values: list[bool]
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class CustomModelDataFlagsReplaceSection(ReplaceSectionListOperation):
    values: list[bool]
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type CustomModelDataFlags = Annotated[
    CustomModelDataFlagsAppend | CustomModelDataFlagsInsert | CustomModelDataFlagsReplaceAll | CustomModelDataFlagsReplaceSection,
    Field(discriminator='mode'),
]


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

