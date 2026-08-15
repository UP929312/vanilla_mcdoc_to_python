"""
Generated from symbols.json for ::java::data::advancement::trigger::CuredZombieVillagerTrigger
Local link to file: generated_symbols/data/advancement/trigger/CuredZombieVillagerTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
class CuredZombieVillagerTriggerTypeArg(PlayerConditions):
    zombie: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    villager: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.


CuredZombieVillagerTrigger = AllOptional[CuredZombieVillagerTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::CuredZombieVillagerTrigger": {
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
                        "desc": "Predicate context: Advancement Entity.",
                        "key": "zombie",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::trigger::AdvancementEntityPredicate"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Predicate context: Advancement Entity.",
                        "key": "villager",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::trigger::AdvancementEntityPredicate"
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}

