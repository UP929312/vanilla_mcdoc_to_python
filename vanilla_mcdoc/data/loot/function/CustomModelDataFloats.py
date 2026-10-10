"""
Generated from symbols.json for ::java::data::loot::function::CustomModelDataFloats
Local link to file: vanilla_mcdoc/data/loot/function/CustomModelDataFloats.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.loot.function.InsertListOperation import InsertListOperation
from vanilla_mcdoc.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.FloatNumberProviderRef import FloatNumberProviderRef


class CustomModelDataFloatsAppend(GeneratedModel):
    values: list[FloatNumberProviderRef]
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class CustomModelDataFloatsInsert(InsertListOperation):
    values: list[FloatNumberProviderRef]
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class CustomModelDataFloatsReplaceAll(GeneratedModel):
    values: list[FloatNumberProviderRef]
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class CustomModelDataFloatsReplaceSection(ReplaceSectionListOperation):
    values: list[FloatNumberProviderRef]
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type CustomModelDataFloats = Annotated[
    CustomModelDataFloatsAppend | CustomModelDataFloatsInsert | CustomModelDataFloatsReplaceAll | CustomModelDataFloatsReplaceSection,
    Field(discriminator='mode'),
]
