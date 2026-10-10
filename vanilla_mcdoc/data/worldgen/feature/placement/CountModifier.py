"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::CountModifier
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/CountModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class CountModifier(GeneratedModel):
    count: IntProvider[Annotated[int, Field(ge=0, le=4096)]] | Annotated[int, Field(ge=0, le=4096)]
