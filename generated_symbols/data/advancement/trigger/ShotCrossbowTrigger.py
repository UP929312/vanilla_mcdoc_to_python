"""
Generated from symbols.json for ::java::data::advancement::trigger::ShotCrossbowTrigger
Local link to file: generated_symbols/data/advancement/trigger/ShotCrossbowTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
class ShotCrossbowTriggerTypeArg(PlayerConditions):
    item: ItemPredicate | None = None  # Crossbow that was used.


ShotCrossbowTrigger = AllOptional[ShotCrossbowTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::ShotCrossbowTrigger": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::advancement::trigger::AllOptional"
        },
        "typeArgs": [
            {
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
        ]
    }
}

