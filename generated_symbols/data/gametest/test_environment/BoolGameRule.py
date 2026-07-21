# Generated from symbols.json for ::java::data::gametest::test_environment::BoolGameRule
from dataclasses import dataclass


@dataclass(kw_only=True)
class BoolGameRule:
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

