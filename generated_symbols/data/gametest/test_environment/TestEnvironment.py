"""
Generated from symbols.json for ::java::data::gametest::test_environment::TestEnvironment
Local link to file: generated_symbols/data/gametest/test_environment/TestEnvironment.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.gametest.test_environment.Difficulty import Difficulty
    from generated_symbols.data.gametest.test_environment.Weather import Weather
    from generated_symbols.registry.KnownGameRuleId import KnownGameRuleId


@dataclass(kw_only=True)
class TestEnvironmentAllOf:
    type: Literal['minecraft:all_of']
    definitions: list[TestEnvironment]


@dataclass(kw_only=True)
class TestEnvironmentClockTime:
    type: Literal['minecraft:clock_time']
    clock: Annotated[str, IdSpec(registry='world_clock')]
    time: Annotated[int, 'Range | Min `0` and above | inclusive']


@dataclass(kw_only=True)
class TestEnvironmentDifficulty:
    type: Literal['minecraft:difficulty']
    difficulty: Difficulty


@dataclass(kw_only=True)
class TestEnvironmentFunction:
    type: Literal['minecraft:function']
    setup: Annotated[str, IdSpec(registry='function')] | None = None
    teardown: Annotated[str, IdSpec(registry='function')] | None = None


@dataclass(kw_only=True)
class TestEnvironmentGameRules:
    type: Literal['minecraft:game_rules']
    rules: dict[Annotated[str, IdSpec(registry='game_rule')] | KnownGameRuleId, bool | Annotated[int, 'Range | Min `-1` and above | inclusive'] | Annotated[int, 'Range | Min `1` and above | inclusive'] | Annotated[int, 'Range | Min `0` and above | inclusive'] | Annotated[int, 'Range | `1`-`1000` | both inclusive'] | Annotated[int, 'Range | `0`-`8` | both inclusive']]


@dataclass(kw_only=True)
class TestEnvironmentTimeOfDay:
    type: Literal['minecraft:time_of_day']
    time: Annotated[int, 'Range | Min `0` and above | inclusive']


@dataclass(kw_only=True)
class TestEnvironmentTimelineAttributes:
    type: Literal['minecraft:timeline_attributes']
    timelines: list[Annotated[str, IdSpec(registry='timeline')]]


@dataclass(kw_only=True)
class TestEnvironmentWeather:
    type: Literal['minecraft:weather']
    weather: Weather


type TestEnvironment = TestEnvironmentAllOf | TestEnvironmentClockTime | TestEnvironmentDifficulty | TestEnvironmentFunction | TestEnvironmentGameRules | TestEnvironmentTimeOfDay | TestEnvironmentTimelineAttributes | TestEnvironmentWeather


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

