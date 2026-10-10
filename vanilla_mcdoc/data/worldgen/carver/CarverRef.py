"""
Generated from symbols.json for ::java::data::worldgen::carver::CarverRef
Local link to file: vanilla_mcdoc/data/worldgen/carver/CarverRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.carver.ConfiguredCarver import ConfiguredCarver


type CarverRef = ConfiguredCarver | Annotated[str, IdSpec(registry='worldgen/carver')]
