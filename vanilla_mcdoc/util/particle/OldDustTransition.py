"""
Generated from symbols.json for ::java::util::particle::OldDustTransition
Local link to file: vanilla_mcdoc/util/particle/OldDustTransition.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.particle.DustColor import DustColor


class OldDustTransition(GeneratedModel):
    fromColor: DustColor
    toColor: DustColor
    scale: Annotated[float, Field(ge=0.01, le=4)]
