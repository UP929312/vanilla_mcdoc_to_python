"""
Generated from symbols.json for ::java::data::gametest::test_environment::TimeOfDayTestEnvironment
Local link to file: vanilla_mcdoc/data/gametest/test_environment/TimeOfDayTestEnvironment.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class TimeOfDayTestEnvironment(GeneratedModel):
    time: Annotated[int, Field(ge=0)]
