"""Vanilla's data/worldgen/density_function/end/ files"""
from vanilla_mcdoc.data.worldgen.density_function.DensityFunction import DensityFunctionStructAdd, DensityFunctionStructCache, DensityFunctionStructClamp, DensityFunctionStructDistanceToPoint, DensityFunctionStructEndOuterIslands, DensityFunctionStructMax, DensityFunctionStructMul, DensityFunctionStructOldBlendedNoise, DensityFunctionStructSlice, DensityFunctionStructSub
from vanilla_mcdoc.data.worldgen.density_function.DistanceMetric import DistanceMetric
from vanilla_mcdoc.util.direction.Axis import Axis

BASE_3D_NOISE = DensityFunctionStructOldBlendedNoise(
    xz_scale=0.25,
    y_scale=0.25,
    xz_factor=80.0,
    y_factor=160.0,
    smear_scale_multiplier=4.0,
    type='minecraft:old_blended_noise',
)

ISLANDS = DensityFunctionStructCache(
    input=DensityFunctionStructMax(
        left=DensityFunctionStructSlice(
            axis=Axis.Y,
            coordinate=0,
            input=DensityFunctionStructMul(
                left=DensityFunctionStructSub(
                    left=DensityFunctionStructClamp(
                        input=DensityFunctionStructSub(
                            left=100.0,
                            right=DensityFunctionStructDistanceToPoint(
                                point=(0, 0, 0),
                                metric=DistanceMetric.EUCLIDEAN,
                                type='minecraft:distance_to_point',
                            ),
                            type='minecraft:sub',
                        ),
                        min=-100.0,
                        max=80.0,
                        type='minecraft:clamp',
                    ),
                    right=8.0,
                    type='minecraft:sub',
                ),
                right=0.0078125,
                type='minecraft:mul',
            ),
            type='minecraft:slice',
        ),
        right=DensityFunctionStructEndOuterIslands(type='minecraft:end_outer_islands'),
        type='minecraft:max',
    ),
    type='minecraft:cache',
)

SLOPED_CHEESE = DensityFunctionStructAdd(left='minecraft:end/islands', right='minecraft:end/base_3d_noise', type='minecraft:add')
