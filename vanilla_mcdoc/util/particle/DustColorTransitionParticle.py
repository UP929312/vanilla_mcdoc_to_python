"""
Generated from symbols.json for ::java::util::particle::DustColorTransitionParticle
Local link to file: vanilla_mcdoc/util/particle/DustColorTransitionParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.particle.DustColor import DustColor


class DustColorTransitionParticle(GeneratedModel):
    from_color: DustColor
    to_color: DustColor
    scale: Annotated[float, Field(ge=0.01, le=4)]
