"""
Generated from symbols.json for ::java::data::advancement::trigger::NetherTravelTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/NetherTravelTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.DistancePredicate import DistancePredicate
from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class NetherTravelTriggerTypeArg(PlayerConditions):
    start_position: LocationPredicate | None = None  # Where in the Overworld the player was when they travelled to the Nether.
    distance: DistancePredicate | None = None  # How far the player now is from the coordinate they started at in the Overworld before travelling.


NetherTravelTrigger = AllOptional[NetherTravelTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::NetherTravelTrigger": {
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
                        "attributes": [
                            {
                                "name": "since",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "1.18"
                                    }
                                }
                            }
                        ],
                        "desc": "Where in the Overworld the player was when they travelled to the Nether.",
                        "key": "start_position",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::LocationPredicate"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "How far the player now is from the coordinate they started at in the Overworld before travelling.",
                        "key": "distance",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::DistancePredicate"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "attributes": [
                            {
                                "name": "until",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "1.18"
                                    }
                                }
                            }
                        ],
                        "desc": "Where in the Overworld the player was when they travelled to the Nether.",
                        "key": "entered",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::LocationPredicate"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "attributes": [
                            {
                                "name": "until",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "1.18"
                                    }
                                }
                            }
                        ],
                        "desc": "Where in the Nether the player was when they travelled back to the Overworld.",
                        "key": "exited",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::LocationPredicate"
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}
