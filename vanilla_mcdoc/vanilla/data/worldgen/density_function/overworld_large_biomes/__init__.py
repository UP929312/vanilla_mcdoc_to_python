"""Vanilla's data/worldgen/density_function/overworld_large_biomes/ files"""
from vanilla_mcdoc.data.worldgen.density_function.CubicSpline import CubicSplineStruct
from vanilla_mcdoc.data.worldgen.density_function.DensityFunction import DensityFunctionStructAdd, DensityFunctionStructBeardifier, DensityFunctionStructBlendAlpha, DensityFunctionStructBlendDensity, DensityFunctionStructBlendOffset, DensityFunctionStructCache, DensityFunctionStructClamp, DensityFunctionStructDiv, DensityFunctionStructFindTopSurface, DensityFunctionStructGradient, DensityFunctionStructHalfNegative, DensityFunctionStructInterpolated, DensityFunctionStructLerp, DensityFunctionStructMax, DensityFunctionStructMin, DensityFunctionStructMul, DensityFunctionStructNoise, DensityFunctionStructQuarterNegative, DensityFunctionStructRangeChoice, DensityFunctionStructSpline, DensityFunctionStructSquare, DensityFunctionStructSqueeze, DensityFunctionStructSub
from vanilla_mcdoc.data.worldgen.density_function.SplinePoint import SplinePoint
from vanilla_mcdoc.util.direction.Axis import Axis

CHUNK_SURFACE_LEVEL = DensityFunctionStructInterpolated(
    input='minecraft:overworld_large_biomes/preliminary_surface_level',
    cell_size_xz=16,
    cell_size_y=1,
    type='minecraft:interpolated',
)

CONTINENTS = DensityFunctionStructCache(
    input=DensityFunctionStructNoise(
        noise='minecraft:continentalness_large',
        xz_scale=0.25,
        y_scale=0.0,
        shift_x='minecraft:shift_x',
        shift_z='minecraft:shift_z',
        type='minecraft:noise',
    ),
    type='minecraft:cache',
)

DEPTH = DensityFunctionStructAdd(
    left=DensityFunctionStructGradient(
        axis=Axis.Y,
        from_coordinate=-64,
        to_coordinate=320,
        from_value=1.5,
        to_value=-1.5,
        type='minecraft:gradient',
    ),
    right='minecraft:overworld_large_biomes/offset',
    type='minecraft:add',
)

EROSION = DensityFunctionStructCache(
    input=DensityFunctionStructNoise(
        noise='minecraft:erosion_large',
        xz_scale=0.25,
        y_scale=0.0,
        shift_x='minecraft:shift_x',
        shift_z='minecraft:shift_z',
        type='minecraft:noise',
    ),
    type='minecraft:cache',
)

FACTOR = DensityFunctionStructCache(
    input=DensityFunctionStructLerp(
        alpha=DensityFunctionStructBlendAlpha(type='minecraft:blend_alpha'),
        first=10.0,
        second=DensityFunctionStructSpline(
            spline=CubicSplineStruct(
                coordinate='minecraft:overworld_large_biomes/continents',
                points=[
                    SplinePoint(location=-0.19, derivative=0.0, value=3.95),
                    SplinePoint(
                        location=-0.15,
                        derivative=0.0,
                        value=CubicSplineStruct(
                            coordinate='minecraft:overworld_large_biomes/erosion',
                            points=[
                                SplinePoint(
                                    location=-0.6,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=6.25),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.5,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.05, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.05, derivative=0.0, value=2.67),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.35,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=6.25),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.25,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=6.25),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.1,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.05, derivative=0.0, value=2.67),
                                            SplinePoint(location=0.05, derivative=0.0, value=6.3),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=0.03,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=6.25),
                                        ],
                                    ),
                                ),
                                SplinePoint(location=0.35, derivative=0.0, value=6.25),
                                SplinePoint(
                                    location=0.45,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(location=-0.9, derivative=0.0, value=6.25),
                                            SplinePoint(
                                                location=-0.69,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=0.0, derivative=0.0, value=6.25),
                                                        SplinePoint(location=0.1, derivative=0.0, value=0.625),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=0.55,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(location=-0.9, derivative=0.0, value=6.25),
                                            SplinePoint(
                                                location=-0.69,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=0.0, derivative=0.0, value=6.25),
                                                        SplinePoint(location=0.1, derivative=0.0, value=0.625),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                SplinePoint(location=0.62, derivative=0.0, value=6.25),
                            ],
                        ),
                    ),
                    SplinePoint(
                        location=-0.1,
                        derivative=0.0,
                        value=CubicSplineStruct(
                            coordinate='minecraft:overworld_large_biomes/erosion',
                            points=[
                                SplinePoint(
                                    location=-0.6,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=5.47),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.5,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.05, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.05, derivative=0.0, value=2.67),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.35,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=5.47),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.25,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=5.47),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.1,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.05, derivative=0.0, value=2.67),
                                            SplinePoint(location=0.05, derivative=0.0, value=6.3),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=0.03,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=5.47),
                                        ],
                                    ),
                                ),
                                SplinePoint(location=0.35, derivative=0.0, value=5.47),
                                SplinePoint(
                                    location=0.45,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(location=-0.9, derivative=0.0, value=5.47),
                                            SplinePoint(
                                                location=-0.69,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=0.0, derivative=0.0, value=5.47),
                                                        SplinePoint(location=0.1, derivative=0.0, value=0.625),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=0.55,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(location=-0.9, derivative=0.0, value=5.47),
                                            SplinePoint(
                                                location=-0.69,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=0.0, derivative=0.0, value=5.47),
                                                        SplinePoint(location=0.1, derivative=0.0, value=0.625),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                SplinePoint(location=0.62, derivative=0.0, value=5.47),
                            ],
                        ),
                    ),
                    SplinePoint(
                        location=0.03,
                        derivative=0.0,
                        value=CubicSplineStruct(
                            coordinate='minecraft:overworld_large_biomes/erosion',
                            points=[
                                SplinePoint(
                                    location=-0.6,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=5.08),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.5,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.05, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.05, derivative=0.0, value=2.67),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.35,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=5.08),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.25,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=5.08),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.1,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.05, derivative=0.0, value=2.67),
                                            SplinePoint(location=0.05, derivative=0.0, value=6.3),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=0.03,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=5.08),
                                        ],
                                    ),
                                ),
                                SplinePoint(location=0.35, derivative=0.0, value=5.08),
                                SplinePoint(
                                    location=0.45,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(location=-0.9, derivative=0.0, value=5.08),
                                            SplinePoint(
                                                location=-0.69,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=0.0, derivative=0.0, value=5.08),
                                                        SplinePoint(location=0.1, derivative=0.0, value=0.625),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=0.55,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(location=-0.9, derivative=0.0, value=5.08),
                                            SplinePoint(
                                                location=-0.69,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=0.0, derivative=0.0, value=5.08),
                                                        SplinePoint(location=0.1, derivative=0.0, value=0.625),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                SplinePoint(location=0.62, derivative=0.0, value=5.08),
                            ],
                        ),
                    ),
                    SplinePoint(
                        location=0.06,
                        derivative=0.0,
                        value=CubicSplineStruct(
                            coordinate='minecraft:overworld_large_biomes/erosion',
                            points=[
                                SplinePoint(
                                    location=-0.6,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=4.69),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.5,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.05, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.05, derivative=0.0, value=2.67),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.35,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=4.69),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.25,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=4.69),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.1,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.05, derivative=0.0, value=2.67),
                                            SplinePoint(location=0.05, derivative=0.0, value=6.3),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=0.03,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                            SplinePoint(location=0.2, derivative=0.0, value=4.69),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=0.05,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(
                                                location=0.45,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                                        SplinePoint(location=0.2, derivative=0.0, value=4.69),
                                                    ],
                                                ),
                                            ),
                                            SplinePoint(location=0.7, derivative=0.0, value=1.56),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=0.4,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(
                                                location=0.45,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                                        SplinePoint(location=0.2, derivative=0.0, value=4.69),
                                                    ],
                                                ),
                                            ),
                                            SplinePoint(location=0.7, derivative=0.0, value=1.56),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=0.45,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(
                                                location=-0.7,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                                        SplinePoint(location=0.2, derivative=0.0, value=4.69),
                                                    ],
                                                ),
                                            ),
                                            SplinePoint(location=-0.15, derivative=0.0, value=1.37),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=0.55,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(
                                                location=-0.7,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=-0.2, derivative=0.0, value=6.3),
                                                        SplinePoint(location=0.2, derivative=0.0, value=4.69),
                                                    ],
                                                ),
                                            ),
                                            SplinePoint(location=-0.15, derivative=0.0, value=1.37),
                                        ],
                                    ),
                                ),
                                SplinePoint(location=0.58, derivative=0.0, value=4.69),
                            ],
                        ),
                    ),
                ],
            ),
            type='minecraft:spline',
        ),
        type='minecraft:lerp',
    ),
    type='minecraft:cache',
)

FINAL_DENSITY = DensityFunctionStructAdd(
    left=DensityFunctionStructMin(
        left=DensityFunctionStructSqueeze(
            input=DensityFunctionStructInterpolated(
                input=DensityFunctionStructMul(
                    left=DensityFunctionStructBlendDensity(
                        input=DensityFunctionStructLerp(
                            alpha=DensityFunctionStructGradient(
                                axis=Axis.Y,
                                from_coordinate=-64,
                                to_coordinate=-40,
                                from_value=0.0,
                                to_value=1.0,
                                type='minecraft:gradient',
                            ),
                            first=0.1171875,
                            second=DensityFunctionStructLerp(
                                alpha=DensityFunctionStructGradient(
                                    axis=Axis.Y,
                                    from_coordinate=240,
                                    to_coordinate=256,
                                    from_value=1.0,
                                    to_value=0.0,
                                    type='minecraft:gradient',
                                ),
                                first=-0.078125,
                                second=DensityFunctionStructRangeChoice(
                                    input='minecraft:overworld_large_biomes/sloped_cheese',
                                    min_inclusive=-1000000.0,
                                    max_exclusive=1.5625,
                                    when_in_range=DensityFunctionStructMin(
                                        left='minecraft:overworld_large_biomes/sloped_cheese',
                                        right=DensityFunctionStructMul(
                                            left='minecraft:overworld/caves/entrances',
                                            right=5.0,
                                            type='minecraft:mul',
                                        ),
                                        type='minecraft:min',
                                    ),
                                    when_out_of_range=DensityFunctionStructMax(
                                        left=DensityFunctionStructMin(
                                            left=DensityFunctionStructMin(
                                                left=DensityFunctionStructAdd(
                                                    left=DensityFunctionStructMul(
                                                        left=DensityFunctionStructSquare(
                                                            input=DensityFunctionStructNoise(
                                                                noise='minecraft:cave_layer',
                                                                xz_scale=1.0,
                                                                y_scale=8.0,
                                                                type='minecraft:noise',
                                                            ),
                                                            type='minecraft:square',
                                                        ),
                                                        right=4.0,
                                                        type='minecraft:mul',
                                                    ),
                                                    right=DensityFunctionStructAdd(
                                                        left=DensityFunctionStructClamp(
                                                            input=DensityFunctionStructAdd(
                                                                left=DensityFunctionStructNoise(
                                                                    noise='minecraft:cave_cheese',
                                                                    xz_scale=1.0,
                                                                    y_scale=0.6666666666666666,
                                                                    type='minecraft:noise',
                                                                ),
                                                                right=0.27,
                                                                type='minecraft:add',
                                                            ),
                                                            min=-1.0,
                                                            max=1.0,
                                                            type='minecraft:clamp',
                                                        ),
                                                        right=DensityFunctionStructClamp(
                                                            input=DensityFunctionStructAdd(
                                                                left=DensityFunctionStructMul(
                                                                    left='minecraft:overworld_large_biomes/sloped_cheese',
                                                                    right=-0.64,
                                                                    type='minecraft:mul',
                                                                ),
                                                                right=1.5,
                                                                type='minecraft:add',
                                                            ),
                                                            min=0.0,
                                                            max=0.5,
                                                            type='minecraft:clamp',
                                                        ),
                                                        type='minecraft:add',
                                                    ),
                                                    type='minecraft:add',
                                                ),
                                                right='minecraft:overworld/caves/entrances',
                                                type='minecraft:min',
                                            ),
                                            right=DensityFunctionStructAdd(
                                                left='minecraft:overworld/caves/spaghetti_2d',
                                                right='minecraft:overworld/caves/spaghetti_roughness_function',
                                                type='minecraft:add',
                                            ),
                                            type='minecraft:min',
                                        ),
                                        right=DensityFunctionStructRangeChoice(
                                            input='minecraft:overworld/caves/pillars',
                                            min_inclusive=-1000000.0,
                                            max_exclusive=0.03,
                                            when_in_range=-1000000.0,
                                            when_out_of_range='minecraft:overworld/caves/pillars',
                                            type='minecraft:range_choice',
                                        ),
                                        type='minecraft:max',
                                    ),
                                    type='minecraft:range_choice',
                                ),
                                type='minecraft:lerp',
                            ),
                            type='minecraft:lerp',
                        ),
                        type='minecraft:blend_density',
                    ),
                    right=0.64,
                    type='minecraft:mul',
                ),
                cell_size_xz=4,
                cell_size_y=8,
                type='minecraft:interpolated',
            ),
            type='minecraft:squeeze',
        ),
        right='minecraft:overworld/caves/noodle',
        type='minecraft:min',
    ),
    right=DensityFunctionStructBeardifier(type='minecraft:beardifier'),
    type='minecraft:add',
)

JAGGEDNESS = DensityFunctionStructCache(
    input=DensityFunctionStructLerp(
        alpha=DensityFunctionStructBlendAlpha(type='minecraft:blend_alpha'),
        first=0.0,
        second=DensityFunctionStructSpline(
            spline=CubicSplineStruct(
                coordinate='minecraft:overworld_large_biomes/continents',
                points=[
                    SplinePoint(location=-0.11, derivative=0.0, value=0.0),
                    SplinePoint(
                        location=0.03,
                        derivative=0.0,
                        value=CubicSplineStruct(
                            coordinate='minecraft:overworld_large_biomes/erosion',
                            points=[
                                SplinePoint(
                                    location=-1.0,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(location=0.19999999, derivative=0.0, value=0.0),
                                            SplinePoint(location=0.44999996, derivative=0.0, value=0.0),
                                            SplinePoint(
                                                location=1.0,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=-0.01, derivative=0.0, value=0.63),
                                                        SplinePoint(location=0.01, derivative=0.0, value=0.3),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.78,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(location=0.19999999, derivative=0.0, value=0.0),
                                            SplinePoint(location=0.44999996, derivative=0.0, value=0.0),
                                            SplinePoint(
                                                location=1.0,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=-0.01, derivative=0.0, value=0.315),
                                                        SplinePoint(location=0.01, derivative=0.0, value=0.15),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.5775,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(location=0.19999999, derivative=0.0, value=0.0),
                                            SplinePoint(location=0.44999996, derivative=0.0, value=0.0),
                                            SplinePoint(
                                                location=1.0,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=-0.01, derivative=0.0, value=0.315),
                                                        SplinePoint(location=0.01, derivative=0.0, value=0.15),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                SplinePoint(location=-0.375, derivative=0.0, value=0.0),
                            ],
                        ),
                    ),
                    SplinePoint(
                        location=0.65,
                        derivative=0.0,
                        value=CubicSplineStruct(
                            coordinate='minecraft:overworld_large_biomes/erosion',
                            points=[
                                SplinePoint(
                                    location=-1.0,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(location=0.19999999, derivative=0.0, value=0.0),
                                            SplinePoint(
                                                location=0.44999996,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=-0.01, derivative=0.0, value=0.63),
                                                        SplinePoint(location=0.01, derivative=0.0, value=0.3),
                                                    ],
                                                ),
                                            ),
                                            SplinePoint(
                                                location=1.0,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=-0.01, derivative=0.0, value=0.63),
                                                        SplinePoint(location=0.01, derivative=0.0, value=0.3),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.78,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(location=0.19999999, derivative=0.0, value=0.0),
                                            SplinePoint(location=0.44999996, derivative=0.0, value=0.0),
                                            SplinePoint(
                                                location=1.0,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=-0.01, derivative=0.0, value=0.63),
                                                        SplinePoint(location=0.01, derivative=0.0, value=0.3),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.5775,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(location=0.19999999, derivative=0.0, value=0.0),
                                            SplinePoint(location=0.44999996, derivative=0.0, value=0.0),
                                            SplinePoint(
                                                location=1.0,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=-0.01, derivative=0.0, value=0.63),
                                                        SplinePoint(location=0.01, derivative=0.0, value=0.3),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                SplinePoint(location=-0.375, derivative=0.0, value=0.0),
                            ],
                        ),
                    ),
                ],
            ),
            type='minecraft:spline',
        ),
        type='minecraft:lerp',
    ),
    type='minecraft:cache',
)

OFFSET = DensityFunctionStructCache(
    input=DensityFunctionStructLerp(
        alpha=DensityFunctionStructBlendAlpha(type='minecraft:blend_alpha'),
        first=DensityFunctionStructBlendOffset(type='minecraft:blend_offset'),
        second=DensityFunctionStructAdd(
            left=-0.50375,
            right=DensityFunctionStructSpline(
                spline=CubicSplineStruct(
                    coordinate='minecraft:overworld_large_biomes/continents',
                    points=[
                        SplinePoint(location=-1.1, derivative=0.0, value=0.044),
                        SplinePoint(location=-1.02, derivative=0.0, value=-0.2222),
                        SplinePoint(location=-0.51, derivative=0.0, value=-0.2222),
                        SplinePoint(location=-0.44, derivative=0.0, value=-0.12),
                        SplinePoint(location=-0.18, derivative=0.0, value=-0.12),
                        SplinePoint(
                            location=-0.16,
                            derivative=0.0,
                            value=CubicSplineStruct(
                                coordinate='minecraft:overworld_large_biomes/erosion',
                                points=[
                                    SplinePoint(
                                        location=-0.85,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.38940096, value=-0.08880186),
                                                SplinePoint(location=1.0, derivative=0.38940096, value=0.69000006),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.7,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.37788022, value=-0.115760356),
                                                SplinePoint(location=1.0, derivative=0.37788022, value=0.6400001),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.4,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=-0.2222),
                                                SplinePoint(location=-0.75, derivative=0.0, value=-0.2222),
                                                SplinePoint(location=-0.65, derivative=0.0, value=0.0),
                                                SplinePoint(location=0.5954547, derivative=0.0, value=2.9802322e-08),
                                                SplinePoint(
                                                    location=0.6054547,
                                                    derivative=0.2534563,
                                                    value=2.9802322e-08,
                                                ),
                                                SplinePoint(location=1.0, derivative=0.2534563, value=0.100000024),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.35,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.3),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.05),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.05),
                                                SplinePoint(location=0.4, derivative=0.0, value=0.05),
                                                SplinePoint(location=1.0, derivative=0.007000001, value=0.060000002),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.1,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.15),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.0),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.0),
                                                SplinePoint(location=0.4, derivative=0.1, value=0.05),
                                                SplinePoint(location=1.0, derivative=0.007000001, value=0.060000002),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.2,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.15),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.0),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.0),
                                                SplinePoint(location=0.4, derivative=0.0, value=0.0),
                                                SplinePoint(location=1.0, derivative=0.0, value=0.0),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.7,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=-0.02),
                                                SplinePoint(location=-0.4, derivative=0.0, value=-0.03),
                                                SplinePoint(location=0.0, derivative=0.0, value=-0.03),
                                                SplinePoint(location=0.4, derivative=0.06, value=0.0),
                                                SplinePoint(location=1.0, derivative=0.0, value=0.0),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        SplinePoint(
                            location=-0.15,
                            derivative=0.0,
                            value=CubicSplineStruct(
                                coordinate='minecraft:overworld_large_biomes/erosion',
                                points=[
                                    SplinePoint(
                                        location=-0.85,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.38940096, value=-0.08880186),
                                                SplinePoint(location=1.0, derivative=0.38940096, value=0.69000006),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.7,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.37788022, value=-0.115760356),
                                                SplinePoint(location=1.0, derivative=0.37788022, value=0.6400001),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.4,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=-0.2222),
                                                SplinePoint(location=-0.75, derivative=0.0, value=-0.2222),
                                                SplinePoint(location=-0.65, derivative=0.0, value=0.0),
                                                SplinePoint(location=0.5954547, derivative=0.0, value=2.9802322e-08),
                                                SplinePoint(
                                                    location=0.6054547,
                                                    derivative=0.2534563,
                                                    value=2.9802322e-08,
                                                ),
                                                SplinePoint(location=1.0, derivative=0.2534563, value=0.100000024),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.35,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.3),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.05),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.05),
                                                SplinePoint(location=0.4, derivative=0.0, value=0.05),
                                                SplinePoint(location=1.0, derivative=0.007000001, value=0.060000002),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.1,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.15),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.0),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.0),
                                                SplinePoint(location=0.4, derivative=0.1, value=0.05),
                                                SplinePoint(location=1.0, derivative=0.007000001, value=0.060000002),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.2,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.15),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.0),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.0),
                                                SplinePoint(location=0.4, derivative=0.0, value=0.0),
                                                SplinePoint(location=1.0, derivative=0.0, value=0.0),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.7,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=-0.02),
                                                SplinePoint(location=-0.4, derivative=0.0, value=-0.03),
                                                SplinePoint(location=0.0, derivative=0.0, value=-0.03),
                                                SplinePoint(location=0.4, derivative=0.06, value=0.0),
                                                SplinePoint(location=1.0, derivative=0.0, value=0.0),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        SplinePoint(
                            location=-0.1,
                            derivative=0.0,
                            value=CubicSplineStruct(
                                coordinate='minecraft:overworld_large_biomes/erosion',
                                points=[
                                    SplinePoint(
                                        location=-0.85,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.38940096, value=-0.08880186),
                                                SplinePoint(location=1.0, derivative=0.38940096, value=0.69000006),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.7,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.37788022, value=-0.115760356),
                                                SplinePoint(location=1.0, derivative=0.37788022, value=0.6400001),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.4,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=-0.2222),
                                                SplinePoint(location=-0.75, derivative=0.0, value=-0.2222),
                                                SplinePoint(location=-0.65, derivative=0.0, value=0.0),
                                                SplinePoint(location=0.5954547, derivative=0.0, value=2.9802322e-08),
                                                SplinePoint(
                                                    location=0.6054547,
                                                    derivative=0.2534563,
                                                    value=2.9802322e-08,
                                                ),
                                                SplinePoint(location=1.0, derivative=0.2534563, value=0.100000024),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.35,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.25),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.05),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.05),
                                                SplinePoint(location=0.4, derivative=0.0, value=0.05),
                                                SplinePoint(location=1.0, derivative=0.007000001, value=0.060000002),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.1,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.1),
                                                SplinePoint(location=-0.4, derivative=0.01, value=0.001),
                                                SplinePoint(location=0.0, derivative=0.01, value=0.003),
                                                SplinePoint(location=0.4, derivative=0.094000004, value=0.05),
                                                SplinePoint(location=1.0, derivative=0.007000001, value=0.060000002),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.2,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.1),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.03),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.1),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.7,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=-0.02),
                                                SplinePoint(location=-0.4, derivative=0.0, value=-0.03),
                                                SplinePoint(location=0.0, derivative=0.0, value=-0.03),
                                                SplinePoint(location=0.4, derivative=0.12, value=0.03),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.1),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        SplinePoint(
                            location=0.25,
                            derivative=0.0,
                            value=CubicSplineStruct(
                                coordinate='minecraft:overworld_large_biomes/erosion',
                                points=[
                                    SplinePoint(
                                        location=-0.85,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=0.20235021),
                                                SplinePoint(location=0.0, derivative=0.5138249, value=0.7161751),
                                                SplinePoint(location=1.0, derivative=0.5138249, value=1.23),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.7,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=0.2),
                                                SplinePoint(location=0.0, derivative=0.43317974, value=0.44682026),
                                                SplinePoint(location=1.0, derivative=0.43317974, value=0.88),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.4,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=0.2),
                                                SplinePoint(location=0.0, derivative=0.3917051, value=0.30829495),
                                                SplinePoint(location=1.0, derivative=0.3917051, value=0.70000005),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.35,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.25),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.35),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.35),
                                                SplinePoint(location=0.4, derivative=0.0, value=0.35),
                                                SplinePoint(location=1.0, derivative=0.049000014, value=0.42000002),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.1,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.1),
                                                SplinePoint(location=-0.4, derivative=0.07, value=0.0069999998),
                                                SplinePoint(location=0.0, derivative=0.07, value=0.021),
                                                SplinePoint(location=0.4, derivative=0.658, value=0.35),
                                                SplinePoint(location=1.0, derivative=0.049000014, value=0.42000002),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.2,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.1),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.03),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.1),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.4,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.1),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.03),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.1),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.45,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=-0.1),
                                                SplinePoint(
                                                    location=-0.4,
                                                    derivative=0.0,
                                                    value=CubicSplineStruct(
                                                        coordinate='minecraft:overworld/ridges_folded',
                                                        points=[
                                                            SplinePoint(location=-1.0, derivative=0.5, value=-0.1),
                                                            SplinePoint(location=-0.4, derivative=0.0, value=0.01),
                                                            SplinePoint(location=0.0, derivative=0.0, value=0.01),
                                                            SplinePoint(location=0.4, derivative=0.04, value=0.03),
                                                            SplinePoint(location=1.0, derivative=0.049, value=0.1),
                                                        ],
                                                    ),
                                                ),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.17),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.55,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=-0.1),
                                                SplinePoint(
                                                    location=-0.4,
                                                    derivative=0.0,
                                                    value=CubicSplineStruct(
                                                        coordinate='minecraft:overworld/ridges_folded',
                                                        points=[
                                                            SplinePoint(location=-1.0, derivative=0.5, value=-0.1),
                                                            SplinePoint(location=-0.4, derivative=0.0, value=0.01),
                                                            SplinePoint(location=0.0, derivative=0.0, value=0.01),
                                                            SplinePoint(location=0.4, derivative=0.04, value=0.03),
                                                            SplinePoint(location=1.0, derivative=0.049, value=0.1),
                                                        ],
                                                    ),
                                                ),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.17),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.58,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.1),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.03),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.1),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.7,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=-0.02),
                                                SplinePoint(location=-0.4, derivative=0.0, value=-0.03),
                                                SplinePoint(location=0.0, derivative=0.0, value=-0.03),
                                                SplinePoint(location=0.4, derivative=0.12, value=0.03),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.1),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        SplinePoint(
                            location=1.0,
                            derivative=0.0,
                            value=CubicSplineStruct(
                                coordinate='minecraft:overworld_large_biomes/erosion',
                                points=[
                                    SplinePoint(
                                        location=-0.85,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=0.34792626),
                                                SplinePoint(location=0.0, derivative=0.5760369, value=0.9239631),
                                                SplinePoint(location=1.0, derivative=0.5760369, value=1.5),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.7,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=0.2),
                                                SplinePoint(location=0.0, derivative=0.4608295, value=0.5391705),
                                                SplinePoint(location=1.0, derivative=0.4608295, value=1.0),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.4,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=0.2),
                                                SplinePoint(location=0.0, derivative=0.4608295, value=0.5391705),
                                                SplinePoint(location=1.0, derivative=0.4608295, value=1.0),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.35,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.2),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.5),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.5),
                                                SplinePoint(location=0.4, derivative=0.0, value=0.5),
                                                SplinePoint(location=1.0, derivative=0.070000015, value=0.6),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.1,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.05),
                                                SplinePoint(location=-0.4, derivative=0.099999994, value=0.01),
                                                SplinePoint(location=0.0, derivative=0.099999994, value=0.03),
                                                SplinePoint(location=0.4, derivative=0.94, value=0.5),
                                                SplinePoint(location=1.0, derivative=0.070000015, value=0.6),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.2,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.05),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.03),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.1),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.4,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.05),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.03),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.1),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.45,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=-0.05),
                                                SplinePoint(
                                                    location=-0.4,
                                                    derivative=0.0,
                                                    value=CubicSplineStruct(
                                                        coordinate='minecraft:overworld/ridges_folded',
                                                        points=[
                                                            SplinePoint(location=-1.0, derivative=0.5, value=-0.05),
                                                            SplinePoint(location=-0.4, derivative=0.0, value=0.01),
                                                            SplinePoint(location=0.0, derivative=0.0, value=0.01),
                                                            SplinePoint(location=0.4, derivative=0.04, value=0.03),
                                                            SplinePoint(location=1.0, derivative=0.049, value=0.1),
                                                        ],
                                                    ),
                                                ),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.17),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.55,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=-0.05),
                                                SplinePoint(
                                                    location=-0.4,
                                                    derivative=0.0,
                                                    value=CubicSplineStruct(
                                                        coordinate='minecraft:overworld/ridges_folded',
                                                        points=[
                                                            SplinePoint(location=-1.0, derivative=0.5, value=-0.05),
                                                            SplinePoint(location=-0.4, derivative=0.0, value=0.01),
                                                            SplinePoint(location=0.0, derivative=0.0, value=0.01),
                                                            SplinePoint(location=0.4, derivative=0.04, value=0.03),
                                                            SplinePoint(location=1.0, derivative=0.049, value=0.1),
                                                        ],
                                                    ),
                                                ),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.17),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.58,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.5, value=-0.05),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.03),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.1),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=0.7,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.015, value=-0.02),
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.01),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.03),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.1),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
                type='minecraft:spline',
            ),
            type='minecraft:add',
        ),
        type='minecraft:lerp',
    ),
    type='minecraft:cache',
)

PRELIMINARY_SURFACE_LEVEL = DensityFunctionStructFindTopSurface(
    density=DensityFunctionStructAdd(
        left=DensityFunctionStructLerp(
            alpha=DensityFunctionStructGradient(
                axis=Axis.Y,
                from_coordinate=-64,
                to_coordinate=-40,
                from_value=0.0,
                to_value=1.0,
                type='minecraft:gradient',
            ),
            first=0.1171875,
            second=DensityFunctionStructLerp(
                alpha=DensityFunctionStructGradient(
                    axis=Axis.Y,
                    from_coordinate=240,
                    to_coordinate=256,
                    from_value=1.0,
                    to_value=0.0,
                    type='minecraft:gradient',
                ),
                first=-0.078125,
                second=DensityFunctionStructClamp(
                    input=DensityFunctionStructAdd(
                        left=DensityFunctionStructMul(
                            left=DensityFunctionStructQuarterNegative(
                                input=DensityFunctionStructMul(
                                    left=DensityFunctionStructAdd(
                                        left=DensityFunctionStructGradient(
                                            axis=Axis.Y,
                                            from_coordinate=-64,
                                            to_coordinate=320,
                                            from_value=1.5,
                                            to_value=-1.5,
                                            type='minecraft:gradient',
                                        ),
                                        right='minecraft:overworld_large_biomes/offset',
                                        type='minecraft:add',
                                    ),
                                    right='minecraft:overworld_large_biomes/factor',
                                    type='minecraft:mul',
                                ),
                                type='minecraft:quarter_negative',
                            ),
                            right=4.0,
                            type='minecraft:mul',
                        ),
                        right=-0.703125,
                        type='minecraft:add',
                    ),
                    min=-64.0,
                    max=64.0,
                    type='minecraft:clamp',
                ),
                type='minecraft:lerp',
            ),
            type='minecraft:lerp',
        ),
        right=-0.390625,
        type='minecraft:add',
    ),
    upper_bound=DensityFunctionStructClamp(
        input=DensityFunctionStructAdd(
            left=DensityFunctionStructMul(
                left=DensityFunctionStructSub(
                    left=DensityFunctionStructDiv(
                        left=0.2734375,
                        right='minecraft:overworld_large_biomes/factor',
                        type='minecraft:div',
                    ),
                    right='minecraft:overworld_large_biomes/offset',
                    type='minecraft:sub',
                ),
                right=-128.0,
                type='minecraft:mul',
            ),
            right=128.0,
            type='minecraft:add',
        ),
        min=-40.0,
        max=320.0,
        type='minecraft:clamp',
    ),
    lower_bound=-64,
    cell_height=8,
    type='minecraft:find_top_surface',
)

SLOPED_CHEESE = DensityFunctionStructCache(
    input=DensityFunctionStructAdd(
        left=DensityFunctionStructMul(
            left=DensityFunctionStructQuarterNegative(
                input=DensityFunctionStructMul(
                    left=DensityFunctionStructAdd(
                        left='minecraft:overworld_large_biomes/depth',
                        right=DensityFunctionStructCache(
                            input=DensityFunctionStructMul(
                                left='minecraft:overworld_large_biomes/jaggedness',
                                right=DensityFunctionStructHalfNegative(
                                    input=DensityFunctionStructNoise(
                                        noise='minecraft:jagged',
                                        xz_scale=1500.0,
                                        y_scale=0.0,
                                        type='minecraft:noise',
                                    ),
                                    type='minecraft:half_negative',
                                ),
                                type='minecraft:mul',
                            ),
                            type='minecraft:cache',
                        ),
                        type='minecraft:add',
                    ),
                    right='minecraft:overworld_large_biomes/factor',
                    type='minecraft:mul',
                ),
                type='minecraft:quarter_negative',
            ),
            right=4.0,
            type='minecraft:mul',
        ),
        right='minecraft:overworld/base_3d_noise',
        type='minecraft:add',
    ),
    type='minecraft:cache',
)

TEMPERATURE = DensityFunctionStructNoise(
    noise='minecraft:temperature_large',
    xz_scale=0.25,
    y_scale=0.0,
    shift_x='minecraft:shift_x',
    shift_z='minecraft:shift_z',
    type='minecraft:noise',
)

VEGETATION = DensityFunctionStructNoise(
    noise='minecraft:vegetation_large',
    xz_scale=0.25,
    y_scale=0.0,
    shift_x='minecraft:shift_x',
    shift_z='minecraft:shift_z',
    type='minecraft:noise',
)
