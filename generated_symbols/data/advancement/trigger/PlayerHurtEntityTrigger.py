"""
Generated from symbols.json for ::java::data::advancement::trigger::PlayerHurtEntityTrigger
Local link to file: generated_symbols/data/advancement/trigger/PlayerHurtEntityTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.predicate.DamagePredicate import DamagePredicate
from generated_symbols.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
class PlayerHurtEntityTriggerTypeArg(PlayerConditions):
    damage: DamagePredicate | None = None
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.


PlayerHurtEntityTrigger = AllOptional[PlayerHurtEntityTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::PlayerHurtEntityTrigger": {
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
                        "key": "damage",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::DamagePredicate"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Predicate context: Advancement Entity.",
                        "key": "entity",
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

