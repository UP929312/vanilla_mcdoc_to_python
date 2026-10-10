"""
Generated from symbols.json for ::java::world::entity::BlockAttachedEntity
Local link to file: vanilla_mcdoc/world/entity/BlockAttachedEntity.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.EntityBase import EntityBase


class BlockAttachedEntity(EntityBase):
    block_pos: tuple[int, int, int] | None = None
