"""Vanilla's data/worldgen/multi_noise_biome_source_parameter_list/ files"""
from vanilla_mcdoc.data.worldgen.dimension.biome_source.MultiNoiseBiomeSourceParameterList import MultiNoiseBiomeSourceParameterList
from vanilla_mcdoc.data.worldgen.dimension.biome_source.MultiNoisePreset import MultiNoisePreset

NETHER = MultiNoiseBiomeSourceParameterList(preset=MultiNoisePreset.NETHER)

OVERWORLD = MultiNoiseBiomeSourceParameterList(preset=MultiNoisePreset.OVERWORLD)
