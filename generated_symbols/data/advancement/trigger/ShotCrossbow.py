# Generated from symbols.json for ::java::data::advancement::trigger::ShotCrossbow
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate


@dataclass(kw_only=True)
class ShotCrossbow(TriggerBase):
    item: ItemPredicate | None = None  # Crossbow that was used.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::ShotCrossbow": {
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
                "desc": "Crossbow that was used.",
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

