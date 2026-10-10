"""
Generated from symbols.json for ::java::world::entity::mob::copper_golem::CopperGolem
Local link to file: vanilla_mcdoc/world/entity/mob/copper_golem/CopperGolem.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.world.entity.mob.MobBase import MobBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.copper_golem.WeatherState import WeatherState


class CopperGolem(MobBase):
    next_weather_age: Annotated[int, Field(ge=-2)] | None = None  # Gametime in ticks when the copper golem oxidizes.  `-2` represents "waxed"  `-1` will be replaced with a random time between 504000 and 552000 ticks later
    weather_state: WeatherState | None = None
