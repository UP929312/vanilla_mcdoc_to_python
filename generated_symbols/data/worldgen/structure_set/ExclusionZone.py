# Generated from symbols.json for ::java::data::worldgen::structure_set::ExclusionZone
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure_set.StructureSetRef import StructureSetRef


@dataclass(kw_only=True)
class ExclusionZone:
    other_set: StructureSetRef
    chunk_count: Annotated[int, 'Range | `1`-`16` | both inclusive']


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

