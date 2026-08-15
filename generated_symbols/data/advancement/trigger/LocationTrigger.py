"""
Generated from symbols.json for ::java::data::advancement::trigger::LocationTrigger
Local link to file: generated_symbols/data/advancement/trigger/LocationTrigger.py
"""
# ~~~ CODE ~~~
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


LocationTrigger = AllOptional[PlayerConditions]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::LocationTrigger": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::advancement::trigger::AllOptional"
        },
        "typeArgs": [
            {
                "kind": "union",
                "members": [
                    {
                        "kind": "reference",
                        "path": "::java::data::advancement::predicate::LocationPredicate",
                        "attributes": [
                            {
                                "name": "deprecated",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "1.16"
                                    }
                                }
                            },
                            {
                                "name": "until",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "1.19"
                                    }
                                }
                            }
                        ]
                    },
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
                                "key": "location",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::data::advancement::predicate::LocationPredicate"
                                },
                                "optional": True
                            }
                        ],
                        "attributes": [
                            {
                                "name": "since",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "1.16"
                                    }
                                }
                            },
                            {
                                "name": "until",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "1.19"
                                    }
                                }
                            }
                        ]
                    },
                    {
                        "kind": "reference",
                        "path": "::java::data::advancement::trigger::PlayerConditions"
                    }
                ]
            }
        ]
    }
}

