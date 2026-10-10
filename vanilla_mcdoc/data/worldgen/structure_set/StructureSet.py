"""
Generated from symbols.json for ::java::data::worldgen::structure_set::StructureSet
Local link to file: vanilla_mcdoc/data/worldgen/structure_set/StructureSet.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.structure_set.StructurePlacement import StructurePlacement
    from vanilla_mcdoc.data.worldgen.structure_set.StructureSetElement import StructureSetElement


class StructureSet(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure_set'

    structures: list[StructureSetElement]
    placement: StructurePlacement
