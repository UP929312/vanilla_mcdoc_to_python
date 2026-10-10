"""
Generated from symbols.json for ::java::util::particle::OldDustParticle
Local link to file: vanilla_mcdoc/util/particle/OldDustParticle.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class OldDustParticle(GeneratedModel):
    r: float
    g: float
    b: float
    scale: Annotated[float, Field(ge=0.01, le=4)]
