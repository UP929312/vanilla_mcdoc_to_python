"""
Generated from symbols.json for ::java::data::loot::function::CustomModelDataFloats
Local link to file: generated_symbols/data/loot/function/CustomModelDataFloats.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.base import GeneratedModel
from generated_symbols.data.loot.function.InsertListOperation import InsertListOperation
from generated_symbols.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.FloatNumberProviderRef import FloatNumberProviderRef


class CustomModelDataFloatsAppend(GeneratedModel):
    values: list[FloatNumberProviderRef]
    mode: Literal['minecraft:append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class CustomModelDataFloatsInsert(InsertListOperation):
    values: list[FloatNumberProviderRef]
    mode: Literal['minecraft:insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class CustomModelDataFloatsReplaceAll(GeneratedModel):
    values: list[FloatNumberProviderRef]
    mode: Literal['minecraft:replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class CustomModelDataFloatsReplaceSection(ReplaceSectionListOperation):
    values: list[FloatNumberProviderRef]
    mode: Literal['minecraft:replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type CustomModelDataFloats = Annotated[
    CustomModelDataFloatsAppend | CustomModelDataFloatsInsert | CustomModelDataFloatsReplaceAll | CustomModelDataFloatsReplaceSection,
    Field(discriminator='mode'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CustomModelDataFloats": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "values",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::number_provider::FloatNumberProviderRef"
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

