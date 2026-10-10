"""
Generated from symbols.json for ::java::data::loot::function::CustomModelDataStrings
Local link to file: generated_symbols/data/loot/function/CustomModelDataStrings.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from generated_symbols.base import GeneratedModel
from generated_symbols.data.loot.function.InsertListOperation import InsertListOperation
from generated_symbols.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation


class CustomModelDataStringsAppend(GeneratedModel):
    values: list[str]
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class CustomModelDataStringsInsert(InsertListOperation):
    values: list[str]
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class CustomModelDataStringsReplaceAll(GeneratedModel):
    values: list[str]
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class CustomModelDataStringsReplaceSection(ReplaceSectionListOperation):
    values: list[str]
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type CustomModelDataStrings = Annotated[
    CustomModelDataStringsAppend | CustomModelDataStringsInsert | CustomModelDataStringsReplaceAll | CustomModelDataStringsReplaceSection,
    Field(discriminator='mode'),
]


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

