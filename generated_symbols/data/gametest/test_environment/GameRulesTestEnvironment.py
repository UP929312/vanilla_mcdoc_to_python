# Generated from symbols.json for ::java::data::gametest::test_environment::GameRulesTestEnvironment
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class GameRulesTestEnvironment:
    rules: dict[Annotated[str, IdSpec(registry='game_rule')], bool | Annotated[int, 'Range | Min `-1` and above | inclusive'] | Annotated[int, 'Range | Min `1` and above | inclusive'] | Annotated[int, 'Range | Min `0` and above | inclusive'] | Annotated[int, 'Range | `1`-`1000` | both inclusive'] | Annotated[int, 'Range | `0`-`8` | both inclusive']]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::test_environment::GameRulesTestEnvironment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "key": "bool_rules",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::gametest::test_environment::BoolGameRule"
                    }
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "key": "int_rules",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::gametest::test_environment::IntGameRule"
                    }
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "key": "rules",
                "type": {
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
        ]
    }
}

