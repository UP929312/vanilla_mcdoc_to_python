"""
Generated from symbols.json for ::java::data::gametest::test_environment::ClockTimeTestEnvironment
Local link to file: vanilla_mcdoc/data/gametest/test_environment/ClockTimeTestEnvironment.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class ClockTimeTestEnvironment(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'test_environment'

    clock: Annotated[str, IdSpec(registry='world_clock')]
    time: Annotated[int, Field(ge=0)]
