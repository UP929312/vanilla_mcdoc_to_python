"""
Generated from symbols.json for ::java::data::gametest::test_environment::TestEnvironment
Local link to file: generated_symbols/data/gametest/test_environment/TestEnvironment.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar, Literal

from generated_symbols.data.gametest.test_environment.AllOffTestEnvironment import AllOffTestEnvironment
from generated_symbols.data.gametest.test_environment.ClockTimeTestEnvironment import ClockTimeTestEnvironment
from generated_symbols.data.gametest.test_environment.DifficultyTestEnvironment import DifficultyTestEnvironment
from generated_symbols.data.gametest.test_environment.FunctionTestEnvironment import FunctionTestEnvironment
from generated_symbols.data.gametest.test_environment.GameRulesTestEnvironment import GameRulesTestEnvironment
from generated_symbols.data.gametest.test_environment.TimelineAttributesTestEnvironment import TimelineAttributesTestEnvironment
from generated_symbols.data.gametest.test_environment.WeatherTestEnvironment import WeatherTestEnvironment
from pydantic import Field


class TestEnvironmentAllOf(AllOffTestEnvironment):
    __resource_dir__: ClassVar[str] = 'test_environment'

    type: Literal['minecraft:all_of', 'all_of'] = 'minecraft:all_of'


class TestEnvironmentClockTime(ClockTimeTestEnvironment):
    __resource_dir__: ClassVar[str] = 'test_environment'

    type: Literal['minecraft:clock_time', 'clock_time'] = 'minecraft:clock_time'


class TestEnvironmentDifficulty(DifficultyTestEnvironment):
    __resource_dir__: ClassVar[str] = 'test_environment'

    type: Literal['minecraft:difficulty', 'difficulty'] = 'minecraft:difficulty'


class TestEnvironmentFunction(FunctionTestEnvironment):
    __resource_dir__: ClassVar[str] = 'test_environment'

    type: Literal['minecraft:function', 'function'] = 'minecraft:function'


class TestEnvironmentGameRules(GameRulesTestEnvironment):
    __resource_dir__: ClassVar[str] = 'test_environment'

    type: Literal['minecraft:game_rules', 'game_rules'] = 'minecraft:game_rules'


class TestEnvironmentTimelineAttributes(TimelineAttributesTestEnvironment):
    __resource_dir__: ClassVar[str] = 'test_environment'

    type: Literal['minecraft:timeline_attributes', 'timeline_attributes'] = 'minecraft:timeline_attributes'


class TestEnvironmentWeather(WeatherTestEnvironment):
    __resource_dir__: ClassVar[str] = 'test_environment'

    type: Literal['minecraft:weather', 'weather'] = 'minecraft:weather'


type TestEnvironment = Annotated[
    TestEnvironmentAllOf | TestEnvironmentClockTime | TestEnvironmentDifficulty | TestEnvironmentFunction | TestEnvironmentGameRules | TestEnvironmentTimelineAttributes | TestEnvironmentWeather,
    Field(discriminator='type'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::test_environment::TestEnvironment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "test_environment_definition_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:test_environment_definition"
                }
            }
        ]
    }
}

