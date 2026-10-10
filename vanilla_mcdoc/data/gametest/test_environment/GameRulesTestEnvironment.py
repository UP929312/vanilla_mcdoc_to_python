"""
Generated from symbols.json for ::java::data::gametest::test_environment::GameRulesTestEnvironment
Local link to file: vanilla_mcdoc/data/gametest/test_environment/GameRulesTestEnvironment.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownGameRuleId import KnownGameRuleId


class GameRulesTestEnvironment(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'test_environment'

    rules: dict[Annotated[str, IdSpec(registry='game_rule')] | KnownGameRuleId, bool | Annotated[int, Field(ge=-1)] | Annotated[int, Field(ge=1)] | Annotated[int, Field(ge=0)] | Annotated[int, Field(ge=1, le=1000)] | Annotated[int, Field(ge=0, le=8)]]


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
