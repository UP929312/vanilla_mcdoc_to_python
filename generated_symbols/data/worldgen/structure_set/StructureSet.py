# Generated from symbols.json for ::java::data::worldgen::structure_set::StructureSet
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure_set.StructurePlacement import StructurePlacement
    from generated_symbols.data.worldgen.structure_set.StructureSetElement import StructureSetElement


@dataclass(kw_only=True)
class StructureSet:
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

