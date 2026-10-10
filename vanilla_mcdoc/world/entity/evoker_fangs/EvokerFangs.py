"""
Generated from symbols.json for ::java::world::entity::evoker_fangs::EvokerFangs
Local link to file: vanilla_mcdoc/world/entity/evoker_fangs/EvokerFangs.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.world.entity.EntityBase import EntityBase


class EvokerFangs(EntityBase):
    Warmup: int | None = None  # Ticks until the fangs pop out of the ground.
    Owner: MinecraftUUID | None = None
