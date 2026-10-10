"""
Generated from symbols.json for ::java::world::entity::painting::Painting
Local link to file: vanilla_mcdoc/world/entity/painting/Painting.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.entity.BlockAttachedEntity import BlockAttachedEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.util.direction.HorizontalDirectionByte import HorizontalDirectionByte


class Painting(BlockAttachedEntity):
    facing: HorizontalDirectionByte | None = None  # Direction it is facing.
    variant: Annotated[str, IdSpec(registry='painting_variant')] | None = None  # Type of painting.
