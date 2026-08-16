"""
Generated from symbols.json for ::java::data::worldgen::structure_set::StructureSet
Local link to file: generated_symbols/data/worldgen/structure_set/StructureSet.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure_set.StructurePlacement import StructurePlacement
    from generated_symbols.data.worldgen.structure_set.StructureSetElement import StructureSetElement


@dataclass(kw_only=True)
class StructureSet:
    __resource_dir__: ClassVar[str] = 'worldgen/structure_set'

    structures: list[StructureSetElement]
    placement: StructurePlacement


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure_set::StructureSet": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "structures",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::structure_set::StructureSetElement"
                    }
                }
            },
            {
                "kind": "pair",
                "key": "placement",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure_set::StructurePlacement"
                }
            }
        ]
    }
}

