"""
Generated from symbols.json for ::java::world::item::shield::Shield
Local link to file: vanilla_mcdoc/world/item/shield/Shield.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.DyeColorInt import DyeColorInt
    from vanilla_mcdoc.world.block.banner.BannerPatternLayer import BannerPatternLayer


class BlockEntityTagStruct(GeneratedModel):
    Base: DyeColorInt | None = None  # Base color.
    Patterns: list[BannerPatternLayer] | None = None


class Shield(ItemBase):
    BlockEntityTag: BlockEntityTagStruct | None = None  # Banner Data.
