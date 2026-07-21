# Generated from symbols.json for ::java::data::advancement::AdvancementCriterion
from dataclasses import dataclass


@dataclass(kw_only=True)
class AdvancementCriterion:
    trigger: str  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::AdvancementCriterion": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.",
                "key": "trigger",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::advancement::Trigger",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.3"
                                        }
                                    }
                                },
                                {
                                    "name": "id"
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.3"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "trigger_type"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "trigger"
                            ]
                        }
                    ],
                    "registry": "minecraft:trigger"
                }
            }
        ]
    }
}

