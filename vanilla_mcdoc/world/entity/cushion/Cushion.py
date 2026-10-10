"""
Generated from symbols.json for ::java::world::entity::cushion::Cushion
Local link to file: vanilla_mcdoc/world/entity/cushion/Cushion.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.BlockAttachedEntity import BlockAttachedEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.DyeColor import DyeColor


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
