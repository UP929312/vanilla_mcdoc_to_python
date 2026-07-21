# Generated from symbols.json for ::java::data::advancement::trigger::FishingRodHooked
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.data.advancement.trigger.CompositeEntity import CompositeEntity


@dataclass(kw_only=True)
class FishingRodHooked(TriggerBase):
    entity: CompositeEntity | None = None  # Entity that was pulled.
    item: ItemPredicate | None = None  # Item that was caught.
    rod: ItemPredicate | None = None  # Fishing rod used.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::FishingRodHooked": {
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
                "desc": "Entity that was pulled.",
                "key": "entity",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::CompositeEntity"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Item that was caught.",
                "key": "item",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::ItemPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Fishing rod used.",
                "key": "rod",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::ItemPredicate"
                },
                "optional": True
            }
        ]
    }
}

