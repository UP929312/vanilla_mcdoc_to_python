"""
Generated from symbols.json for ::java::data::gametest::test_environment::TestEnvironment
Local link to file: generated_symbols/data/gametest/test_environment/TestEnvironment.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import ClassVar, Literal

from generated_symbols.data.gametest.test_environment.AllOffTestEnvironment import AllOffTestEnvironment
from generated_symbols.data.gametest.test_environment.ClockTimeTestEnvironment import ClockTimeTestEnvironment
from generated_symbols.data.gametest.test_environment.DifficultyTestEnvironment import DifficultyTestEnvironment
from generated_symbols.data.gametest.test_environment.FunctionTestEnvironment import FunctionTestEnvironment
from generated_symbols.data.gametest.test_environment.GameRulesTestEnvironment import GameRulesTestEnvironment
from generated_symbols.data.gametest.test_environment.TimelineAttributesTestEnvironment import TimelineAttributesTestEnvironment
from generated_symbols.data.gametest.test_environment.WeatherTestEnvironment import WeatherTestEnvironment


@dataclass(kw_only=True)
class TestEnvironmentAllOf(AllOffTestEnvironment):
    __resource_dir__: ClassVar[str] = 'test_environment'

    type: Literal['minecraft:all_of']


@dataclass(kw_only=True)
class TestEnvironmentClockTime(ClockTimeTestEnvironment):
    type: Literal['minecraft:clock_time']


@dataclass(kw_only=True)
class TestEnvironmentDifficulty(DifficultyTestEnvironment):
    type: Literal['minecraft:difficulty']


@dataclass(kw_only=True)
class TestEnvironmentFunction(FunctionTestEnvironment):
    type: Literal['minecraft:function']


@dataclass(kw_only=True)
class TestEnvironmentGameRules(GameRulesTestEnvironment):
    type: Literal['minecraft:game_rules']


@dataclass(kw_only=True)
class TestEnvironmentTimelineAttributes(TimelineAttributesTestEnvironment):
    type: Literal['minecraft:timeline_attributes']


@dataclass(kw_only=True)
class TestEnvironmentWeather(WeatherTestEnvironment):
    type: Literal['minecraft:weather']


type TestEnvironment = TestEnvironmentAllOf | TestEnvironmentClockTime | TestEnvironmentDifficulty | TestEnvironmentFunction | TestEnvironmentGameRules | TestEnvironmentTimelineAttributes | TestEnvironmentWeather


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

