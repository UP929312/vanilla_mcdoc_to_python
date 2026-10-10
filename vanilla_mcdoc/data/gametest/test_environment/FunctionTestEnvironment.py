"""
Generated from symbols.json for ::java::data::gametest::test_environment::FunctionTestEnvironment
Local link to file: vanilla_mcdoc/data/gametest/test_environment/FunctionTestEnvironment.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class FunctionTestEnvironment(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'test_environment'

    setup: Annotated[str, IdSpec(registry='function')] | None = None
    teardown: Annotated[str, IdSpec(registry='function')] | None = None
