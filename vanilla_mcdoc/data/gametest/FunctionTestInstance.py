"""
Generated from symbols.json for ::java::data::gametest::FunctionTestInstance
Local link to file: vanilla_mcdoc/data/gametest/FunctionTestInstance.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from vanilla_mcdoc.data.gametest.TestData import TestData
from vanilla_mcdoc.minecraft_types import IdSpec


class FunctionTestInstance(TestData):
    __resource_dir__: ClassVar[str] = 'test_instance'

    function: Annotated[str, IdSpec(registry='test_function')]  # Test function (Java code) to run.
