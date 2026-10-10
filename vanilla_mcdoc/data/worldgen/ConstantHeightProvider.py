"""
Generated from symbols.json for ::java::data::worldgen::ConstantHeightProvider
Local link to file: vanilla_mcdoc/data/worldgen/ConstantHeightProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.VerticalAnchor import VerticalAnchor


class ConstantHeightProvider(GeneratedModel):
    value: VerticalAnchor
