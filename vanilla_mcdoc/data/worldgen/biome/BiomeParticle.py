"""
Generated from symbols.json for ::java::data::worldgen::biome::BiomeParticle
Local link to file: vanilla_mcdoc/data/worldgen/biome/BiomeParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.particle.Particle import Particle


class BiomeParticle(GeneratedModel):
    options: Particle
    probability: Annotated[float, Field(ge=0, le=1)]
