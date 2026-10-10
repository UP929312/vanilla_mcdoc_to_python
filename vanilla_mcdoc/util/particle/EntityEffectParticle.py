"""
Generated from symbols.json for ::java::util::particle::EntityEffectParticle
Local link to file: vanilla_mcdoc/util/particle/EntityEffectParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.particle.TranslucentParticle import TranslucentParticle


class EntityEffectParticle(GeneratedModel):
    color: TranslucentParticle
