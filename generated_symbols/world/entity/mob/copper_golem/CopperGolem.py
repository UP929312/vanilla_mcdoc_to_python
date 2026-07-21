# Generated from symbols.json for ::java::world::entity::mob::copper_golem::CopperGolem
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.entity.mob.MobBase import MobBase

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.copper_golem.WeatherState import WeatherState


@dataclass(kw_only=True)
class CopperGolem(MobBase):
    next_weather_age: Annotated[int, 'Range | Min `-2` and above | inclusive'] | None = None  # Gametime in ticks when the copper golem oxidizes.  `-2` represents "waxed"  `-1` will be replaced with a random time between 504000 and 552000 ticks later
    weather_state: WeatherState | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::copper_golem::CopperGolem": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::MobBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Gametime in ticks when the copper golem oxidizes. \\\n`-2` represents \"waxed\" \\\n`-1` will be replaced with a random time between 504000 and 552000 ticks later",
                "key": "next_weather_age",
                "type": {
                    "kind": "long",
                    "valueRange": {
                        "kind": 0,
                        "min": -2
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "weather_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::copper_golem::WeatherState"
                },
                "optional": True
            }
        ]
    }
}

