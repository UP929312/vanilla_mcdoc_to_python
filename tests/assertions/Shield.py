# ~~~ WHAT ARE WE TESTING ~~~

# Inline pair structs are materialized as sibling models instead of degrading to Any.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::world::item::shield::Shield
Local link to file: generated_symbols/world/item/shield/Shield.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel
from generated_symbols.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from generated_symbols.util.color.DyeColorInt import DyeColorInt
    from generated_symbols.world.block.banner.BannerPatternLayer import BannerPatternLayer


class BlockEntityTagStruct(GeneratedModel):
    Base: DyeColorInt | None = None  # Base color.
    Patterns: list[BannerPatternLayer] | None = None


class Shield(ItemBase):
    BlockEntityTag: BlockEntityTagStruct | None = None  # Banner Data.
