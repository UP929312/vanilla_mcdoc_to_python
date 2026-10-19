"""Vanilla's data/worldgen/carver/ files"""
from typing import Any
from vanilla_mcdoc.data.worldgen.FloatProvider import FloatProvider
from vanilla_mcdoc.data.worldgen.HeightProvider import HeightProviderStructUniform
from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
from vanilla_mcdoc.data.worldgen.VerticalAnchor import VerticalAnchorStruct1, VerticalAnchorStruct2, VerticalAnchorStruct3
from vanilla_mcdoc.data.worldgen.carver.CanyonShape import CanyonShape
from vanilla_mcdoc.data.worldgen.carver.ConfiguredCarver import ConfiguredCarverCanyon, ConfiguredCarverCave

CANYON = ConfiguredCarverCanyon(
    probability=0.01,
    y=HeightProviderStructUniform(
        min_inclusive=VerticalAnchorStruct1(absolute=10),
        max_inclusive=VerticalAnchorStruct1(absolute=67),
        type='minecraft:uniform',
    ),
    vertical_rotation=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 0.125, 'min_inclusive': -0.125})),
    shape=CanyonShape(
        distance_factor=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 1.0, 'min_inclusive': 0.75})),
        thickness=FloatProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6.0, 'min': 0.0, 'plateau': 2.0})),
        width_smoothness=3,
        horizontal_radius_factor=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 1.0, 'min_inclusive': 0.75})),
        vertical_radius_default_factor=1.0,
        vertical_radius_center_factor=0.0,
        y_scale=3.0,
    ),
    type='minecraft:canyon',
)

CAVE = ConfiguredCarverCave(
    probability=0.15,
    y=HeightProviderStructUniform(
        min_inclusive=VerticalAnchorStruct2(above_bottom=8),
        max_inclusive=VerticalAnchorStruct1(absolute=180),
        type='minecraft:uniform',
    ),
    count=IntProvider(type='minecraft:very_biased_to_bottom', **dict[str, Any]({'max_inclusive': 14, 'min_inclusive': 0})),
    thickness=FloatProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3.0, 'min': 0.0, 'plateau': 1.0})),
    weird_thickness_bias=True,
    room_vertical_radius_multiplier=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 0.9, 'min_inclusive': 0.1})),
    horizontal_radius_multiplier=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 1.4, 'min_inclusive': 0.7})),
    vertical_radius_multiplier=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 1.3, 'min_inclusive': 0.8})),
    floor_level=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': -0.4, 'min_inclusive': -1.0})),
    type='minecraft:cave',
)

CAVE_EXTRA_UNDERGROUND = ConfiguredCarverCave(
    probability=0.07,
    y=HeightProviderStructUniform(
        min_inclusive=VerticalAnchorStruct2(above_bottom=8),
        max_inclusive=VerticalAnchorStruct1(absolute=47),
        type='minecraft:uniform',
    ),
    count=IntProvider(type='minecraft:very_biased_to_bottom', **dict[str, Any]({'max_inclusive': 14, 'min_inclusive': 0})),
    thickness=FloatProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3.0, 'min': 0.0, 'plateau': 1.0})),
    weird_thickness_bias=True,
    room_vertical_radius_multiplier=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 0.9, 'min_inclusive': 0.1})),
    horizontal_radius_multiplier=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 1.4, 'min_inclusive': 0.7})),
    vertical_radius_multiplier=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 1.3, 'min_inclusive': 0.8})),
    floor_level=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': -0.4, 'min_inclusive': -1.0})),
    type='minecraft:cave',
)

NETHER_CAVE = ConfiguredCarverCave(
    probability=0.2,
    y=HeightProviderStructUniform(
        min_inclusive=VerticalAnchorStruct1(absolute=0),
        max_inclusive=VerticalAnchorStruct3(below_top=1),
        type='minecraft:uniform',
    ),
    count=IntProvider(type='minecraft:very_biased_to_bottom', **dict[str, Any]({'max_inclusive': 9, 'min_inclusive': 0})),
    thickness=FloatProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6.0, 'min': 0.0, 'plateau': 2.0})),
    room_vertical_radius_multiplier=0.5,
    horizontal_radius_multiplier=1.0,
    vertical_radius_multiplier=1.0,
    start_vertical_radius_multiplier=5.0,
    floor_level=-0.7,
    type='minecraft:cave',
)
