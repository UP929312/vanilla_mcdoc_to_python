"""
Generated from symbols.json for ::java::world::entity::mob::NeutralMob
Local link to file: vanilla_mcdoc/world/entity/mob/NeutralMob.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import MinecraftUUID


class NeutralMob(GeneratedModel):
    anger_end_time: int | None = None  # The time anger ends.
    angry_at: MinecraftUUID | None = None
