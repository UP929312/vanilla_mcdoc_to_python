"""
Generated from symbols.json for ::java::data::worldgen::structure::Structure
Local link to file: generated_symbols/data/worldgen/structure/Structure.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal

from generated_symbols.data.worldgen.structure.BuriedTreasure import BuriedTreasure
from generated_symbols.data.worldgen.structure.Jigsaw import Jigsaw
from generated_symbols.data.worldgen.structure.Mineshaft import Mineshaft
from generated_symbols.data.worldgen.structure.NetherFossil import NetherFossil
from generated_symbols.data.worldgen.structure.OceanRuin import OceanRuin
from generated_symbols.data.worldgen.structure.RuinedPortal import RuinedPortal
from generated_symbols.data.worldgen.structure.Shipwreck import Shipwreck
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.DecorationStep import DecorationStep
    from generated_symbols.data.worldgen.biome.MobCategory import MobCategory
    from generated_symbols.data.worldgen.structure.SpawnOverride import SpawnOverride
    from generated_symbols.data.worldgen.structure.TerrainAdaptation import TerrainAdaptation


@dataclass(kw_only=True)
class StructureBastionRemnant(Jigsaw):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:bastion_remnant'] = 'minecraft:bastion_remnant'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureBuriedTreasure(BuriedTreasure):
    type: Literal['minecraft:buried_treasure'] = 'minecraft:buried_treasure'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureDesertPyramid:
    type: Literal['minecraft:desert_pyramid'] = 'minecraft:desert_pyramid'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureEndCity:
    type: Literal['minecraft:end_city'] = 'minecraft:end_city'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureFortress:
    type: Literal['minecraft:fortress'] = 'minecraft:fortress'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureIgloo:
    type: Literal['minecraft:igloo'] = 'minecraft:igloo'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureJigsaw(Jigsaw):
    type: Literal['minecraft:jigsaw'] = 'minecraft:jigsaw'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureJungleTemple:
    type: Literal['minecraft:jungle_temple'] = 'minecraft:jungle_temple'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureMineshaft(Mineshaft):
    type: Literal['minecraft:mineshaft'] = 'minecraft:mineshaft'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureNetherFossil(NetherFossil):
    type: Literal['minecraft:nether_fossil'] = 'minecraft:nether_fossil'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureOceanMonument:
    type: Literal['minecraft:ocean_monument'] = 'minecraft:ocean_monument'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureOceanRuin(OceanRuin):
    type: Literal['minecraft:ocean_ruin'] = 'minecraft:ocean_ruin'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructurePillagerOutpost(Jigsaw):
    type: Literal['minecraft:pillager_outpost'] = 'minecraft:pillager_outpost'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureRuinedPortal(RuinedPortal):
    type: Literal['minecraft:ruined_portal'] = 'minecraft:ruined_portal'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureShipwreck(Shipwreck):
    type: Literal['minecraft:shipwreck'] = 'minecraft:shipwreck'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureStronghold:
    type: Literal['minecraft:stronghold'] = 'minecraft:stronghold'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureSwampHut:
    type: Literal['minecraft:swamp_hut'] = 'minecraft:swamp_hut'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureVillage(Jigsaw):
    type: Literal['minecraft:village'] = 'minecraft:village'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


@dataclass(kw_only=True)
class StructureWoodlandMansion:
    type: Literal['minecraft:woodland_mansion'] = 'minecraft:woodland_mansion'
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

