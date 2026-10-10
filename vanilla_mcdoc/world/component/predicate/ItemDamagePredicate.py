"""
Generated from symbols.json for ::java::world::component::predicate::ItemDamagePredicate
Local link to file: vanilla_mcdoc/world/component/predicate/ItemDamagePredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class ItemDamagePredicate(GeneratedModel):
    damage: MinMaxBounds[int] | int | None = None
    durability: MinMaxBounds[int] | int | None = None
