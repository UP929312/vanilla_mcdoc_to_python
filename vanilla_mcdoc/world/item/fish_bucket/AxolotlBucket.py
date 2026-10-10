"""
Generated from symbols.json for ::java::world::item::fish_bucket::AxolotlBucket
Local link to file: vanilla_mcdoc/world/item/fish_bucket/AxolotlBucket.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.AnyEntity import AnyEntity


class AxolotlBucket(ItemBase):
    EntityTag: AnyEntity | None = None
    BucketVariantTag: int | None = None  # Turns into the `Variant` entity tag.
