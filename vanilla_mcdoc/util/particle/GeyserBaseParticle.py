"""
Generated from symbols.json for ::java::util::particle::GeyserBaseParticle
Local link to file: vanilla_mcdoc/util/particle/GeyserBaseParticle.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class GeyserBaseParticle(GeneratedModel):
    water_blocks: Annotated[int, Field(ge=1)]  # Scales the particle size and its burst impulse.
    burst_impulse_base: float  # Scales the initial burst impulse
