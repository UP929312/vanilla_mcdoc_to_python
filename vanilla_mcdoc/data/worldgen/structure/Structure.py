"""
Generated from symbols.json for ::java::data::worldgen::structure::Structure
Local link to file: vanilla_mcdoc/data/worldgen/structure/Structure.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.worldgen.structure.BuriedTreasure import BuriedTreasure
from vanilla_mcdoc.data.worldgen.structure.Jigsaw import Jigsaw
from vanilla_mcdoc.data.worldgen.structure.Mineshaft import Mineshaft
from vanilla_mcdoc.data.worldgen.structure.NetherFossil import NetherFossil
from vanilla_mcdoc.data.worldgen.structure.OceanRuin import OceanRuin
from vanilla_mcdoc.data.worldgen.structure.RuinedPortal import RuinedPortal
from vanilla_mcdoc.data.worldgen.structure.Shipwreck import Shipwreck
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.DecorationStep import DecorationStep
    from vanilla_mcdoc.data.worldgen.biome.MobCategory import MobCategory
    from vanilla_mcdoc.data.worldgen.structure.SpawnOverride import SpawnOverride
    from vanilla_mcdoc.data.worldgen.structure.TerrainAdaptation import TerrainAdaptation


class StructureBastionRemnant(Jigsaw):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:bastion_remnant', 'bastion_remnant'] = 'minecraft:bastion_remnant'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureBuriedTreasure(BuriedTreasure):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:buried_treasure', 'buried_treasure'] = 'minecraft:buried_treasure'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureDesertPyramid(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:desert_pyramid', 'desert_pyramid'] = 'minecraft:desert_pyramid'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureEndCity(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:end_city', 'end_city'] = 'minecraft:end_city'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureFortress(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:fortress', 'fortress'] = 'minecraft:fortress'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureIgloo(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:igloo', 'igloo'] = 'minecraft:igloo'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureJigsaw(Jigsaw):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:jigsaw', 'jigsaw'] = 'minecraft:jigsaw'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureJungleTemple(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:jungle_temple', 'jungle_temple'] = 'minecraft:jungle_temple'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureMineshaft(Mineshaft):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:mineshaft', 'mineshaft'] = 'minecraft:mineshaft'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureNetherFossil(NetherFossil):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:nether_fossil', 'nether_fossil'] = 'minecraft:nether_fossil'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureOceanMonument(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:ocean_monument', 'ocean_monument'] = 'minecraft:ocean_monument'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureOceanRuin(OceanRuin):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:ocean_ruin', 'ocean_ruin'] = 'minecraft:ocean_ruin'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructurePillagerOutpost(Jigsaw):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:pillager_outpost', 'pillager_outpost'] = 'minecraft:pillager_outpost'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureRuinedPortal(RuinedPortal):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:ruined_portal', 'ruined_portal'] = 'minecraft:ruined_portal'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureShipwreck(Shipwreck):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:shipwreck', 'shipwreck'] = 'minecraft:shipwreck'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureStronghold(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:stronghold', 'stronghold'] = 'minecraft:stronghold'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureSwampHut(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:swamp_hut', 'swamp_hut'] = 'minecraft:swamp_hut'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureVillage(Jigsaw):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:village', 'village'] = 'minecraft:village'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


class StructureWoodlandMansion(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    type: Literal['minecraft:woodland_mansion', 'woodland_mansion'] = 'minecraft:woodland_mansion'
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    step: DecorationStep  # The step when the structure generates.
    terrain_adaptation: TerrainAdaptation | None = None
    spawn_overrides: dict[MobCategory, SpawnOverride]


type Structure = Annotated[
    StructureBastionRemnant | StructureBuriedTreasure | StructureDesertPyramid | StructureEndCity | StructureFortress | StructureIgloo | StructureJigsaw | StructureJungleTemple | StructureMineshaft | StructureNetherFossil | StructureOceanMonument | StructureOceanRuin | StructurePillagerOutpost | StructureRuinedPortal | StructureShipwreck | StructureStronghold | StructureSwampHut | StructureVillage | StructureWoodlandMansion,
    Field(discriminator='type'),
]


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
