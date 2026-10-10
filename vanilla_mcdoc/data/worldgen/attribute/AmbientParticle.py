"""
Generated from symbols.json for ::java::data::worldgen::attribute::AmbientParticle
Local link to file: vanilla_mcdoc/data/worldgen/attribute/AmbientParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.particle.Particle import Particle


class AmbientParticle(GeneratedModel):
    particle: Particle
    probability: Annotated[float, Field(ge=0, le=1)]
