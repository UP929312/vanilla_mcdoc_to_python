# Generated from symbols.json for ::java::world::item::fish_bucket::AxolotlBucket
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from generated_symbols.world.entity.AnyEntity import AnyEntity


@dataclass(kw_only=True)
class AxolotlBucket(ItemBase):
    EntityTag: AnyEntity | None = None
    BucketVariantTag: int | None = None  # Turns into the `Variant` entity tag.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::fish_bucket::AxolotlBucket": {
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
                "key": "EntityTag",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::AnyEntity"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Turns into the `Variant` entity tag.",
                "key": "BucketVariantTag",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

