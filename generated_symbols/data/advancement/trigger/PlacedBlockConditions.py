"""
Generated from symbols.json for ::java::data::advancement::trigger::PlacedBlockConditions
Local link to file: generated_symbols/data/advancement/trigger/PlacedBlockConditions.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

from generated_symbols.data.advancement.trigger.BlockStateConditions import BlockStateConditions
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.data.advancement.predicate.LocationPredicate import LocationPredicate


@dataclass(kw_only=True)
class PlacedBlockConditions(BlockStateConditions, PlayerConditions):
    item: ItemPredicate | None = None  # Item that was used to place the block before the item was consumed.
    location: LocationPredicate | None = None  # Predicate context: Advancement Location.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::PlacedBlockConditions": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::PlayerConditions"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::BlockStateConditions"
                }
            },
            {
                "kind": "pair",
                "desc": "Item that was used to place the block before the item was consumed.",
                "key": "item",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::ItemPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Predicate context: Advancement Location.",
                "key": "location",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::LocationPredicate"
                },
                "optional": True
            }
        ]
    }
}

