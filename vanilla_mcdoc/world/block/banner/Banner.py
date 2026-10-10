"""
Generated from symbols.json for ::java::world::block::banner::Banner
Local link to file: vanilla_mcdoc/world/block/banner/Banner.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.block.BlockEntity import BlockEntity
from vanilla_mcdoc.world.block.Nameable import Nameable

if TYPE_CHECKING:
    from vanilla_mcdoc.world.block.banner.BannerPatternLayer import BannerPatternLayer


class Banner(BlockEntity, Nameable):
    patterns: list[BannerPatternLayer] | None = None
