# Generated from symbols.json for ::java::data::gametest::test_environment::WeatherTestEnvironment
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.gametest.test_environment.Weather import Weather


@dataclass(kw_only=True)
class WeatherTestEnvironment:
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

