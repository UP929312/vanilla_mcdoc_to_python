"""
Generated from symbols.json for ::java::util::particle::EffectParticle
Local link to file: vanilla_mcdoc/util/particle/EffectParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.RGB import RGB


class EffectParticle(GeneratedModel):
    power: float | None = None  # Multiplier of initial velocity. Defaults to 1.0
    color: RGB | None = None
