"""Vanilla's data/worldgen/density_function/nether/ files"""
from vanilla_mcdoc.data.worldgen.density_function.DensityFunction import DensityFunctionStructOldBlendedNoise

BASE_3D_NOISE = DensityFunctionStructOldBlendedNoise(
    xz_scale=0.25,
    y_scale=0.375,
    xz_factor=80.0,
    y_factor=60.0,
    smear_scale_multiplier=8.0,
    type='minecraft:old_blended_noise',
)
