"""
Generated from symbols.json for ::java::data::gametest::test_environment::BoolGameRule
Local link to file: vanilla_mcdoc/data/gametest/test_environment/BoolGameRule.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class BoolGameRule(GeneratedModel):
    rule: str
    value: bool


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::test_environment::BoolGameRule": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "rule",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "game_rule",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "type": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "boolean"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}
