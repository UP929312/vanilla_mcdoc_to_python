"""
Generated from symbols.json for ::java::data::worldgen::UniformHeightProvider
Local link to file: vanilla_mcdoc/data/worldgen/UniformHeightProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.VerticalAnchor import VerticalAnchor


class UniformHeightProvider(GeneratedModel):
    min_inclusive: VerticalAnchor
    max_inclusive: VerticalAnchor
