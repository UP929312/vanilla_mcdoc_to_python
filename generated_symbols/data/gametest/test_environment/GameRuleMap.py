# Generated from symbols.json for ::java::data::gametest::test_environment::GameRuleMap
from typing import Any


type GameRuleMap = dict[str, Any]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::test_environment::GameRuleMap": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "game_rule"
                                }
                            }
                        }
                    ]
                },
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                {
                                    "keyword": "key"
                                }
                            ]
                        }
                    ],
                    "registry": "minecraft:game_rule"
                }
            }
        ]
    }
}

