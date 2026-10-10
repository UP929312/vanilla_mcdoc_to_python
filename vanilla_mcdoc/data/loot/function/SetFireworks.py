"""
Generated from symbols.json for ::java::data::loot::function::SetFireworks
Local link to file: vanilla_mcdoc/data/loot/function/SetFireworks.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.data.loot.function.InsertListOperation import InsertListOperation
from vanilla_mcdoc.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.Explosion import Explosion


class ExplosionsStructAppend(GeneratedModel):
    values: list[Explosion]
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class ExplosionsStructInsert(InsertListOperation):
    values: list[Explosion]
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class ExplosionsStructReplaceAll(GeneratedModel):
    values: list[Explosion]
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class ExplosionsStructReplaceSection(ReplaceSectionListOperation):
    values: list[Explosion]
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type ExplosionsStruct = Annotated[
    ExplosionsStructAppend | ExplosionsStructInsert | ExplosionsStructReplaceAll | ExplosionsStructReplaceSection,
    Field(discriminator='mode'),
]


class SetFireworks(Conditions):
    flight_duration: Annotated[int, Field(ge=0, le=255)] | None = None  # If omitted, the flight duration of the item is left untouched - or set to 0 if the component did not exist before.
    explosions: ExplosionsStruct | None = None
