"""
Generated from symbols.json for ::java::util::particle::VibrationParticleData
Local link to file: vanilla_mcdoc/util/particle/VibrationParticleData.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.particle.SafePositionSource import SafePositionSource


class VibrationParticleData(GeneratedModel):
    arrival_in_ticks: int  # Ticks in which to interpolate the particle's initial position to the destination.
    destination: SafePositionSource
