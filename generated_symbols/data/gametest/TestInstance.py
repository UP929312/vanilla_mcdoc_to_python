"""
Generated from symbols.json for ::java::data::gametest::TestInstance
Local link to file: generated_symbols/data/gametest/TestInstance.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, Literal

from generated_symbols.data.gametest.TestData import TestData
from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class TestInstanceBlockBased(TestData):
    type: Literal['minecraft:block_based']


@dataclass(kw_only=True)
class TestInstanceFunction(TestData):
    type: Literal['minecraft:function']
    function: Annotated[str, IdSpec(registry='test_function')]  # Test function (Java code) to run.


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

