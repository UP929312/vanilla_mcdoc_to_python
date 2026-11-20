"""
Generated from symbols.json for ::java::data::dispense_behavior::DispenseSound
Local link to file: vanilla_mcdoc/data/dispense_behavior/DispenseSound.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef
    from vanilla_mcdoc.data.worldgen.FloatProvider import FloatProvider


class DispenseSound(GeneratedModel):
    sound: SoundEventRef
    volume: FloatProvider[float] | float
    pitch: FloatProvider[float] | float
