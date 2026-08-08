# Generated from symbols.json for ::java::world::item::shield::Shield
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


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::shield::Shield": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Banner Data.",
                "key": "BlockEntityTag",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Base color.",
                            "key": "Base",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::color::DyeColorInt"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "Patterns",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "reference",
                                    "path": "::java::world::block::banner::BannerPatternLayer"
                                }
                            },
                            "optional": True
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

