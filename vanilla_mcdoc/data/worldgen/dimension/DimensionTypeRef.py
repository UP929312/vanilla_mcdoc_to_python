"""
Generated from symbols.json for ::java::data::worldgen::dimension::DimensionTypeRef
Local link to file: vanilla_mcdoc/data/worldgen/dimension/DimensionTypeRef.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec


type DimensionTypeRef = Annotated[str, IdSpec(registry='dimension_type')]
