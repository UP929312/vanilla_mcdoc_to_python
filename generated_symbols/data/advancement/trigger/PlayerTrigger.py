# Generated from symbols.json for ::java::data::advancement::trigger::PlayerTrigger
from dataclasses import dataclass
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase


@dataclass(kw_only=True)
class PlayerTrigger(TriggerBase):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::PlayerTrigger": {
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
                            "path": "::java::data::advancement::trigger::TriggerBase"
                        }
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
                                        "value": "1.19"
                                    }
                                }
                            }
                        ],
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
                    }
                ]
            }
        ]
    }
}

