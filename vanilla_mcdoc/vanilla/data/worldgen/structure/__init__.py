"""Vanilla's data/worldgen/structure/ files"""
from typing import Any
from vanilla_mcdoc.data.worldgen.DecorationStep import DecorationStep
from vanilla_mcdoc.data.worldgen.HeightProvider import HeightProviderStructUniform
from vanilla_mcdoc.data.worldgen.HeightmapType import HeightmapType
from vanilla_mcdoc.data.worldgen.VerticalAnchor import VerticalAnchorStruct1, VerticalAnchorStruct3
from vanilla_mcdoc.data.worldgen.biome.MobCategory import MobCategory
from vanilla_mcdoc.data.worldgen.structure.BiomeTemperature import BiomeTemperature
from vanilla_mcdoc.data.worldgen.structure.BoundingBox import BoundingBox
from vanilla_mcdoc.data.worldgen.structure.LiquidSettings import LiquidSettings
from vanilla_mcdoc.data.worldgen.structure.MineshaftType import MineshaftType
from vanilla_mcdoc.data.worldgen.structure.PoolAlias import PoolAliasDirect, PoolAliasRandom, PoolAliasRandomGroup
from vanilla_mcdoc.data.worldgen.structure.RuinedPortalPlacement import RuinedPortalPlacement
from vanilla_mcdoc.data.worldgen.structure.RuinedPortalSetup import RuinedPortalSetup
from vanilla_mcdoc.data.worldgen.structure.SpawnOverride import SpawnOverride
from vanilla_mcdoc.data.worldgen.structure.Structure import StructureBuriedTreasure, StructureDesertPyramid, StructureEndCity, StructureFortress, StructureIgloo, StructureJigsaw, StructureJungleTemple, StructureMineshaft, StructureNetherFossil, StructureOceanMonument, StructureOceanRuin, StructureRuinedPortal, StructureShipwreck, StructureStronghold, StructureSwampHut, StructureWoodlandMansion
from vanilla_mcdoc.data.worldgen.structure.TerrainAdaptation import TerrainAdaptation
from vanilla_mcdoc.util.FlatWeightedEntry import FlatWeightedEntry
from vanilla_mcdoc.util.WeightedEntry import WeightedEntry

ABANDONED_CAMP_BAMBOO_JUNGLE = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/bamboo_jungle',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_bamboo_jungle',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_BIRCH_FOREST = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/birch_forest',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_birch_forest',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_CHERRY_GROVE = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/cherry_grove',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_cherry_grove',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_DAPPLED_FOREST = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/dappled_forest',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_dappled_forest',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_FLOWER_FOREST = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/flower_forest',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_flower_forest',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_FOREST = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/forest',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_forest',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_MEADOW = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/meadow',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_meadow',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_OLD_GROWTH_BIRCH_FOREST = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/old_growth_birch_forest',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_old_growth_birch_forest',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_OLD_GROWTH_PINE_TAIGA = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/old_growth_pine_taiga',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_old_growth_pine_taiga',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_OLD_GROWTH_SPRUCE_TAIGA = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/old_growth_spruce_taiga',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_old_growth_spruce_taiga',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_PALE_GARDEN = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/pale_garden',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_pale_garden',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_SAVANNA = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/savanna',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_savanna',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_SNOWY_TAIGA = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/snowy_taiga',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_snowy_taiga',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_SPARSE_JUNGLE = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/sparse_jungle',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_sparse_jungle',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_SWAMP = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/swamp',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_swamp',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_TAIGA = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/taiga',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_taiga',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_WINDSWEPT_FOREST = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/windswept_forest',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_windswept_forest',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ABANDONED_CAMP_WOODED_BADLANDS = StructureJigsaw(
    start_pool='minecraft:abandoned_camp/tent/wooded_badlands',
    size=2,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/abandoned_camp_wooded_badlands',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

ANCIENT_CITY = StructureJigsaw(
    start_pool='minecraft:ancient_city/city_center',
    size=7,
    start_height=VerticalAnchorStruct1(absolute=-27),
    start_jigsaw_name='minecraft:city_anchor',
    max_distance_from_center=116,
    use_expansion_hack=False,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/ancient_city',
    step=DecorationStep.UNDERGROUNDDECORATION,
    terrain_adaptation=TerrainAdaptation.BEARDBOX,
    spawn_overrides={
        MobCategory.AMBIENT: SpawnOverride(bounding_box=BoundingBox.FULL, spawns=[]),
        MobCategory.AXOLOTLS: SpawnOverride(bounding_box=BoundingBox.FULL, spawns=[]),
        MobCategory.CREATURE: SpawnOverride(bounding_box=BoundingBox.FULL, spawns=[]),
        MobCategory.MISC: SpawnOverride(bounding_box=BoundingBox.FULL, spawns=[]),
        MobCategory.MONSTER: SpawnOverride(bounding_box=BoundingBox.FULL, spawns=[]),
        MobCategory.UNDERGROUNDWATERCREATURE: SpawnOverride(bounding_box=BoundingBox.FULL, spawns=[]),
        MobCategory.WATERAMBIENT: SpawnOverride(bounding_box=BoundingBox.FULL, spawns=[]),
        MobCategory.WATERCREATURE: SpawnOverride(bounding_box=BoundingBox.FULL, spawns=[]),
    },
)

BASTION_REMNANT = StructureJigsaw(
    start_pool='minecraft:bastion/starts',
    size=6,
    start_height=VerticalAnchorStruct1(absolute=33),
    max_distance_from_center=80,
    use_expansion_hack=False,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/bastion_remnant',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

BURIED_TREASURE = StructureBuriedTreasure(
    type='minecraft:buried_treasure',
    biomes='#minecraft:has_structure/buried_treasure',
    step=DecorationStep.UNDERGROUNDSTRUCTURES,
    spawn_overrides={},
)

DESERT_PYRAMID = StructureDesertPyramid(
    type='minecraft:desert_pyramid',
    biomes='#minecraft:has_structure/desert_pyramid',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

END_CITY = StructureEndCity(
    type='minecraft:end_city',
    biomes='#minecraft:has_structure/end_city',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

FORTRESS = StructureFortress(
    type='minecraft:fortress',
    biomes='#minecraft:has_structure/nether_fortress',
    step=DecorationStep.UNDERGROUNDDECORATION,
    spawn_overrides={
        MobCategory.MONSTER: SpawnOverride(
            bounding_box=BoundingBox.PIECE,
            spawns=[
                FlatWeightedEntry(
                    weight=10,
                    **dict[str, Any]({
                        'type': 'minecraft:blaze',
                        'count': {'type': 'minecraft:uniform', 'max_inclusive': 3, 'min_inclusive': 2},
                    }),
                ),
                FlatWeightedEntry(weight=5, **dict[str, Any]({'type': 'minecraft:zombified_piglin', 'count': 4})),
                FlatWeightedEntry(weight=8, **dict[str, Any]({'type': 'minecraft:wither_skeleton', 'count': 5})),
                FlatWeightedEntry(weight=2, **dict[str, Any]({'type': 'minecraft:skeleton', 'count': 5})),
                FlatWeightedEntry(weight=3, **dict[str, Any]({'type': 'minecraft:magma_cube', 'count': 4})),
            ],
        ),
    },
)

IGLOO = StructureIgloo(
    type='minecraft:igloo',
    biomes='#minecraft:has_structure/igloo',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

JUNGLE_PYRAMID = StructureJungleTemple(
    type='minecraft:jungle_temple',
    biomes='#minecraft:has_structure/jungle_temple',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

MANSION = StructureWoodlandMansion(
    type='minecraft:woodland_mansion',
    biomes='#minecraft:has_structure/woodland_mansion',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

MINESHAFT = StructureMineshaft(
    mineshaft_type=MineshaftType.NORMAL,
    type='minecraft:mineshaft',
    biomes='#minecraft:has_structure/mineshaft',
    step=DecorationStep.UNDERGROUNDSTRUCTURES,
    spawn_overrides={},
)

MINESHAFT_MESA = StructureMineshaft(
    mineshaft_type=MineshaftType.MESA,
    type='minecraft:mineshaft',
    biomes='#minecraft:has_structure/mineshaft_mesa',
    step=DecorationStep.UNDERGROUNDSTRUCTURES,
    spawn_overrides={},
)

MONUMENT = StructureOceanMonument(
    type='minecraft:ocean_monument',
    biomes='#minecraft:has_structure/ocean_monument',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={
        MobCategory.AXOLOTLS: SpawnOverride(bounding_box=BoundingBox.FULL, spawns=[]),
        MobCategory.MONSTER: SpawnOverride(
            bounding_box=BoundingBox.FULL,
            spawns=[
                FlatWeightedEntry(
                    weight=1,
                    **dict[str, Any]({
                        'type': 'minecraft:guardian',
                        'count': {'type': 'minecraft:uniform', 'max_inclusive': 4, 'min_inclusive': 2},
                    }),
                ),
            ],
        ),
        MobCategory.UNDERGROUNDWATERCREATURE: SpawnOverride(bounding_box=BoundingBox.FULL, spawns=[]),
    },
)

NETHER_FOSSIL = StructureNetherFossil(
    height=HeightProviderStructUniform(
        min_inclusive=VerticalAnchorStruct1(absolute=32),
        max_inclusive=VerticalAnchorStruct3(below_top=2),
        type='minecraft:uniform',
    ),
    type='minecraft:nether_fossil',
    biomes='#minecraft:has_structure/nether_fossil',
    step=DecorationStep.UNDERGROUNDDECORATION,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

OCEAN_RUIN_COLD = StructureOceanRuin(
    biome_temp=BiomeTemperature.COLD,
    large_probability=0.3,
    cluster_probability=0.9,
    type='minecraft:ocean_ruin',
    biomes='#minecraft:has_structure/ocean_ruin_cold',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

OCEAN_RUIN_WARM = StructureOceanRuin(
    biome_temp=BiomeTemperature.WARM,
    large_probability=0.3,
    cluster_probability=0.9,
    type='minecraft:ocean_ruin',
    biomes='#minecraft:has_structure/ocean_ruin_warm',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

PILLAGER_OUTPOST = StructureJigsaw(
    start_pool='minecraft:pillager_outpost/base_plates',
    size=7,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/pillager_outpost',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={
        MobCategory.MONSTER: SpawnOverride(
            bounding_box=BoundingBox.FULL,
            spawns=[FlatWeightedEntry(weight=1, **dict[str, Any]({'type': 'minecraft:pillager', 'count': 1}))],
        ),
    },
)

RUINED_PORTAL = StructureRuinedPortal(
    setups=[
        RuinedPortalSetup(
            placement=RuinedPortalPlacement.UNDERGROUND,
            air_pocket_probability=1.0,
            mossiness=0.2,
            overgrown=False,
            vines=False,
            can_be_cold=True,
            replace_with_blackstone=False,
            weight=0.5,
        ),
        RuinedPortalSetup(
            placement=RuinedPortalPlacement.ONLANDSURFACE,
            air_pocket_probability=0.0,
            mossiness=0.2,
            overgrown=False,
            vines=False,
            can_be_cold=True,
            replace_with_blackstone=False,
            weight=0.5,
        ),
    ],
    type='minecraft:ruined_portal',
    biomes='#minecraft:has_structure/ruined_portal_standard',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

RUINED_PORTAL_DESERT = StructureRuinedPortal(
    setups=[
        RuinedPortalSetup(
            placement=RuinedPortalPlacement.PARTLYBURIED,
            air_pocket_probability=0.0,
            mossiness=0.0,
            overgrown=False,
            vines=False,
            can_be_cold=False,
            replace_with_blackstone=False,
            weight=1.0,
        ),
    ],
    type='minecraft:ruined_portal',
    biomes='#minecraft:has_structure/ruined_portal_desert',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

RUINED_PORTAL_JUNGLE = StructureRuinedPortal(
    setups=[
        RuinedPortalSetup(
            placement=RuinedPortalPlacement.ONLANDSURFACE,
            air_pocket_probability=0.0,
            mossiness=0.8,
            overgrown=True,
            vines=True,
            can_be_cold=False,
            replace_with_blackstone=False,
            weight=1.0,
        ),
    ],
    type='minecraft:ruined_portal',
    biomes='#minecraft:has_structure/ruined_portal_jungle',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

RUINED_PORTAL_MOUNTAIN = StructureRuinedPortal(
    setups=[
        RuinedPortalSetup(
            placement=RuinedPortalPlacement.INMOUNTAIN,
            air_pocket_probability=1.0,
            mossiness=0.2,
            overgrown=False,
            vines=False,
            can_be_cold=True,
            replace_with_blackstone=False,
            weight=0.5,
        ),
        RuinedPortalSetup(
            placement=RuinedPortalPlacement.ONLANDSURFACE,
            air_pocket_probability=0.0,
            mossiness=0.2,
            overgrown=False,
            vines=False,
            can_be_cold=True,
            replace_with_blackstone=False,
            weight=0.5,
        ),
    ],
    type='minecraft:ruined_portal',
    biomes='#minecraft:has_structure/ruined_portal_mountain',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

RUINED_PORTAL_NETHER = StructureRuinedPortal(
    setups=[
        RuinedPortalSetup(
            placement=RuinedPortalPlacement.INNETHER,
            air_pocket_probability=0.0,
            mossiness=0.0,
            overgrown=False,
            vines=False,
            can_be_cold=False,
            replace_with_blackstone=True,
            weight=1.0,
        ),
    ],
    type='minecraft:ruined_portal',
    biomes='#minecraft:has_structure/ruined_portal_nether',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

RUINED_PORTAL_OCEAN = StructureRuinedPortal(
    setups=[
        RuinedPortalSetup(
            placement=RuinedPortalPlacement.ONOCEANFLOOR,
            air_pocket_probability=0.0,
            mossiness=0.8,
            overgrown=False,
            vines=False,
            can_be_cold=True,
            replace_with_blackstone=False,
            weight=1.0,
        ),
    ],
    type='minecraft:ruined_portal',
    biomes='#minecraft:has_structure/ruined_portal_ocean',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

RUINED_PORTAL_SWAMP = StructureRuinedPortal(
    setups=[
        RuinedPortalSetup(
            placement=RuinedPortalPlacement.ONOCEANFLOOR,
            air_pocket_probability=0.0,
            mossiness=0.5,
            overgrown=False,
            vines=True,
            can_be_cold=False,
            replace_with_blackstone=False,
            weight=1.0,
        ),
    ],
    type='minecraft:ruined_portal',
    biomes='#minecraft:has_structure/ruined_portal_swamp',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

SHIPWRECK = StructureShipwreck(
    is_beached=False,
    type='minecraft:shipwreck',
    biomes='#minecraft:has_structure/shipwreck',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

SHIPWRECK_BEACHED = StructureShipwreck(
    is_beached=True,
    type='minecraft:shipwreck',
    biomes='#minecraft:has_structure/shipwreck_beached',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={},
)

STRONGHOLD = StructureStronghold(
    type='minecraft:stronghold',
    biomes='#minecraft:has_structure/stronghold',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BURY,
    spawn_overrides={},
)

SWAMP_HUT = StructureSwampHut(
    type='minecraft:swamp_hut',
    biomes='#minecraft:has_structure/swamp_hut',
    step=DecorationStep.SURFACESTRUCTURES,
    spawn_overrides={
        MobCategory.CREATURE: SpawnOverride(
            bounding_box=BoundingBox.PIECE,
            spawns=[FlatWeightedEntry(weight=1, **dict[str, Any]({'type': 'minecraft:cat', 'count': 1}))],
        ),
        MobCategory.MONSTER: SpawnOverride(
            bounding_box=BoundingBox.PIECE,
            spawns=[FlatWeightedEntry(weight=1, **dict[str, Any]({'type': 'minecraft:witch', 'count': 1}))],
        ),
    },
)

TRAIL_RUINS = StructureJigsaw(
    start_pool='minecraft:trail_ruins/tower',
    size=7,
    start_height=VerticalAnchorStruct1(absolute=-15),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=False,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/trail_ruins',
    step=DecorationStep.UNDERGROUNDSTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BURY,
    spawn_overrides={},
)

TRIAL_CHAMBERS = StructureJigsaw(
    start_pool='minecraft:trial_chambers/chamber/end',
    size=20,
    start_height=HeightProviderStructUniform(
        min_inclusive=VerticalAnchorStruct1(absolute=-40),
        max_inclusive=VerticalAnchorStruct1(absolute=-20),
        type='minecraft:uniform',
    ),
    max_distance_from_center=116,
    use_expansion_hack=False,
    pool_aliases=[
        PoolAliasRandomGroup(
            groups=[
                WeightedEntry(
                    weight=1,
                    data=[
                        PoolAliasDirect(
                            alias='minecraft:trial_chambers/spawner/contents/ranged',
                            target='minecraft:trial_chambers/spawner/ranged/skeleton',
                            type='minecraft:direct',
                        ),
                        PoolAliasDirect(
                            alias='minecraft:trial_chambers/spawner/contents/slow_ranged',
                            target='minecraft:trial_chambers/spawner/slow_ranged/skeleton',
                            type='minecraft:direct',
                        ),
                    ],
                ),
                WeightedEntry(
                    weight=1,
                    data=[
                        PoolAliasDirect(
                            alias='minecraft:trial_chambers/spawner/contents/ranged',
                            target='minecraft:trial_chambers/spawner/ranged/stray',
                            type='minecraft:direct',
                        ),
                        PoolAliasDirect(
                            alias='minecraft:trial_chambers/spawner/contents/slow_ranged',
                            target='minecraft:trial_chambers/spawner/slow_ranged/stray',
                            type='minecraft:direct',
                        ),
                    ],
                ),
                WeightedEntry(
                    weight=1,
                    data=[
                        PoolAliasDirect(
                            alias='minecraft:trial_chambers/spawner/contents/ranged',
                            target='minecraft:trial_chambers/spawner/ranged/poison_skeleton',
                            type='minecraft:direct',
                        ),
                        PoolAliasDirect(
                            alias='minecraft:trial_chambers/spawner/contents/slow_ranged',
                            target='minecraft:trial_chambers/spawner/slow_ranged/poison_skeleton',
                            type='minecraft:direct',
                        ),
                    ],
                ),
            ],
            type='minecraft:random_group',
        ),
        PoolAliasRandom(
            alias='minecraft:trial_chambers/spawner/contents/melee',
            targets=[
                WeightedEntry(weight=1, data='minecraft:trial_chambers/spawner/melee/zombie'),
                WeightedEntry(weight=1, data='minecraft:trial_chambers/spawner/melee/husk'),
                WeightedEntry(weight=1, data='minecraft:trial_chambers/spawner/melee/spider'),
            ],
            type='minecraft:random',
        ),
        PoolAliasRandom(
            alias='minecraft:trial_chambers/spawner/contents/small_melee',
            targets=[
                WeightedEntry(weight=1, data='minecraft:trial_chambers/spawner/small_melee/slime'),
                WeightedEntry(weight=1, data='minecraft:trial_chambers/spawner/small_melee/cave_spider'),
                WeightedEntry(weight=1, data='minecraft:trial_chambers/spawner/small_melee/silverfish'),
                WeightedEntry(weight=1, data='minecraft:trial_chambers/spawner/small_melee/baby_zombie'),
            ],
            type='minecraft:random',
        ),
    ],
    dimension_padding=10,
    liquid_settings=LiquidSettings.IGNOREWATERLOGGING,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/trial_chambers',
    step=DecorationStep.UNDERGROUNDSTRUCTURES,
    terrain_adaptation=TerrainAdaptation.ENCAPSULATE,
    spawn_overrides={
        MobCategory.AMBIENT: SpawnOverride(bounding_box=BoundingBox.PIECE, spawns=[]),
        MobCategory.AXOLOTLS: SpawnOverride(bounding_box=BoundingBox.PIECE, spawns=[]),
        MobCategory.CREATURE: SpawnOverride(bounding_box=BoundingBox.PIECE, spawns=[]),
        MobCategory.MISC: SpawnOverride(bounding_box=BoundingBox.PIECE, spawns=[]),
        MobCategory.MONSTER: SpawnOverride(bounding_box=BoundingBox.PIECE, spawns=[]),
        MobCategory.UNDERGROUNDWATERCREATURE: SpawnOverride(bounding_box=BoundingBox.PIECE, spawns=[]),
        MobCategory.WATERAMBIENT: SpawnOverride(bounding_box=BoundingBox.PIECE, spawns=[]),
        MobCategory.WATERCREATURE: SpawnOverride(bounding_box=BoundingBox.PIECE, spawns=[]),
    },
)

VILLAGE_DESERT = StructureJigsaw(
    start_pool='minecraft:village/desert/town_centers',
    size=6,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/village_desert',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

VILLAGE_PLAINS = StructureJigsaw(
    start_pool='minecraft:village/plains/town_centers',
    size=6,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/village_plains',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

VILLAGE_SAVANNA = StructureJigsaw(
    start_pool='minecraft:village/savanna/town_centers',
    size=6,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/village_savanna',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

VILLAGE_SNOWY = StructureJigsaw(
    start_pool='minecraft:village/snowy/town_centers',
    size=6,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/village_snowy',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)

VILLAGE_TAIGA = StructureJigsaw(
    start_pool='minecraft:village/taiga/town_centers',
    size=6,
    start_height=VerticalAnchorStruct1(absolute=0),
    project_start_to_heightmap=HeightmapType.WORLDSURFACEWORLDGEN,
    max_distance_from_center=80,
    use_expansion_hack=True,
    type='minecraft:jigsaw',
    biomes='#minecraft:has_structure/village_taiga',
    step=DecorationStep.SURFACESTRUCTURES,
    terrain_adaptation=TerrainAdaptation.BEARDTHIN,
    spawn_overrides={},
)
