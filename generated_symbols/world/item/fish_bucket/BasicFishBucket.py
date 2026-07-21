# Generated from symbols.json for ::java::world::item::fish_bucket::BasicFishBucket
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.entity.AnyEntity import AnyEntity


@dataclass(kw_only=True)
class BasicFishBucket:
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

