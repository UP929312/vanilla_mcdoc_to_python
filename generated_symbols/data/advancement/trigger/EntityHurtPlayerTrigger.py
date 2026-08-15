"""
Generated from symbols.json for ::java::data::advancement::trigger::EntityHurtPlayerTrigger
Local link to file: generated_symbols/data/advancement/trigger/EntityHurtPlayerTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.predicate.DamagePredicate import DamagePredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
class EntityHurtPlayerTriggerTypeArg(PlayerConditions):
    damage: DamagePredicate | None = None


EntityHurtPlayerTrigger = AllOptional[EntityHurtPlayerTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::EntityHurtPlayerTrigger": {
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
                    }
                ]
            }
        ]
    }
}

