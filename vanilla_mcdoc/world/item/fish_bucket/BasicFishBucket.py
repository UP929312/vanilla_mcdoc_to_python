"""
Generated from symbols.json for ::java::world::item::fish_bucket::BasicFishBucket
Local link to file: vanilla_mcdoc/world/item/fish_bucket/BasicFishBucket.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.AnyEntity import AnyEntity


class BasicFishBucket(GeneratedModel):
    EntityTag: AnyEntity | None = None
