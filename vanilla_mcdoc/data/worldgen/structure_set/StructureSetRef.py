"""
Generated from symbols.json for ::java::data::worldgen::structure_set::StructureSetRef
Local link to file: vanilla_mcdoc/data/worldgen/structure_set/StructureSetRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.structure_set.StructureSet import StructureSet


type StructureSetRef = Annotated[str, IdSpec(registry='worldgen/structure_set')] | StructureSet


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure_set::StructureSetRef": {
        "kind": "union",
        "members": [
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "worldgen/structure_set"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::worldgen::structure_set::StructureSet"
            }
        ]
    }
}
