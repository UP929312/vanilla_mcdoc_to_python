"""
Generated from symbols.json for ::java::data::gametest::test_environment::IntGameRule
Local link to file: vanilla_mcdoc/data/gametest/test_environment/IntGameRule.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class IntGameRule(GeneratedModel):
    rule: str
    value: int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::test_environment::IntGameRule": {
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
                                            "value": "int"
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
                    "kind": "int"
                }
            }
        ]
    }
}
