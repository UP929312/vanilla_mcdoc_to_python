"""Vanilla's data/worldgen/structure_set/ files"""
from vanilla_mcdoc.data.worldgen.structure_set.ExclusionZone import ExclusionZone
from vanilla_mcdoc.data.worldgen.structure_set.FrequencyReductionMethod import FrequencyReductionMethod
from vanilla_mcdoc.data.worldgen.structure_set.SpreadType import SpreadType
from vanilla_mcdoc.data.worldgen.structure_set.StructurePlacement import StructurePlacementConcentricRings, StructurePlacementRandomSpread
from vanilla_mcdoc.data.worldgen.structure_set.StructureSet import StructureSet
from vanilla_mcdoc.data.worldgen.structure_set.StructureSetElement import StructureSetElement

ABANDONED_CAMP = StructureSet(
    structures=[
        StructureSetElement(structure='minecraft:abandoned_camp_bamboo_jungle', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_birch_forest', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_cherry_grove', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_dappled_forest', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_flower_forest', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_forest', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_meadow', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_old_growth_pine_taiga', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_old_growth_birch_forest', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_old_growth_spruce_taiga', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_pale_garden', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_savanna', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_snowy_taiga', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_sparse_jungle', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_swamp', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_taiga', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_windswept_forest', weight=1),
        StructureSetElement(structure='minecraft:abandoned_camp_wooded_badlands', weight=1),
    ],
    placement=StructurePlacementRandomSpread(salt=91231127, spacing=37, separation=8, type='minecraft:random_spread'),
)

ANCIENT_CITIES = StructureSet(
    structures=[StructureSetElement(structure='minecraft:ancient_city', weight=1)],
    placement=StructurePlacementRandomSpread(salt=20083232, spacing=24, separation=8, type='minecraft:random_spread'),
)

BURIED_TREASURES = StructureSet(
    structures=[StructureSetElement(structure='minecraft:buried_treasure', weight=1)],
    placement=StructurePlacementRandomSpread(
        salt=0,
        frequency_reduction_method=FrequencyReductionMethod.LEGACYTYPE2,
        frequency=0.01,
        locate_offset=(9, 0, 9),
        spacing=1,
        separation=0,
        type='minecraft:random_spread',
    ),
)

DESERT_PYRAMIDS = StructureSet(
    structures=[StructureSetElement(structure='minecraft:desert_pyramid', weight=1)],
    placement=StructurePlacementRandomSpread(salt=14357617, spacing=32, separation=8, type='minecraft:random_spread'),
)

END_CITIES = StructureSet(
    structures=[StructureSetElement(structure='minecraft:end_city', weight=1)],
    placement=StructurePlacementRandomSpread(
        salt=10387313,
        spacing=20,
        separation=11,
        spread_type=SpreadType.TRIANGULAR,
        type='minecraft:random_spread',
    ),
)

IGLOOS = StructureSet(
    structures=[StructureSetElement(structure='minecraft:igloo', weight=1)],
    placement=StructurePlacementRandomSpread(salt=14357618, spacing=32, separation=8, type='minecraft:random_spread'),
)

JUNGLE_TEMPLES = StructureSet(
    structures=[StructureSetElement(structure='minecraft:jungle_pyramid', weight=1)],
    placement=StructurePlacementRandomSpread(salt=14357619, spacing=32, separation=8, type='minecraft:random_spread'),
)

MINESHAFTS = StructureSet(
    structures=[
        StructureSetElement(structure='minecraft:mineshaft', weight=1),
        StructureSetElement(structure='minecraft:mineshaft_mesa', weight=1),
    ],
    placement=StructurePlacementRandomSpread(
        salt=0,
        frequency_reduction_method=FrequencyReductionMethod.LEGACYTYPE3,
        frequency=0.004,
        spacing=1,
        separation=0,
        type='minecraft:random_spread',
    ),
)

NETHER_COMPLEXES = StructureSet(
    structures=[
        StructureSetElement(structure='minecraft:fortress', weight=2),
        StructureSetElement(structure='minecraft:bastion_remnant', weight=3),
    ],
    placement=StructurePlacementRandomSpread(salt=30084232, spacing=27, separation=4, type='minecraft:random_spread'),
)

NETHER_FOSSILS = StructureSet(
    structures=[StructureSetElement(structure='minecraft:nether_fossil', weight=1)],
    placement=StructurePlacementRandomSpread(salt=14357921, spacing=2, separation=1, type='minecraft:random_spread'),
)

OCEAN_MONUMENTS = StructureSet(
    structures=[StructureSetElement(structure='minecraft:monument', weight=1)],
    placement=StructurePlacementRandomSpread(
        salt=10387313,
        spacing=32,
        separation=5,
        spread_type=SpreadType.TRIANGULAR,
        type='minecraft:random_spread',
    ),
)

OCEAN_RUINS = StructureSet(
    structures=[
        StructureSetElement(structure='minecraft:ocean_ruin_cold', weight=1),
        StructureSetElement(structure='minecraft:ocean_ruin_warm', weight=1),
    ],
    placement=StructurePlacementRandomSpread(salt=14357621, spacing=20, separation=8, type='minecraft:random_spread'),
)

PILLAGER_OUTPOSTS = StructureSet(
    structures=[StructureSetElement(structure='minecraft:pillager_outpost', weight=1)],
    placement=StructurePlacementRandomSpread(
        salt=165745296,
        frequency_reduction_method=FrequencyReductionMethod.LEGACYTYPE1,
        frequency=0.2,
        exclusion_zone=ExclusionZone(other_set='minecraft:villages', chunk_count=10),
        spacing=32,
        separation=8,
        type='minecraft:random_spread',
    ),
)

RUINED_PORTALS = StructureSet(
    structures=[
        StructureSetElement(structure='minecraft:ruined_portal', weight=1),
        StructureSetElement(structure='minecraft:ruined_portal_desert', weight=1),
        StructureSetElement(structure='minecraft:ruined_portal_jungle', weight=1),
        StructureSetElement(structure='minecraft:ruined_portal_swamp', weight=1),
        StructureSetElement(structure='minecraft:ruined_portal_mountain', weight=1),
        StructureSetElement(structure='minecraft:ruined_portal_ocean', weight=1),
        StructureSetElement(structure='minecraft:ruined_portal_nether', weight=1),
    ],
    placement=StructurePlacementRandomSpread(salt=34222645, spacing=40, separation=15, type='minecraft:random_spread'),
)

SHIPWRECKS = StructureSet(
    structures=[
        StructureSetElement(structure='minecraft:shipwreck', weight=1),
        StructureSetElement(structure='minecraft:shipwreck_beached', weight=1),
    ],
    placement=StructurePlacementRandomSpread(salt=165745295, spacing=24, separation=4, type='minecraft:random_spread'),
)

STRONGHOLDS = StructureSet(
    structures=[StructureSetElement(structure='minecraft:stronghold', weight=1)],
    placement=StructurePlacementConcentricRings(
        salt=0,
        distance=32,
        spread=3,
        count=128,
        preferred_biomes='#minecraft:stronghold_biased_to',
        type='minecraft:concentric_rings',
    ),
)

SWAMP_HUTS = StructureSet(
    structures=[StructureSetElement(structure='minecraft:swamp_hut', weight=1)],
    placement=StructurePlacementRandomSpread(salt=14357620, spacing=32, separation=8, type='minecraft:random_spread'),
)

TRAIL_RUINS = StructureSet(
    structures=[StructureSetElement(structure='minecraft:trail_ruins', weight=1)],
    placement=StructurePlacementRandomSpread(salt=83469867, spacing=34, separation=8, type='minecraft:random_spread'),
)

TRIAL_CHAMBERS = StructureSet(
    structures=[StructureSetElement(structure='minecraft:trial_chambers', weight=1)],
    placement=StructurePlacementRandomSpread(salt=94251327, spacing=34, separation=12, type='minecraft:random_spread'),
)

VILLAGES = StructureSet(
    structures=[
        StructureSetElement(structure='minecraft:village_plains', weight=1),
        StructureSetElement(structure='minecraft:village_desert', weight=1),
        StructureSetElement(structure='minecraft:village_savanna', weight=1),
        StructureSetElement(structure='minecraft:village_snowy', weight=1),
        StructureSetElement(structure='minecraft:village_taiga', weight=1),
    ],
    placement=StructurePlacementRandomSpread(salt=10387312, spacing=34, separation=8, type='minecraft:random_spread'),
)

WOODLAND_MANSIONS = StructureSet(
    structures=[StructureSetElement(structure='minecraft:mansion', weight=1)],
    placement=StructurePlacementRandomSpread(
        salt=10387319,
        spacing=80,
        separation=20,
        spread_type=SpreadType.TRIANGULAR,
        type='minecraft:random_spread',
    ),
)
