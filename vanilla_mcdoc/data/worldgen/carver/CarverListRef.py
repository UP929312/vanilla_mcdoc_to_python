"""
Generated from symbols.json for ::java::data::worldgen::carver::CarverListRef
Local link to file: vanilla_mcdoc/data/worldgen/carver/CarverListRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.carver.ConfiguredCarver import ConfiguredCarver


type CarverListRef = ConfiguredCarver | Annotated[str, IdSpec(registry='worldgen/carver', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/carver')] | ConfiguredCarver]
