"""
Generated from symbols.json for ::java::data::loot::function::CustomModelDataFlags
Local link to file: vanilla_mcdoc/data/loot/function/CustomModelDataFlags.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.loot.function.InsertListOperation import InsertListOperation
from vanilla_mcdoc.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation


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
    Annotated[CustomModelDataFlagsAppend, Tag('minecraft:append')]
    | Annotated[CustomModelDataFlagsInsert, Tag('minecraft:insert')]
    | Annotated[CustomModelDataFlagsReplaceAll, Tag('minecraft:replace_all')]
    | Annotated[CustomModelDataFlagsReplaceSection, Tag('minecraft:replace_section')],
    Discriminator(tag_of('mode')),
]
