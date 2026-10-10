"""
Generated from symbols.json for ::java::world::entity::minecart::Minecart
Local link to file: vanilla_mcdoc/world/entity/minecart/Minecart.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.BlockState import BlockState


class Minecart(EntityBase):
    DisplayState: BlockState | None = None  # Custom block to display.
    DisplayOffset: int | None = None  # Vertical offset of the block display.
