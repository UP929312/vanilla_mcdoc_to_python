"""
Generated from symbols.json for ::java::world::block::sculk_sensor::SculkSensor
Local link to file: vanilla_mcdoc/world/block/sculk_sensor/SculkSensor.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.game_event.VibrationListener import VibrationListener


class SculkSensor(GeneratedModel):
    last_vibration_frequency: Annotated[int, Field(ge=1, le=15)] | None = None
    listener: VibrationListener | None = None  # Vibration listener
