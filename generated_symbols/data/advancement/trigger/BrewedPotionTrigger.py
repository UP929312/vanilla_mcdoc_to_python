"""
Generated from symbols.json for ::java::data::advancement::trigger::BrewedPotionTrigger
Local link to file: generated_symbols/data/advancement/trigger/BrewedPotionTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions
from generated_symbols.world.component.predicate.PotionsPredicate import PotionsPredicate


@dataclass(kw_only=True)
class BrewedPotionTriggerTypeArg(PlayerConditions):
    potion: PotionsPredicate | None = None


BrewedPotionTrigger = AllOptional[BrewedPotionTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::BrewedPotionTrigger": {
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
                        "key": "potion",
                        "type": {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "string",
                                    "attributes": [
                                        {
                                            "name": "until",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "26.3"
                                                }
                                            }
                                        },
                                        {
                                            "name": "id",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "potion"
                                                }
                                            }
                                        }
                                    ]
                                },
                                {
                                    "kind": "reference",
                                    "path": "::java::world::component::predicate::PotionsPredicate",
                                    "attributes": [
                                        {
                                            "name": "since",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "26.3"
                                                }
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}

