"""
Generated from symbols.json for ::java::world::entity::mob::fish::Salmon
Local link to file: vanilla_mcdoc/world/entity/mob/fish/Salmon.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.mob.fish.Fish import Fish

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.entity.SalmonType import SalmonType


class Salmon(Fish):
    type: SalmonType | None = None  # The size variant of the salmon.
