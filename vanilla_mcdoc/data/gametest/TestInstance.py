"""
Generated from symbols.json for ::java::data::gametest::TestInstance
Local link to file: vanilla_mcdoc/data/gametest/TestInstance.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar, Literal

from pydantic import Field

from vanilla_mcdoc.data.gametest.BlockBasedTestInstance import BlockBasedTestInstance
from vanilla_mcdoc.data.gametest.FunctionTestInstance import FunctionTestInstance


class TestInstanceBlockBased(BlockBasedTestInstance):
    __resource_dir__: ClassVar[str] = 'test_instance'

    type: Literal['minecraft:block_based', 'block_based'] = 'minecraft:block_based'


class TestInstanceFunction(FunctionTestInstance):
    __resource_dir__: ClassVar[str] = 'test_instance'

    type: Literal['minecraft:function', 'function'] = 'minecraft:function'


type TestInstance = Annotated[
    TestInstanceBlockBased | TestInstanceFunction,
    Field(discriminator='type'),
]
