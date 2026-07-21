# Generated from symbols.json for ::java::world::entity::cushion::Cushion
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.BlockAttachedEntity import BlockAttachedEntity

if TYPE_CHECKING:
    from generated_symbols.util.color.DyeColor import DyeColor


@dataclass(kw_only=True)
class Cushion(BlockAttachedEntity):
    color: DyeColor | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::cushion::Cushion": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::BlockAttachedEntity"
                }
            },
            {
                "kind": "pair",
                "key": "color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::DyeColor"
                },
                "optional": True
            }
        ]
    }
}

