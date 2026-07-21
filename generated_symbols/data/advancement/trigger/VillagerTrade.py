# Generated from symbols.json for ::java::data::advancement::trigger::VillagerTrade
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.data.advancement.trigger.CompositeEntity import CompositeEntity


@dataclass(kw_only=True)
class VillagerTrade(TriggerBase):
    villager: CompositeEntity | None = None
    item: ItemPredicate | None = None  # Item that was purchased. `count` tag checks the item count from one trade, not the total amount traded for.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::VillagerTrade": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::TriggerBase"
                }
            },
            {
                "kind": "pair",
                "key": "villager",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::CompositeEntity"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Item that was purchased. `count` tag checks the item count from one trade, not the total amount traded for.",
                "key": "item",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::ItemPredicate"
                },
                "optional": True
            }
        ]
    }
}

