"""
Generated from symbols.json for ::java::world::block::Lockable
Local link to file: vanilla_mcdoc/world/block/Lockable.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate


class Lockable(GeneratedModel):
    lock: ItemPredicate | None = None  # Item predicate testing the item that a player has to be holding to open this container.
