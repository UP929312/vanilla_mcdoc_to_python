"""
Generated from symbols.json for ::java::data::gametest::test_environment::WeatherTestEnvironment
Local link to file: vanilla_mcdoc/data/gametest/test_environment/WeatherTestEnvironment.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.gametest.test_environment.Weather import Weather


class WeatherTestEnvironment(GeneratedModel):
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
