"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::CuboidModifier
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/CuboidModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class CuboidModifier(GeneratedModel):
    xz_size: IntProvider[Annotated[int, Field(ge=1, le=16)]] | Annotated[int, Field(ge=1, le=16)]
    y_size: IntProvider[Annotated[int, Field(ge=1, le=16)]] | Annotated[int, Field(ge=1, le=16)]
    include_interior: bool | None = None  # Defaults to `true`.
    include_edges: bool | None = None  # Defaults to `true`.
