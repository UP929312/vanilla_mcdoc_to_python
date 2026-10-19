"""
Generated from symbols.json for ::java::data::loot::function::CustomModelDataStrings
Local link to file: vanilla_mcdoc/data/loot/function/CustomModelDataStrings.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.loot.function.InsertListOperation import InsertListOperation
from vanilla_mcdoc.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation


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
    Annotated[CustomModelDataStringsAppend, Tag('minecraft:append')]
    | Annotated[CustomModelDataStringsInsert, Tag('minecraft:insert')]
    | Annotated[CustomModelDataStringsReplaceAll, Tag('minecraft:replace_all')]
    | Annotated[CustomModelDataStringsReplaceSection, Tag('minecraft:replace_section')],
    Discriminator(tag_of('mode')),
]
