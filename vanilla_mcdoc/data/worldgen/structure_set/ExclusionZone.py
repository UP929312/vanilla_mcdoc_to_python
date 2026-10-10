"""
Generated from symbols.json for ::java::data::worldgen::structure_set::ExclusionZone
Local link to file: vanilla_mcdoc/data/worldgen/structure_set/ExclusionZone.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.structure_set.StructureSetRef import StructureSetRef


class ExclusionZone(GeneratedModel):
    other_set: StructureSetRef
    chunk_count: Annotated[int, Field(ge=1, le=16)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure_set::ExclusionZone": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "other_set",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure_set::StructureSetRef"
                }
            },
            {
                "kind": "pair",
                "key": "chunk_count",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 16
                    }
                }
            }
        ]
    }
}
