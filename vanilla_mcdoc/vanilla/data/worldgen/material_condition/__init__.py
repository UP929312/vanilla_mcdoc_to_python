"""Vanilla's data/worldgen/material_condition/ files"""
from vanilla_mcdoc.data.worldgen.CaveSurface import CaveSurface
from vanilla_mcdoc.data.worldgen.material_condition.MaterialCondition import MaterialConditionStoneDepth, MaterialConditionWater

DEEP_UNDER_FLOOR = MaterialConditionStoneDepth(
    offset=0,
    surface_type=CaveSurface.FLOOR,
    add_surface_depth=True,
    secondary_depth_range=6,
    type='minecraft:stone_depth',
)

NOT_UNDERWATER = MaterialConditionWater(offset=-1, surface_depth_multiplier=0, add_stone_depth=False, type='minecraft:water')

NOT_UNDER_DEEP_WATER = MaterialConditionWater(offset=-6, surface_depth_multiplier=-1, add_stone_depth=True, type='minecraft:water')

ON_CEILING = MaterialConditionStoneDepth(
    offset=0,
    surface_type=CaveSurface.CEILING,
    add_surface_depth=False,
    secondary_depth_range=0,
    type='minecraft:stone_depth',
)

ON_FLOOR = MaterialConditionStoneDepth(
    offset=0,
    surface_type=CaveSurface.FLOOR,
    add_surface_depth=False,
    secondary_depth_range=0,
    type='minecraft:stone_depth',
)

UNDER_CEILING = MaterialConditionStoneDepth(
    offset=0,
    surface_type=CaveSurface.CEILING,
    add_surface_depth=True,
    secondary_depth_range=0,
    type='minecraft:stone_depth',
)

UNDER_FLOOR = MaterialConditionStoneDepth(
    offset=0,
    surface_type=CaveSurface.FLOOR,
    add_surface_depth=True,
    secondary_depth_range=0,
    type='minecraft:stone_depth',
)

VERY_DEEP_UNDER_FLOOR = MaterialConditionStoneDepth(
    offset=0,
    surface_type=CaveSurface.FLOOR,
    add_surface_depth=True,
    secondary_depth_range=30,
    type='minecraft:stone_depth',
)
