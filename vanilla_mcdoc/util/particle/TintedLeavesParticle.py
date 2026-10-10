"""
Generated from symbols.json for ::java::util::particle::TintedLeavesParticle
Local link to file: vanilla_mcdoc/util/particle/TintedLeavesParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.RGBA import RGBA


class TintedLeavesParticle(GeneratedModel):
    color: RGBA
