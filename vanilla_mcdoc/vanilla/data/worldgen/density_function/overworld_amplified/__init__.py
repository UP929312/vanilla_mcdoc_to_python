"""Vanilla's data/worldgen/density_function/overworld_amplified/ files"""
from vanilla_mcdoc.data.worldgen.density_function.CubicSpline import CubicSplineStruct
from vanilla_mcdoc.data.worldgen.density_function.DensityFunction import DensityFunctionStructAdd, DensityFunctionStructBeardifier, DensityFunctionStructBlendAlpha, DensityFunctionStructBlendDensity, DensityFunctionStructBlendOffset, DensityFunctionStructCache, DensityFunctionStructClamp, DensityFunctionStructDiv, DensityFunctionStructFindTopSurface, DensityFunctionStructGradient, DensityFunctionStructHalfNegative, DensityFunctionStructInterpolated, DensityFunctionStructLerp, DensityFunctionStructMax, DensityFunctionStructMin, DensityFunctionStructMul, DensityFunctionStructNoise, DensityFunctionStructQuarterNegative, DensityFunctionStructRangeChoice, DensityFunctionStructSpline, DensityFunctionStructSquare, DensityFunctionStructSqueeze, DensityFunctionStructSub
from vanilla_mcdoc.data.worldgen.density_function.SplinePoint import SplinePoint
from vanilla_mcdoc.util.direction.Axis import Axis

CHUNK_SURFACE_LEVEL = DensityFunctionStructInterpolated(
    input='minecraft:overworld_amplified/preliminary_surface_level',
    cell_size_xz=16,
    cell_size_y=1,
    type='minecraft:interpolated',
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
    right='minecraft:overworld_amplified/offset',
    type='minecraft:add',
)

FACTOR = DensityFunctionStructCache(
    input=DensityFunctionStructLerp(
        alpha=DensityFunctionStructBlendAlpha(type='minecraft:blend_alpha'),
        first=10.0,
        second=DensityFunctionStructSpline(
            spline=CubicSplineStruct(
                coordinate='minecraft:overworld/continents',
                points=[
                    SplinePoint(location=-0.19, derivative=0.0, value=3.95),
                    SplinePoint(
                        location=-0.15,
                        derivative=0.0,
                        value=CubicSplineStruct(
                            coordinate='minecraft:overworld/erosion',
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
                            coordinate='minecraft:overworld/erosion',
                            points=[
                                SplinePoint(
                                    location=-0.6,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                            SplinePoint(location=0.2, derivative=0.0, value=0.6530563),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.5,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.05, derivative=0.0, value=0.6969027),
                                            SplinePoint(location=0.05, derivative=0.0, value=0.4351369),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.35,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                            SplinePoint(location=0.2, derivative=0.0, value=0.6530563),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.25,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                            SplinePoint(location=0.2, derivative=0.0, value=0.6530563),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.1,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.05, derivative=0.0, value=0.4351369),
                                            SplinePoint(location=0.05, derivative=0.0, value=0.6969027),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=0.03,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                            SplinePoint(location=0.2, derivative=0.0, value=0.6530563),
                                        ],
                                    ),
                                ),
                                SplinePoint(location=0.35, derivative=0.0, value=0.6530563),
                                SplinePoint(
                                    location=0.45,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(location=-0.9, derivative=0.0, value=0.6530563),
                                            SplinePoint(
                                                location=-0.69,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=0.0, derivative=0.0, value=0.6530563),
                                                        SplinePoint(location=0.1, derivative=0.0, value=0.13888884),
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
                                            SplinePoint(location=-0.9, derivative=0.0, value=0.6530563),
                                            SplinePoint(
                                                location=-0.69,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=0.0, derivative=0.0, value=0.6530563),
                                                        SplinePoint(location=0.1, derivative=0.0, value=0.13888884),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                SplinePoint(location=0.62, derivative=0.0, value=0.6530563),
                            ],
                        ),
                    ),
                    SplinePoint(
                        location=0.03,
                        derivative=0.0,
                        value=CubicSplineStruct(
                            coordinate='minecraft:overworld/erosion',
                            points=[
                                SplinePoint(
                                    location=-0.6,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                            SplinePoint(location=0.2, derivative=0.0, value=0.6299603),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.5,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.05, derivative=0.0, value=0.6969027),
                                            SplinePoint(location=0.05, derivative=0.0, value=0.4351369),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.35,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                            SplinePoint(location=0.2, derivative=0.0, value=0.6299603),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.25,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                            SplinePoint(location=0.2, derivative=0.0, value=0.6299603),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.1,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.05, derivative=0.0, value=0.4351369),
                                            SplinePoint(location=0.05, derivative=0.0, value=0.6969027),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=0.03,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                            SplinePoint(location=0.2, derivative=0.0, value=0.6299603),
                                        ],
                                    ),
                                ),
                                SplinePoint(location=0.35, derivative=0.0, value=0.6299603),
                                SplinePoint(
                                    location=0.45,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges_folded',
                                        points=[
                                            SplinePoint(location=-0.9, derivative=0.0, value=0.6299603),
                                            SplinePoint(
                                                location=-0.69,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=0.0, derivative=0.0, value=0.6299603),
                                                        SplinePoint(location=0.1, derivative=0.0, value=0.13888884),
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
                                            SplinePoint(location=-0.9, derivative=0.0, value=0.6299603),
                                            SplinePoint(
                                                location=-0.69,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=0.0, derivative=0.0, value=0.6299603),
                                                        SplinePoint(location=0.1, derivative=0.0, value=0.13888884),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                SplinePoint(location=0.62, derivative=0.0, value=0.6299603),
                            ],
                        ),
                    ),
                    SplinePoint(
                        location=0.06,
                        derivative=0.0,
                        value=CubicSplineStruct(
                            coordinate='minecraft:overworld/erosion',
                            points=[
                                SplinePoint(
                                    location=-0.6,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                            SplinePoint(location=0.2, derivative=0.0, value=0.6050052),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.5,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.05, derivative=0.0, value=0.6969027),
                                            SplinePoint(location=0.05, derivative=0.0, value=0.4351369),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.35,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                            SplinePoint(location=0.2, derivative=0.0, value=0.6050052),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.25,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                            SplinePoint(location=0.2, derivative=0.0, value=0.6050052),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=-0.1,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.05, derivative=0.0, value=0.4351369),
                                            SplinePoint(location=0.05, derivative=0.0, value=0.6969027),
                                        ],
                                    ),
                                ),
                                SplinePoint(
                                    location=0.03,
                                    derivative=0.0,
                                    value=CubicSplineStruct(
                                        coordinate='minecraft:overworld/ridges',
                                        points=[
                                            SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                            SplinePoint(location=0.2, derivative=0.0, value=0.6050052),
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
                                                        SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                                        SplinePoint(location=0.2, derivative=0.0, value=0.6050052),
                                                    ],
                                                ),
                                            ),
                                            SplinePoint(location=0.7, derivative=0.0, value=0.2972561),
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
                                                        SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                                        SplinePoint(location=0.2, derivative=0.0, value=0.6050052),
                                                    ],
                                                ),
                                            ),
                                            SplinePoint(location=0.7, derivative=0.0, value=0.2972561),
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
                                                        SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                                        SplinePoint(location=0.2, derivative=0.0, value=0.6050052),
                                                    ],
                                                ),
                                            ),
                                            SplinePoint(location=-0.15, derivative=0.0, value=0.2688383),
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
                                                        SplinePoint(location=-0.2, derivative=0.0, value=0.6969027),
                                                        SplinePoint(location=0.2, derivative=0.0, value=0.6050052),
                                                    ],
                                                ),
                                            ),
                                            SplinePoint(location=-0.15, derivative=0.0, value=0.2688383),
                                        ],
                                    ),
                                ),
                                SplinePoint(location=0.58, derivative=0.0, value=0.6050052),
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
                            first=0.4,
                            second=DensityFunctionStructLerp(
                                alpha=DensityFunctionStructGradient(
                                    axis=Axis.Y,
                                    from_coordinate=304,
                                    to_coordinate=320,
                                    from_value=1.0,
                                    to_value=0.0,
                                    type='minecraft:gradient',
                                ),
                                first=-0.078125,
                                second=DensityFunctionStructRangeChoice(
                                    input='minecraft:overworld_amplified/sloped_cheese',
                                    min_inclusive=-1000000.0,
                                    max_exclusive=1.5625,
                                    when_in_range=DensityFunctionStructMin(
                                        left='minecraft:overworld_amplified/sloped_cheese',
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
                                                                    left='minecraft:overworld_amplified/sloped_cheese',
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
                coordinate='minecraft:overworld/continents',
                points=[
                    SplinePoint(location=-0.11, derivative=0.0, value=0.0),
                    SplinePoint(
                        location=0.03,
                        derivative=0.0,
                        value=CubicSplineStruct(
                            coordinate='minecraft:overworld/erosion',
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
                                                        SplinePoint(location=-0.01, derivative=0.0, value=1.26),
                                                        SplinePoint(location=0.01, derivative=0.0, value=0.6),
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
                    SplinePoint(
                        location=0.65,
                        derivative=0.0,
                        value=CubicSplineStruct(
                            coordinate='minecraft:overworld/erosion',
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
                                                        SplinePoint(location=-0.01, derivative=0.0, value=1.26),
                                                        SplinePoint(location=0.01, derivative=0.0, value=0.6),
                                                    ],
                                                ),
                                            ),
                                            SplinePoint(
                                                location=1.0,
                                                derivative=0.0,
                                                value=CubicSplineStruct(
                                                    coordinate='minecraft:overworld/ridges',
                                                    points=[
                                                        SplinePoint(location=-0.01, derivative=0.0, value=1.26),
                                                        SplinePoint(location=0.01, derivative=0.0, value=0.6),
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
                                                        SplinePoint(location=-0.01, derivative=0.0, value=1.26),
                                                        SplinePoint(location=0.01, derivative=0.0, value=0.6),
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
                                                        SplinePoint(location=-0.01, derivative=0.0, value=1.26),
                                                        SplinePoint(location=0.01, derivative=0.0, value=0.6),
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
                    coordinate='minecraft:overworld/continents',
                    points=[
                        SplinePoint(location=-1.1, derivative=0.0, value=0.088),
                        SplinePoint(location=-1.02, derivative=0.0, value=-0.2222),
                        SplinePoint(location=-0.51, derivative=0.0, value=-0.2222),
                        SplinePoint(location=-0.44, derivative=0.0, value=-0.12),
                        SplinePoint(location=-0.18, derivative=0.0, value=-0.12),
                        SplinePoint(
                            location=-0.16,
                            derivative=0.0,
                            value=CubicSplineStruct(
                                coordinate='minecraft:overworld/erosion',
                                points=[
                                    SplinePoint(
                                        location=-0.85,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.38940096, value=-0.08880186),
                                                SplinePoint(location=1.0, derivative=0.38940096, value=1.3800001),
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
                                                SplinePoint(location=1.0, derivative=0.37788022, value=1.2800002),
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
                                                SplinePoint(location=0.5954547, derivative=0.0, value=5.9604645e-08),
                                                SplinePoint(
                                                    location=0.6054547,
                                                    derivative=0.2534563,
                                                    value=5.9604645e-08,
                                                ),
                                                SplinePoint(location=1.0, derivative=0.2534563, value=0.20000005),
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
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.1),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.1),
                                                SplinePoint(location=0.4, derivative=0.0, value=0.1),
                                                SplinePoint(location=1.0, derivative=0.007000001, value=0.120000005),
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
                                                SplinePoint(location=0.4, derivative=0.1, value=0.1),
                                                SplinePoint(location=1.0, derivative=0.007000001, value=0.120000005),
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
                                coordinate='minecraft:overworld/erosion',
                                points=[
                                    SplinePoint(
                                        location=-0.85,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.38940096, value=-0.08880186),
                                                SplinePoint(location=1.0, derivative=0.38940096, value=1.3800001),
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
                                                SplinePoint(location=1.0, derivative=0.37788022, value=1.2800002),
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
                                                SplinePoint(location=0.5954547, derivative=0.0, value=5.9604645e-08),
                                                SplinePoint(
                                                    location=0.6054547,
                                                    derivative=0.2534563,
                                                    value=5.9604645e-08,
                                                ),
                                                SplinePoint(location=1.0, derivative=0.2534563, value=0.20000005),
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
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.1),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.1),
                                                SplinePoint(location=0.4, derivative=0.0, value=0.1),
                                                SplinePoint(location=1.0, derivative=0.007000001, value=0.120000005),
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
                                                SplinePoint(location=0.4, derivative=0.1, value=0.1),
                                                SplinePoint(location=1.0, derivative=0.007000001, value=0.120000005),
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
                                coordinate='minecraft:overworld/erosion',
                                points=[
                                    SplinePoint(
                                        location=-0.85,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.38940096, value=-0.08880186),
                                                SplinePoint(location=1.0, derivative=0.38940096, value=1.3800001),
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
                                                SplinePoint(location=1.0, derivative=0.37788022, value=1.2800002),
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
                                                SplinePoint(location=0.5954547, derivative=0.0, value=5.9604645e-08),
                                                SplinePoint(
                                                    location=0.6054547,
                                                    derivative=0.2534563,
                                                    value=5.9604645e-08,
                                                ),
                                                SplinePoint(location=1.0, derivative=0.2534563, value=0.20000005),
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
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.1),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.1),
                                                SplinePoint(location=0.4, derivative=0.0, value=0.1),
                                                SplinePoint(location=1.0, derivative=0.007000001, value=0.120000005),
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
                                                SplinePoint(location=-0.4, derivative=0.01, value=0.002),
                                                SplinePoint(location=0.0, derivative=0.01, value=0.006),
                                                SplinePoint(location=0.4, derivative=0.094000004, value=0.1),
                                                SplinePoint(location=1.0, derivative=0.007000001, value=0.120000005),
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
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.06),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.2),
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
                                                SplinePoint(location=0.4, derivative=0.12, value=0.06),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.2),
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
                                coordinate='minecraft:overworld/erosion',
                                points=[
                                    SplinePoint(
                                        location=-0.85,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=0.40470043),
                                                SplinePoint(location=0.0, derivative=0.5138249, value=1.4323502),
                                                SplinePoint(location=1.0, derivative=0.5138249, value=2.46),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.7,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=0.4),
                                                SplinePoint(location=0.0, derivative=0.43317974, value=0.8936405),
                                                SplinePoint(location=1.0, derivative=0.43317974, value=1.76),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.4,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=0.4),
                                                SplinePoint(location=0.0, derivative=0.3917051, value=0.6165899),
                                                SplinePoint(location=1.0, derivative=0.3917051, value=1.4000001),
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
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.7),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.7),
                                                SplinePoint(location=0.4, derivative=0.0, value=0.7),
                                                SplinePoint(location=1.0, derivative=0.049000014, value=0.84000003),
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
                                                SplinePoint(location=-0.4, derivative=0.07, value=0.0139999995),
                                                SplinePoint(location=0.0, derivative=0.07, value=0.042),
                                                SplinePoint(location=0.4, derivative=0.658, value=0.7),
                                                SplinePoint(location=1.0, derivative=0.049000014, value=0.84000003),
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
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.06),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.2),
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
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.06),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.2),
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
                                                            SplinePoint(location=-0.4, derivative=0.0, value=0.02),
                                                            SplinePoint(location=0.0, derivative=0.0, value=0.02),
                                                            SplinePoint(location=0.4, derivative=0.04, value=0.06),
                                                            SplinePoint(location=1.0, derivative=0.049, value=0.2),
                                                        ],
                                                    ),
                                                ),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.34),
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
                                                            SplinePoint(location=-0.4, derivative=0.0, value=0.02),
                                                            SplinePoint(location=0.0, derivative=0.0, value=0.02),
                                                            SplinePoint(location=0.4, derivative=0.04, value=0.06),
                                                            SplinePoint(location=1.0, derivative=0.049, value=0.2),
                                                        ],
                                                    ),
                                                ),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.34),
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
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.06),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.2),
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
                                                SplinePoint(location=0.4, derivative=0.12, value=0.06),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.2),
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
                                coordinate='minecraft:overworld/erosion',
                                points=[
                                    SplinePoint(
                                        location=-0.85,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=0.6958525),
                                                SplinePoint(location=0.0, derivative=0.5760369, value=1.8479263),
                                                SplinePoint(location=1.0, derivative=0.5760369, value=3.0),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.7,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=0.4),
                                                SplinePoint(location=0.0, derivative=0.4608295, value=1.078341),
                                                SplinePoint(location=1.0, derivative=0.4608295, value=2.0),
                                            ],
                                        ),
                                    ),
                                    SplinePoint(
                                        location=-0.4,
                                        derivative=0.0,
                                        value=CubicSplineStruct(
                                            coordinate='minecraft:overworld/ridges_folded',
                                            points=[
                                                SplinePoint(location=-1.0, derivative=0.0, value=0.4),
                                                SplinePoint(location=0.0, derivative=0.4608295, value=1.078341),
                                                SplinePoint(location=1.0, derivative=0.4608295, value=2.0),
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
                                                SplinePoint(location=-0.4, derivative=0.0, value=1.0),
                                                SplinePoint(location=0.0, derivative=0.0, value=1.0),
                                                SplinePoint(location=0.4, derivative=0.0, value=1.0),
                                                SplinePoint(location=1.0, derivative=0.070000015, value=1.2),
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
                                                SplinePoint(location=-0.4, derivative=0.099999994, value=0.02),
                                                SplinePoint(location=0.0, derivative=0.099999994, value=0.06),
                                                SplinePoint(location=0.4, derivative=0.94, value=1.0),
                                                SplinePoint(location=1.0, derivative=0.070000015, value=1.2),
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
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.06),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.2),
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
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.06),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.2),
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
                                                            SplinePoint(location=-0.4, derivative=0.0, value=0.02),
                                                            SplinePoint(location=0.0, derivative=0.0, value=0.02),
                                                            SplinePoint(location=0.4, derivative=0.04, value=0.06),
                                                            SplinePoint(location=1.0, derivative=0.049, value=0.2),
                                                        ],
                                                    ),
                                                ),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.34),
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
                                                            SplinePoint(location=-0.4, derivative=0.0, value=0.02),
                                                            SplinePoint(location=0.0, derivative=0.0, value=0.02),
                                                            SplinePoint(location=0.4, derivative=0.04, value=0.06),
                                                            SplinePoint(location=1.0, derivative=0.049, value=0.2),
                                                        ],
                                                    ),
                                                ),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.34),
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
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.06),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.2),
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
                                                SplinePoint(location=-0.4, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.0, derivative=0.0, value=0.02),
                                                SplinePoint(location=0.4, derivative=0.04, value=0.06),
                                                SplinePoint(location=1.0, derivative=0.049, value=0.2),
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
            first=0.4,
            second=DensityFunctionStructLerp(
                alpha=DensityFunctionStructGradient(
                    axis=Axis.Y,
                    from_coordinate=304,
                    to_coordinate=320,
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
                                        right='minecraft:overworld_amplified/offset',
                                        type='minecraft:add',
                                    ),
                                    right='minecraft:overworld_amplified/factor',
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
                        right='minecraft:overworld_amplified/factor',
                        type='minecraft:div',
                    ),
                    right='minecraft:overworld_amplified/offset',
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
                        left='minecraft:overworld_amplified/depth',
                        right=DensityFunctionStructCache(
                            input=DensityFunctionStructMul(
                                left='minecraft:overworld_amplified/jaggedness',
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
                    right='minecraft:overworld_amplified/factor',
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
