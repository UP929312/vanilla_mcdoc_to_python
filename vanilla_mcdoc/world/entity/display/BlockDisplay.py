"""
Generated from symbols.json for ::java::world::entity::display::BlockDisplay
Local link to file: vanilla_mcdoc/world/entity/display/BlockDisplay.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.display.DisplayBase import DisplayBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class BlockDisplay(DisplayBase):
    block_state: BlockState | None = None  # Block state to display. Can display most block entities (eg. Chests, Beds, Furnaces, etc).  Does not display specially rendered block entities (eg. The bell in a bell block, an end gateway, the book on an enchantment table, a banner, a sign, etc).
