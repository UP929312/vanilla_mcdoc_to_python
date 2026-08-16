"""
Generated from symbols.json for ::java::data::gametest::test_environment::TimeOfDayTestEnvironment
Local link to file: generated_symbols/data/gametest/test_environment/TimeOfDayTestEnvironment.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, ClassVar


@dataclass(kw_only=True)
class TimeOfDayTestEnvironment:
    __resource_dir__: ClassVar[str] = 'test_environment'

    time: Annotated[int, 'Range | Min `0` and above | inclusive']


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

