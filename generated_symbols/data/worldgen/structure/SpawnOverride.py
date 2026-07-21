# Generated from symbols.json for ::java::data::worldgen::structure::SpawnOverride
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.biome.SpawnerData import SpawnerData
    from generated_symbols.data.worldgen.structure.BoundingBox import BoundingBox
    from generated_symbols.util.FlatWeightedList import FlatWeightedList


@dataclass(kw_only=True)
class SpawnOverride:
    bounding_box: BoundingBox
    spawns: FlatWeightedList[SpawnerData]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::SpawnOverride": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "bounding_box",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure::BoundingBox"
                }
            },
            {
                "kind": "pair",
                "key": "spawns",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::FlatWeightedList"
                    },
                    "typeArgs": [
                        {
                            "kind": "reference",
                            "path": "::java::data::worldgen::biome::SpawnerData"
                        }
                    ]
                }
            }
        ]
    }
}

