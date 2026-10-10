"""
Generated from symbols.json for ::java::world::component::block::Occupant
Local link to file: vanilla_mcdoc/world/component/block/Occupant.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.AnyEntity import AnyEntity


class Occupant(GeneratedModel):
    entity_data: AnyEntity
    min_ticks_in_hive: int
    ticks_in_hive: int
