"""
Generated from symbols.json for ::java::data::loot::function::CustomModelDataColors
Local link to file: generated_symbols/data/loot/function/CustomModelDataColors.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.base import GeneratedModel
from generated_symbols.data.loot.function.InsertListOperation import InsertListOperation
from generated_symbols.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.IntNumberProviderRef import IntNumberProviderRef
    from generated_symbols.util.color.RGB import RGB


class CustomModelDataColorsAppend(GeneratedModel):
    values: list[RGB | IntNumberProviderRef]
    mode: Literal['minecraft:append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class CustomModelDataColorsInsert(InsertListOperation):
    values: list[RGB | IntNumberProviderRef]
    mode: Literal['minecraft:insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class CustomModelDataColorsReplaceAll(GeneratedModel):
    values: list[RGB | IntNumberProviderRef]
    mode: Literal['minecraft:replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class CustomModelDataColorsReplaceSection(ReplaceSectionListOperation):
    values: list[RGB | IntNumberProviderRef]
    mode: Literal['minecraft:replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type CustomModelDataColors = Annotated[
    CustomModelDataColorsAppend | CustomModelDataColorsInsert | CustomModelDataColorsReplaceAll | CustomModelDataColorsReplaceSection,
    Field(discriminator='mode'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CustomModelDataColors": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "values",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "union",
                        "members": [
                            {
                                "kind": "reference",
                                "path": "::java::util::color::RGB"
                            },
                            {
                                "kind": "reference",
                                "path": "::java::data::number_provider::IntNumberProviderRef"
                            }
                        ]
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

