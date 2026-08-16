"""
Generated from symbols.json for ::java::data::gametest::test_environment::ClockTimeTestEnvironment
Local link to file: generated_symbols/data/gametest/test_environment/ClockTimeTestEnvironment.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, ClassVar

from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class ClockTimeTestEnvironment:
    __resource_dir__: ClassVar[str] = 'test_environment'

    clock: Annotated[str, IdSpec(registry='world_clock')]
    time: Annotated[int, 'Range | Min `0` and above | inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::test_environment::ClockTimeTestEnvironment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "clock",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "world_clock"
                                }
                            }
                        }
                    ]
                }
            },
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

