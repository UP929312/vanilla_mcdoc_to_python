# Generated from symbols.json for ::java::data::worldgen::processor_list::RuleTest
from dataclasses import dataclass


@dataclass(kw_only=True)
class RuleTest:
    predicate_type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::RuleTest": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "predicate_type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "rule_test"
                                }
                            }
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
                                "predicate_type"
                            ]
                        }
                    ],
                    "registry": "minecraft:rule_test"
                }
            }
        ]
    }
}

