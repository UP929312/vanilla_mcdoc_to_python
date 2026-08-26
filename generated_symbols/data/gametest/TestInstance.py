"""
Generated from symbols.json for ::java::data::gametest::TestInstance
Local link to file: generated_symbols/data/gametest/TestInstance.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import ClassVar, Literal

from generated_symbols.data.gametest.BlockBasedTestInstance import BlockBasedTestInstance
from generated_symbols.data.gametest.FunctionTestInstance import FunctionTestInstance


@dataclass(kw_only=True)
class TestInstanceBlockBased(BlockBasedTestInstance):
    __resource_dir__: ClassVar[str] = 'test_instance'

    type: Literal['minecraft:block_based']


@dataclass(kw_only=True)
class TestInstanceFunction(FunctionTestInstance):
    type: Literal['minecraft:function']


type TestInstance = TestInstanceBlockBased | TestInstanceFunction


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::TestInstance": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "test_instance_type"
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
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:test_instance"
                }
            }
        ]
    }
}

