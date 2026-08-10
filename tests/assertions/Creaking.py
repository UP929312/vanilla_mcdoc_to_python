# ~~~ WHAT ARE WE TESTING ~~~

# This has an override of it's parent (inherited), but because it's the same type, we're fine.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::world::entity::mob::creaking::Creaking
Local link to file: generated_symbols/world/entity/mob/creaking/Creaking.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class Creaking(MobBase):
    home_pos: tuple[int, int, int] | None = None  # The creaking heart block that this is linked to.
