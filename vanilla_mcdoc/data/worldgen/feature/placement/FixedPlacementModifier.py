"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::FixedPlacementModifier
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/FixedPlacementModifier.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class FixedPlacementModifier(GeneratedModel):
    positions: Annotated[list[tuple[int, int, int]], Field(min_length=1)]  # Fixed list of block positions to place the feature at.
