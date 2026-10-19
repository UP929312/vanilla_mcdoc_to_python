"""Vanilla's data/worldgen/density_function/overworld/ore_vein/ files"""
from vanilla_mcdoc.data.worldgen.density_function.DensityFunction import DensityFunctionStructAbs, DensityFunctionStructAdd, DensityFunctionStructCache, DensityFunctionStructClamp, DensityFunctionStructInterpolated, DensityFunctionStructMax, DensityFunctionStructMin, DensityFunctionStructMul, DensityFunctionStructNegate, DensityFunctionStructNoise, DensityFunctionStructRangeChoice, DensityFunctionStructSub

COPPER_DENSITY = DensityFunctionStructRangeChoice(
    input='minecraft:y',
    min_inclusive=0.0,
    max_exclusive=50.0,
    when_in_range=DensityFunctionStructRangeChoice(
        input='minecraft:overworld/ore_vein/mask',
        min_inclusive=0.0,
        max_exclusive=1000000.0,
        when_in_range=DensityFunctionStructRangeChoice(
            input=DensityFunctionStructAdd(
                left=DensityFunctionStructSub(left='minecraft:overworld/ore_vein/toggle', right=0.4, type='minecraft:sub'),
                right=DensityFunctionStructAdd(
                    left=DensityFunctionStructMul(
                        left=DensityFunctionStructClamp(
                            input=DensityFunctionStructMin(
                                left=DensityFunctionStructSub(left=50.0, right='minecraft:y', type='minecraft:sub'),
                                right=DensityFunctionStructSub(left='minecraft:y', right=0.0, type='minecraft:sub'),
                                type='minecraft:min',
                            ),
                            min=0.0,
                            max=20.0,
                            type='minecraft:clamp',
                        ),
                        right=0.01,
                        type='minecraft:mul',
                    ),
                    right=-0.2,
                    type='minecraft:add',
                ),
                type='minecraft:add',
            ),
            min_inclusive=0.0,
            max_exclusive=1000000.0,
            when_in_range=0.7,
            when_out_of_range=-1.0,
            type='minecraft:range_choice',
        ),
        when_out_of_range=-1.0,
        type='minecraft:range_choice',
    ),
    when_out_of_range=-1.0,
    type='minecraft:range_choice',
)

GAP = DensityFunctionStructSub(
    left=-0.3,
    right=DensityFunctionStructNoise(noise='minecraft:ore_gap', xz_scale=1.0, y_scale=1.0, type='minecraft:noise'),
    type='minecraft:sub',
)

IRON_DENSITY = DensityFunctionStructRangeChoice(
    input='minecraft:y',
    min_inclusive=-60.0,
    max_exclusive=-8.0,
    when_in_range=DensityFunctionStructRangeChoice(
        input='minecraft:overworld/ore_vein/mask',
        min_inclusive=0.0,
        max_exclusive=1000000.0,
        when_in_range=DensityFunctionStructRangeChoice(
            input=DensityFunctionStructAdd(
                left=DensityFunctionStructSub(
                    left=DensityFunctionStructNegate(input='minecraft:overworld/ore_vein/toggle', type='minecraft:negate'),
                    right=0.4,
                    type='minecraft:sub',
                ),
                right=DensityFunctionStructAdd(
                    left=DensityFunctionStructMul(
                        left=DensityFunctionStructClamp(
                            input=DensityFunctionStructMin(
                                left=DensityFunctionStructSub(left=-8.0, right='minecraft:y', type='minecraft:sub'),
                                right=DensityFunctionStructSub(left='minecraft:y', right=-60.0, type='minecraft:sub'),
                                type='minecraft:min',
                            ),
                            min=0.0,
                            max=20.0,
                            type='minecraft:clamp',
                        ),
                        right=0.01,
                        type='minecraft:mul',
                    ),
                    right=-0.2,
                    type='minecraft:add',
                ),
                type='minecraft:add',
            ),
            min_inclusive=0.0,
            max_exclusive=1000000.0,
            when_in_range=0.7,
            when_out_of_range=-1.0,
            type='minecraft:range_choice',
        ),
        when_out_of_range=-1.0,
        type='minecraft:range_choice',
    ),
    when_out_of_range=-1.0,
    type='minecraft:range_choice',
)

MASK = DensityFunctionStructCache(
    input=DensityFunctionStructRangeChoice(
        input='minecraft:overworld/ore_vein/toggle',
        min_inclusive=-0.4,
        max_exclusive=0.4,
        when_in_range=-1.0,
        when_out_of_range=DensityFunctionStructSub(
            left=0.08,
            right=DensityFunctionStructMax(
                left=DensityFunctionStructAbs(
                    input=DensityFunctionStructInterpolated(
                        input=DensityFunctionStructRangeChoice(
                            input='minecraft:y',
                            min_inclusive=-64.0,
                            max_exclusive=57.0,
                            when_in_range=DensityFunctionStructNoise(
                                noise='minecraft:ore_vein_a',
                                xz_scale=4.0,
                                y_scale=4.0,
                                type='minecraft:noise',
                            ),
                            when_out_of_range=1.0,
                            type='minecraft:range_choice',
                        ),
                        cell_size_xz=4,
                        cell_size_y=8,
                        type='minecraft:interpolated',
                    ),
                    type='minecraft:abs',
                ),
                right=DensityFunctionStructAbs(
                    input=DensityFunctionStructInterpolated(
                        input=DensityFunctionStructRangeChoice(
                            input='minecraft:y',
                            min_inclusive=-64.0,
                            max_exclusive=57.0,
                            when_in_range=DensityFunctionStructNoise(
                                noise='minecraft:ore_vein_b',
                                xz_scale=4.0,
                                y_scale=4.0,
                                type='minecraft:noise',
                            ),
                            when_out_of_range=1.0,
                            type='minecraft:range_choice',
                        ),
                        cell_size_xz=4,
                        cell_size_y=8,
                        type='minecraft:interpolated',
                    ),
                    type='minecraft:abs',
                ),
                type='minecraft:max',
            ),
            type='minecraft:sub',
        ),
        type='minecraft:range_choice',
    ),
    type='minecraft:cache',
)

RICHNESS = DensityFunctionStructAdd(
    left=DensityFunctionStructMul(
        left=DensityFunctionStructClamp(
            input=DensityFunctionStructAbs(input='minecraft:overworld/ore_vein/toggle', type='minecraft:abs'),
            min=0.4,
            max=0.6,
            type='minecraft:clamp',
        ),
        right=1.0,
        type='minecraft:mul',
    ),
    right=-0.3,
    type='minecraft:add',
)

TOGGLE = DensityFunctionStructCache(
    input=DensityFunctionStructInterpolated(
        input=DensityFunctionStructRangeChoice(
            input='minecraft:y',
            min_inclusive=-64.0,
            max_exclusive=57.0,
            when_in_range=DensityFunctionStructNoise(
                noise='minecraft:ore_veininess',
                xz_scale=1.5,
                y_scale=1.5,
                type='minecraft:noise',
            ),
            when_out_of_range=0.0,
            type='minecraft:range_choice',
        ),
        cell_size_xz=4,
        cell_size_y=8,
        type='minecraft:interpolated',
    ),
    type='minecraft:cache',
)
