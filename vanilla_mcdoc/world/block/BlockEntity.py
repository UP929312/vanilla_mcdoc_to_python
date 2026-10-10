"""
Generated from symbols.json for ::java::world::block::BlockEntity
Local link to file: vanilla_mcdoc/world/block/BlockEntity.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.DataComponentPatch import DataComponentPatch


class BlockEntity(GeneratedModel):
    id: Annotated[str, IdSpec(registry='block_entity_type')] | None = None
    x: int | None = None
    y: int | None = None
    z: int | None = None
    keepPacked: bool | None = None  # Unknown 0 for regular block entities
    components: DataComponentPatch | None = None
