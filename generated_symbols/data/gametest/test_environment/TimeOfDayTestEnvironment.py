# Generated from symbols.json for ::java::data::gametest::test_environment::TimeOfDayTestEnvironment
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class TimeOfDayTestEnvironment:
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

