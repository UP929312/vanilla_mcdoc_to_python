"""
Generated from symbols.json for ::java::data::gametest::test_environment::TimelineAttributesTestEnvironment
Local link to file: vanilla_mcdoc/data/gametest/test_environment/TimelineAttributesTestEnvironment.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class TimelineAttributesTestEnvironment(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'test_environment'

    timelines: list[Annotated[str, IdSpec(registry='timeline')]]
