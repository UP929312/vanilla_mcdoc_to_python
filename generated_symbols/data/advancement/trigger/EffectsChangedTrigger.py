"""
Generated from symbols.json for ::java::data::advancement::trigger::EffectsChangedTrigger
Local link to file: generated_symbols/data/advancement/trigger/EffectsChangedTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.predicate.EntityEffectsPredicate import EntityEffectsPredicate
from generated_symbols.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
class EffectsChangedTriggerTypeArg(PlayerConditions):
    effects: EntityEffectsPredicate | None = None
    source: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.  Entity may not exist.


EffectsChangedTrigger = AllOptional[EffectsChangedTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::EffectsChangedTrigger": {
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
                        "key": "effects",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::EntityEffectsPredicate"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "attributes": [
                            {
                                "name": "since",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "1.17"
                                    }
                                }
                            }
                        ],
                        "desc": "Predicate context: Advancement Entity. \\\nEntity may not exist.",
                        "key": "source",
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

