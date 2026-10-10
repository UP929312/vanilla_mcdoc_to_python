"""
Generated from symbols.json for ::java::world::item::shield::BlockEntityTag
Local link to file: vanilla_mcdoc/world/item/shield/BlockEntityTag.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.DyeColorInt import DyeColorInt
    from vanilla_mcdoc.world.block.banner.BannerPatternLayer import BannerPatternLayer


class BlockEntityTag(GeneratedModel):
    Base: DyeColorInt | None = None  # Base color.
    Patterns: list[BannerPatternLayer] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::shield::BlockEntityTag": {
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
    }
}
