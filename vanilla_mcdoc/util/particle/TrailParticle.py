"""
Generated from symbols.json for ::java::util::particle::TrailParticle
Local link to file: vanilla_mcdoc/util/particle/TrailParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.RGB import RGB


class TrailParticle(GeneratedModel):
    target: tuple[float, float, float]
    color: RGB
    duration: Annotated[int, Field(ge=1)]
