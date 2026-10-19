"""
Generated from symbols.json for ::java::data::loot::function::CustomModelDataColors
Local link to file: vanilla_mcdoc/data/loot/function/CustomModelDataColors.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.loot.function.InsertListOperation import InsertListOperation
from vanilla_mcdoc.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.IntNumberProviderRef import IntNumberProviderRef
    from vanilla_mcdoc.util.color.RGB import RGB


class CustomModelDataColorsAppend(GeneratedModel):
    values: list[RGB | IntNumberProviderRef]
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class CustomModelDataColorsInsert(InsertListOperation):
    values: list[RGB | IntNumberProviderRef]
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class CustomModelDataColorsReplaceAll(GeneratedModel):
    values: list[RGB | IntNumberProviderRef]
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class CustomModelDataColorsReplaceSection(ReplaceSectionListOperation):
    values: list[RGB | IntNumberProviderRef]
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type CustomModelDataColors = Annotated[
    Annotated[CustomModelDataColorsAppend, Tag('minecraft:append')]
    | Annotated[CustomModelDataColorsInsert, Tag('minecraft:insert')]
    | Annotated[CustomModelDataColorsReplaceAll, Tag('minecraft:replace_all')]
    | Annotated[CustomModelDataColorsReplaceSection, Tag('minecraft:replace_section')],
    Discriminator(tag_of('mode')),
]
