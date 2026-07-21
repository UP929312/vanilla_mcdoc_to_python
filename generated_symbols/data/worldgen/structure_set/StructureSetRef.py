# Generated from symbols.json for ::java::data::worldgen::structure_set::StructureSetRef
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure_set.StructureSet import StructureSet


type StructureSetRef = str | StructureSet


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

