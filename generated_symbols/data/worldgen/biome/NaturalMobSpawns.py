"""
Generated from symbols.json for ::java::data::worldgen::biome::NaturalMobSpawns
Local link to file: generated_symbols/data/worldgen/biome/NaturalMobSpawns.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.biome.MobSpawnCost import MobSpawnCost
    from generated_symbols.data.worldgen.biome.SpawnerDataMap import SpawnerDataMap


@dataclass(kw_only=True)
class NaturalMobSpawns:
    spawns_by_category: SpawnerDataMap
    spawn_costs: dict[Annotated[str, IdSpec(registry='entity')], MobSpawnCost]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::biome::NaturalMobSpawns": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "creature_spawn_probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 0.9999999
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "spawners",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::biome::SpawnerDataMap"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "spawns_by_category",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::biome::SpawnerDataMap"
                }
            },
            {
                "kind": "pair",
                "key": "spawn_costs",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "entity"
                                            }
                                        }
                                    }
                                ]
                            },
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::biome::MobSpawnCost"
                            }
                        }
                    ]
                }
            }
        ]
    }
}

