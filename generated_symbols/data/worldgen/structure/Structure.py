"""
Generated from symbols.json for ::java::data::worldgen::structure::Structure
Local link to file: generated_symbols/data/worldgen/structure/Structure.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.DecorationStep import DecorationStep
    from generated_symbols.data.worldgen.HeightProvider import HeightProvider
    from generated_symbols.data.worldgen.HeightmapType import HeightmapType
    from generated_symbols.data.worldgen.biome.MobCategory import MobCategory
    from generated_symbols.data.worldgen.structure.BiomeTemperature import BiomeTemperature
    from generated_symbols.data.worldgen.structure.JigsawDistanceLimits import JigsawDistanceLimits
    from generated_symbols.data.worldgen.structure.LiquidSettings import LiquidSettings
    from generated_symbols.data.worldgen.structure.MineshaftType import MineshaftType
    from generated_symbols.data.worldgen.structure.PoolAlias import PoolAlias
    from generated_symbols.data.worldgen.structure.RuinedPortalSetup import RuinedPortalSetup
    from generated_symbols.data.worldgen.structure.SpawnOverride import SpawnOverride
    from generated_symbols.data.worldgen.structure.TerrainAdaptation import TerrainAdaptation


@dataclass(kw_only=True)
class DimensionPaddingStruct:
    bottom: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None
    top: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None


@dataclass(kw_only=True)
class StructureBastionRemnant:
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:bastion_remnant']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]
    start_pool: Annotated[str, IdSpec(registry='worldgen/template_pool')]
    size: Annotated[int, 'Range | `1`-`20` | both inclusive']
    start_height: HeightProvider
    start_jigsaw_name: Annotated[str, IdSpec()] | None = None
    project_start_to_heightmap: HeightmapType | None = None
    max_distance_from_center: Annotated[int, 'Range | `1`-`128` | both inclusive'] | JigsawDistanceLimits[Annotated[int, 'Range | `1`-`128` | both inclusive']] | Annotated[int, 'Range | `1`-`128` | both inclusive'] | Annotated[int, 'Range | `1`-`116` | both inclusive'] | JigsawDistanceLimits[Annotated[int, 'Range | `1`-`116` | both inclusive']] | Annotated[int, 'Range | `1`-`116` | both inclusive']
    use_expansion_hack: bool
    pool_aliases: list[PoolAlias] | None = None
    dimension_padding: Annotated[int, 'Range | Min `0` and above | inclusive'] | DimensionPaddingStruct | None = None
    liquid_settings: LiquidSettings | None = None


@dataclass(kw_only=True)
class StructureBuriedTreasure:
    type: Literal['minecraft:buried_treasure']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureDesertPyramid:
    type: Literal['minecraft:desert_pyramid']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureEndCity:
    type: Literal['minecraft:end_city']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureFortress:
    type: Literal['minecraft:fortress']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureIgloo:
    type: Literal['minecraft:igloo']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureJigsaw:
    type: Literal['minecraft:jigsaw']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]
    start_pool: Annotated[str, IdSpec(registry='worldgen/template_pool')]
    size: Annotated[int, 'Range | `1`-`20` | both inclusive']
    start_height: HeightProvider
    start_jigsaw_name: Annotated[str, IdSpec()] | None = None
    project_start_to_heightmap: HeightmapType | None = None
    max_distance_from_center: Annotated[int, 'Range | `1`-`128` | both inclusive'] | JigsawDistanceLimits[Annotated[int, 'Range | `1`-`128` | both inclusive']] | Annotated[int, 'Range | `1`-`128` | both inclusive'] | Annotated[int, 'Range | `1`-`116` | both inclusive'] | JigsawDistanceLimits[Annotated[int, 'Range | `1`-`116` | both inclusive']] | Annotated[int, 'Range | `1`-`116` | both inclusive']
    use_expansion_hack: bool
    pool_aliases: list[PoolAlias] | None = None
    dimension_padding: Annotated[int, 'Range | Min `0` and above | inclusive'] | DimensionPaddingStruct | None = None
    liquid_settings: LiquidSettings | None = None


@dataclass(kw_only=True)
class StructureJungleTemple:
    type: Literal['minecraft:jungle_temple']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureMineshaft:
    type: Literal['minecraft:mineshaft']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]
    mineshaft_type: MineshaftType


@dataclass(kw_only=True)
class StructureNetherFossil:
    type: Literal['minecraft:nether_fossil']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]
    height: HeightProvider


@dataclass(kw_only=True)
class StructureOceanMonument:
    type: Literal['minecraft:ocean_monument']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureOceanRuin:
    type: Literal['minecraft:ocean_ruin']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]
    biome_temp: BiomeTemperature
    large_probability: Annotated[float, 'Range | `0`-`1` | both inclusive']
    cluster_probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class StructurePillagerOutpost:
    type: Literal['minecraft:pillager_outpost']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]
    start_pool: Annotated[str, IdSpec(registry='worldgen/template_pool')]
    size: Annotated[int, 'Range | `1`-`20` | both inclusive']
    start_height: HeightProvider
    start_jigsaw_name: Annotated[str, IdSpec()] | None = None
    project_start_to_heightmap: HeightmapType | None = None
    max_distance_from_center: Annotated[int, 'Range | `1`-`128` | both inclusive'] | JigsawDistanceLimits[Annotated[int, 'Range | `1`-`128` | both inclusive']] | Annotated[int, 'Range | `1`-`128` | both inclusive'] | Annotated[int, 'Range | `1`-`116` | both inclusive'] | JigsawDistanceLimits[Annotated[int, 'Range | `1`-`116` | both inclusive']] | Annotated[int, 'Range | `1`-`116` | both inclusive']
    use_expansion_hack: bool
    pool_aliases: list[PoolAlias] | None = None
    dimension_padding: Annotated[int, 'Range | Min `0` and above | inclusive'] | DimensionPaddingStruct | None = None
    liquid_settings: LiquidSettings | None = None


@dataclass(kw_only=True)
class StructureRuinedPortal:
    type: Literal['minecraft:ruined_portal']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]
    setups: list[RuinedPortalSetup]


@dataclass(kw_only=True)
class StructureShipwreck:
    type: Literal['minecraft:shipwreck']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]
    is_beached: bool | None = None


@dataclass(kw_only=True)
class StructureStronghold:
    type: Literal['minecraft:stronghold']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureSwampHut:
    type: Literal['minecraft:swamp_hut']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureVillage:
    type: Literal['minecraft:village']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]
    start_pool: Annotated[str, IdSpec(registry='worldgen/template_pool')]
    size: Annotated[int, 'Range | `1`-`20` | both inclusive']
    start_height: HeightProvider
    start_jigsaw_name: Annotated[str, IdSpec()] | None = None
    project_start_to_heightmap: HeightmapType | None = None
    max_distance_from_center: Annotated[int, 'Range | `1`-`128` | both inclusive'] | JigsawDistanceLimits[Annotated[int, 'Range | `1`-`128` | both inclusive']] | Annotated[int, 'Range | `1`-`128` | both inclusive'] | Annotated[int, 'Range | `1`-`116` | both inclusive'] | JigsawDistanceLimits[Annotated[int, 'Range | `1`-`116` | both inclusive']] | Annotated[int, 'Range | `1`-`116` | both inclusive']
    use_expansion_hack: bool
    pool_aliases: list[PoolAlias] | None = None
    dimension_padding: Annotated[int, 'Range | Min `0` and above | inclusive'] | DimensionPaddingStruct | None = None
    liquid_settings: LiquidSettings | None = None


@dataclass(kw_only=True)
class StructureWoodlandMansion:
    type: Literal['minecraft:woodland_mansion']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


type Structure = StructureBastionRemnant | StructureBuriedTreasure | StructureDesertPyramid | StructureEndCity | StructureFortress | StructureIgloo | StructureJigsaw | StructureJungleTemple | StructureMineshaft | StructureNetherFossil | StructureOceanMonument | StructureOceanRuin | StructurePillagerOutpost | StructureRuinedPortal | StructureShipwreck | StructureStronghold | StructureSwampHut | StructureVillage | StructureWoodlandMansion


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::Structure": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.19"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/structure_feature"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.19"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/structure_type"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
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
                                "value": "1.18.2"
                            }
                        }
                    }
                ],
                "key": "biomes",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "list",
                            "item": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "worldgen/biome"
                                            }
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "worldgen/biome"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        }
                    ]
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "desc": "The step when the structure generates.",
                "key": "step",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::DecorationStep"
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
                                "value": "1.18.2"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "desc": "Whether to add extra terrain below the structure.",
                "key": "adapt_noise",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "terrain_adaptation",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure::TerrainAdaptation"
                },
                "optional": True
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
                                "value": "1.18.2"
                            }
                        }
                    }
                ],
                "key": "spawn_overrides",
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
                                "kind": "reference",
                                "path": "::java::data::worldgen::structure::SpawnOverride"
                            }
                        }
                    ]
                }
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "config",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:structure_config"
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:structure_config"
                }
            }
        ]
    }
}

