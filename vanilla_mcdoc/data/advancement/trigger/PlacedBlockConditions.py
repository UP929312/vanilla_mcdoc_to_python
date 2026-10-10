"""
Generated from symbols.json for ::java::data::advancement::trigger::PlacedBlockConditions
Local link to file: vanilla_mcdoc/data/advancement/trigger/PlacedBlockConditions.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.advancement.trigger.BlockStateConditions import BlockStateConditions
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
    from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate


class PlacedBlockConditions(BlockStateConditions, PlayerConditions):
    item: ItemPredicate | None = None  # Item that was used to place the block before the item was consumed.
    location: LocationPredicate | None = None  # Predicate context: Advancement Location.
