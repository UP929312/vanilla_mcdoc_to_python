"""Vanilla's data/worldgen/density_function/ files"""
from vanilla_mcdoc.data.worldgen.density_function.DensityFunction import DensityFunctionStructCache, DensityFunctionStructGradient, DensityFunctionStructShiftA, DensityFunctionStructShiftB
from vanilla_mcdoc.util.direction.Axis import Axis

SHIFT_X = DensityFunctionStructCache(
    input=DensityFunctionStructShiftA(noise='minecraft:offset', type='minecraft:shift_a'),
    type='minecraft:cache',
)

SHIFT_Z = DensityFunctionStructCache(
    input=DensityFunctionStructShiftB(noise='minecraft:offset', type='minecraft:shift_b'),
    type='minecraft:cache',
)

Y = DensityFunctionStructGradient(
    axis=Axis.Y,
    from_coordinate=-4064,
    to_coordinate=4062,
    from_value=-4064.0,
    to_value=4062.0,
    type='minecraft:gradient',
)

ZERO = 0.0
