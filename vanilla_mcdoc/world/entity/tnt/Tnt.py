"""
Generated from symbols.json for ::java::world::entity::tnt::Tnt
Local link to file: vanilla_mcdoc/world/entity/tnt/Tnt.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class Tnt(EntityBase):
    fuse: int | None = None  # Ticks until it explodes.
    block_state: BlockState | None = None  # Defaults to tnt.
    explosion_power: Annotated[float, Field(ge=0, le=128)] | None = None
    owner: MinecraftUUID | None = None  # The entity that primed this TNT.
