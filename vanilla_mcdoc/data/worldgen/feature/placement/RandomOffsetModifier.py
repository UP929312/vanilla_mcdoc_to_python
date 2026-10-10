"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::RandomOffsetModifier
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/RandomOffsetModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class RandomOffsetModifier(GeneratedModel):
    xz_spread: IntProvider[Annotated[int, Field(ge=-16, le=16)]] | Annotated[int, Field(ge=-16, le=16)]
    y_spread: IntProvider[Annotated[int, Field(ge=-16, le=16)]] | Annotated[int, Field(ge=-16, le=16)]
