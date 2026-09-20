"""
Generated from symbols.json for ::java::data::gametest::test_environment::TimeOfDayTestEnvironment
Local link to file: generated_symbols/data/gametest/test_environment/TimeOfDayTestEnvironment.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from generated_symbols.base import GeneratedModel
from pydantic import Field


class TimeOfDayTestEnvironment(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'test_environment'

    time: Annotated[int, Field(ge=0)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::test_environment::TimeOfDayTestEnvironment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "time",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            }
        ]
    }
}

