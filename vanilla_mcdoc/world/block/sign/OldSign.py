"""
Generated from symbols.json for ::java::world::block::sign::OldSign
Local link to file: vanilla_mcdoc/world/block/sign/OldSign.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.DyeColor import DyeColor


class OldSign(BlockEntity):
    Color: DyeColor | None = None  # Color the text has been dyed.
    GlowingText: bool | None = None
    Text1: str | None = None  # First line of text.
    Text2: str | None = None  # Second line of text.
    Text3: str | None = None  # Third line of text.
    Text4: str | None = None  # Fourth line of text.
