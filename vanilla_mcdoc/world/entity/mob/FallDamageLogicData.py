"""
Generated from symbols.json for ::java::world::entity::mob::FallDamageLogicData
Local link to file: vanilla_mcdoc/world/entity/mob/FallDamageLogicData.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class FallDamageLogicData(GeneratedModel):
    current_explosion_impact_pos: tuple[float, float, float] | None = None  # Added mid-air after being hit by an explosion.
    current_impulse_context_reset_grace_time: Annotated[int, Field(ge=0)] | None = None  # Used by fall damage logic. Decreases by 1 every tick.
