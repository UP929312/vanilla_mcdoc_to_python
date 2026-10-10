"""
Generated from symbols.json for ::java::world::block::moving_piston::MovingPiston
Local link to file: vanilla_mcdoc/world/block/moving_piston/MovingPiston.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState
    from vanilla_mcdoc.util.direction.DirectionByte import DirectionByte


class MovingPiston(BlockEntity):
    blockState: BlockState | None = None  # Moving block represented by the moving piston.
    facing: DirectionByte | None = None  # The direction it is moving.
    progress: float | None = None  # How far it has moved.
    extending: bool | None = None
    source: bool | None = None  # Whether the moving piston is the piston head.
