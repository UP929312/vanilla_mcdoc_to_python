"""
Generated from symbols.json for ::java::data::worldgen::biome::SpawnerDataMap
Local link to file: generated_symbols/data/worldgen/biome/SpawnerDataMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.biome.MobCategory import MobCategory
    from generated_symbols.data.worldgen.biome.SpawnerData import SpawnerData
    from generated_symbols.util.FlatWeightedList import FlatWeightedList


type SpawnerDataMap = dict[MobCategory, FlatWeightedList[SpawnerData]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::biome::SpawnerDataMap": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::biome::MobCategory"
                },
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

