# Generated from symbols.json for ::java::world::block::sculk_catalyst::SculkCatalyst
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from generated_symbols.world.block.sculk_catalyst.ChargeCursor import ChargeCursor


@dataclass(kw_only=True)
class SculkCatalyst(BlockEntity):
    cursors: list[ChargeCursor] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::sculk_catalyst::SculkCatalyst": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::BlockEntity"
                }
            },
            {
                "kind": "pair",
                "key": "cursors",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::block::sculk_catalyst::ChargeCursor"
                    }
                },
                "optional": True
            }
        ]
    }
}

