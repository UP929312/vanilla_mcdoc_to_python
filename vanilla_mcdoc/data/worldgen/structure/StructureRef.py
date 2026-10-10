"""
Generated from symbols.json for ::java::data::worldgen::structure::StructureRef
Local link to file: vanilla_mcdoc/data/worldgen/structure/StructureRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.structure.Structure import Structure


type StructureRef = Annotated[str, IdSpec(registry='worldgen/structure')] | Structure
