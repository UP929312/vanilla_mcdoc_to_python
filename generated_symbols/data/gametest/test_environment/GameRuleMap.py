"""
Generated from symbols.json for ::java::data::gametest::test_environment::GameRuleMap
Local link to file: generated_symbols/data/gametest/test_environment/GameRuleMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownGameRuleId import KnownGameRuleId


type GameRuleMap = dict[Annotated[str, IdSpec(registry='game_rule')] | KnownGameRuleId, bool | Annotated[int, Field(ge=-1)] | Annotated[int, Field(ge=1)] | Annotated[int, Field(ge=0)] | Annotated[int, Field(ge=1, le=1000)] | Annotated[int, Field(ge=0, le=8)]]


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

