"""
Generated from symbols.json for ::java::world::entity::mob::raider::Spellcaster
Local link to file: vanilla_mcdoc/world/entity/mob/raider/Spellcaster.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.raider.RaiderBase import RaiderBase


class Spellcaster(RaiderBase):
    SpellTicks: int | None = None  # Ticks until the raider can cast its spell.
