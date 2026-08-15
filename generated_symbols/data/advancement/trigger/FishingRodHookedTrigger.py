"""
Generated from symbols.json for ::java::data::advancement::trigger::FishingRodHookedTrigger
Local link to file: generated_symbols/data/advancement/trigger/FishingRodHookedTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
from generated_symbols.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
class FishingRodHookedTriggerTypeArg(PlayerConditions):
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.  Entity that was pulled. Or the hook itself if no entity was hooked.
    item: ItemPredicate | None = None  # Item that was caught.
    rod: ItemPredicate | None = None  # Fishing rod used.


FishingRodHookedTrigger = AllOptional[FishingRodHookedTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::FishingRodHookedTrigger": {
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
                        "desc": "Predicate context: Advancement Entity. \\\nEntity that was pulled.\nOr the hook itself if no entity was hooked.",
                        "key": "entity",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::trigger::AdvancementEntityPredicate"
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
        ]
    }
}

