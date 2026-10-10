"""
Generated from symbols.json for ::java::world::entity::experience_orb::ExperienceOrb
Local link to file: vanilla_mcdoc/world/entity/experience_orb/ExperienceOrb.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.EntityBase import EntityBase


class ExperienceOrb(EntityBase):
    Age: int | None = None  # Ticks that it has existed.
    Health: int | None = None
    Value: int | None = None  # Amount of experience it will give.
    Count: int | None = None  # Remaining number of times that the orb can be picked up. When the orb is picked up, the value decreases by 1. When multiple orbs are merged, their values are added up to result orb. When the value reaches 0, the orb is depleted.
