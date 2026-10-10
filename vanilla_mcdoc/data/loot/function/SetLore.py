"""
Generated from symbols.json for ::java::data::loot::function::SetLore
Local link to file: vanilla_mcdoc/data/loot/function/SetLore.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.data.loot.function.InsertListOperation import InsertListOperation
from vanilla_mcdoc.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
    from vanilla_mcdoc.util.text.Text import Text


class SetLoreAppend(Conditions):
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    lore: list[Text]
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class SetLoreInsert(Conditions, InsertListOperation):
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    lore: list[Text]
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class SetLoreReplaceAll(Conditions):
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    lore: list[Text]
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class SetLoreReplaceSection(Conditions, ReplaceSectionListOperation):
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    lore: list[Text]
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type SetLore = Annotated[
    SetLoreAppend | SetLoreInsert | SetLoreReplaceAll | SetLoreReplaceSection,
    Field(discriminator='mode'),
]
