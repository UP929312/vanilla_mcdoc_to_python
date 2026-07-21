# Generated from symbols.json for ::java::data::worldgen::biome::NaturalMobSpawns
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.biome.MobCategory import MobCategory
    from generated_symbols.data.worldgen.biome.MobSpawnCost import MobSpawnCost
    from generated_symbols.data.worldgen.biome.SpawnerData import SpawnerData
    from generated_symbols.util.FlatWeightedList import FlatWeightedList


@dataclass(kw_only=True)
class NaturalMobSpawns:
    spawns_by_category: dict[MobCategory, FlatWeightedList[SpawnerData]]
    spawn_costs: MobSpawnCost


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::biome::NaturalMobSpawns": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "spawns_by_category",
                "type": {
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
            },
            {
                "kind": "pair",
                "key": "spawn_costs",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::biome::MobSpawnCost"
                }
            }
        ]
    }
}

