"""
Generated from symbols.json for ::java::world::item::fish_bucket::BasicFishBucket
Local link to file: generated_symbols/world/item/fish_bucket/BasicFishBucket.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.world.entity.AnyEntity import AnyEntity


class BasicFishBucket(GeneratedModel):
    EntityTag: AnyEntity | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::fish_bucket::BasicFishBucket": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "EntityTag",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::AnyEntity"
                },
                "optional": True
            }
        ]
    }
}

