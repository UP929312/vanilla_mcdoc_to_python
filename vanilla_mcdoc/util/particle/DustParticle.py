"""
Generated from symbols.json for ::java::util::particle::DustParticle
Local link to file: vanilla_mcdoc/util/particle/DustParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.particle.DustColor import DustColor


class DustParticle(GeneratedModel):
    color: DustColor
    scale: Annotated[float, Field(ge=0.01, le=4)]
