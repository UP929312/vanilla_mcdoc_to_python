# Generated from symbols.json for ::java::world::item::shield::BlockEntityTag
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.color.DyeColorInt import DyeColorInt
    from generated_symbols.world.block.banner.BannerPatternLayer import BannerPatternLayer


@dataclass(kw_only=True)
class BlockEntityTag:
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

