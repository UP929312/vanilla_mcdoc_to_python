"""
Generated from symbols.json for ::java::util::particle::ShriekParticle
Local link to file: vanilla_mcdoc/util/particle/ShriekParticle.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class ShriekParticle(GeneratedModel):
    delay: Annotated[int, Field(ge=0)]  # Ticks until the particle renders.
