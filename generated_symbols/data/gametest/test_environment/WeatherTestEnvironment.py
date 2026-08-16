"""
Generated from symbols.json for ::java::data::gametest::test_environment::WeatherTestEnvironment
Local link to file: generated_symbols/data/gametest/test_environment/WeatherTestEnvironment.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.gametest.test_environment.Weather import Weather


@dataclass(kw_only=True)
class WeatherTestEnvironment:
    __resource_dir__: ClassVar[str] = 'test_environment'

    weather: Weather


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::test_environment::WeatherTestEnvironment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "weather",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::gametest::test_environment::Weather"
                }
            }
        ]
    }
}

