# Generated from symbols.json for ::java::data::worldgen::processor_list::PosRuleTest
from dataclasses import dataclass


@dataclass(kw_only=True)
class PosRuleTest:
    predicate_type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::PosRuleTest": {
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
                                    "value": "pos_rule_test"
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
                    "registry": "minecraft:pos_rule_test"
                }
            }
        ]
    }
}

