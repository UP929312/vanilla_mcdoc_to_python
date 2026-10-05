"""
Generated from symbols.json for ::java::data::gametest::TestInstance
Local link to file: generated_symbols/data/gametest/TestInstance.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar, Literal

from generated_symbols.data.gametest.BlockBasedTestInstance import BlockBasedTestInstance
from generated_symbols.data.gametest.FunctionTestInstance import FunctionTestInstance
from pydantic import Field


class TestInstanceBlockBased(BlockBasedTestInstance):
    __resource_dir__: ClassVar[str] = 'test_instance'

    type: Literal['minecraft:block_based'] = 'minecraft:block_based'


class TestInstanceFunction(FunctionTestInstance):
    type: Literal['minecraft:function'] = 'minecraft:function'


type TestInstance = Annotated[
    TestInstanceBlockBased | TestInstanceFunction,
    Field(discriminator='type'),
]


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

