# ~~~ WHAT ARE WE TESTING ~~~

# Inline pair structs are materialized as sibling dataclasses instead of degrading to Any.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::world::item::shield::Shield
Local link to file: generated_symbols/world/item/shield/Shield.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

from generated_symbols.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from generated_symbols.util.color.DyeColorInt import DyeColorInt
    from generated_symbols.world.block.banner.BannerPatternLayer import BannerPatternLayer


@dataclass(kw_only=True)
class BlockEntityTagStruct:
    Base: DyeColorInt | None = None  # Base color.
    Patterns: list[BannerPatternLayer] | None = None


@dataclass(kw_only=True)
class Shield(ItemBase):
    BlockEntityTag: BlockEntityTagStruct | None = None  # Banner Data.
