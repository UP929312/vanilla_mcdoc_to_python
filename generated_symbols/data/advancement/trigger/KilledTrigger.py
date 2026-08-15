"""
Generated from symbols.json for ::java::data::advancement::trigger::KilledTrigger
Local link to file: generated_symbols/data/advancement/trigger/KilledTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.predicate.DamageSourcePredicate import DamageSourcePredicate
from generated_symbols.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
class KilledTriggerTypeArg(PlayerConditions):
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    killing_blow: DamageSourcePredicate | None = None


KilledTrigger = AllOptional[KilledTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::KilledTrigger": {
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
                        "key": "entity",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::trigger::AdvancementEntityPredicate"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "key": "killing_blow",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::DamageSourcePredicate"
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}

