"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::TypedBlockStateProvider
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_state_provider/TypedBlockStateProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.worldgen.feature.RuleBasedBlockStateProvider import RuleBasedBlockStateProvider
from vanilla_mcdoc.data.worldgen.feature.block_state_provider.CopyPropertiesProvider import CopyPropertiesProvider
from vanilla_mcdoc.data.worldgen.feature.block_state_provider.DualNoiseProvider import DualNoiseProvider
from vanilla_mcdoc.data.worldgen.feature.block_state_provider.NoiseProvider import NoiseProvider
from vanilla_mcdoc.data.worldgen.feature.block_state_provider.NoiseThresholdProvider import NoiseThresholdProvider
from vanilla_mcdoc.data.worldgen.feature.block_state_provider.RandomBlockStateProvider import RandomBlockStateProvider
from vanilla_mcdoc.data.worldgen.feature.block_state_provider.RandomizedIntStateProvider import RandomizedIntStateProvider
from vanilla_mcdoc.data.worldgen.feature.block_state_provider.RotatedStateProvider import RotatedStateProvider
from vanilla_mcdoc.data.worldgen.feature.block_state_provider.SimpleStateProvider import SimpleStateProvider
from vanilla_mcdoc.data.worldgen.feature.block_state_provider.WeightedBlockStateProvider import WeightedBlockStateProvider
from vanilla_mcdoc.minecraft_types import IdSpec


class TypedBlockStateProviderDefault(GeneratedModel):
    type: Annotated[str, IdSpec(registry='worldgen/block_state_provider_type')]


class TypedBlockStateProviderCopyProperties(CopyPropertiesProvider):
    type: Literal['minecraft:copy_properties', 'copy_properties'] = 'minecraft:copy_properties'


class TypedBlockStateProviderDualNoise(DualNoiseProvider):
    type: Literal['minecraft:dual_noise', 'dual_noise'] = 'minecraft:dual_noise'


class TypedBlockStateProviderNoise(NoiseProvider):
    type: Literal['minecraft:noise', 'noise'] = 'minecraft:noise'


class TypedBlockStateProviderNoiseThreshold(NoiseThresholdProvider):
    type: Literal['minecraft:noise_threshold', 'noise_threshold'] = 'minecraft:noise_threshold'


class TypedBlockStateProviderRandomBlock(RandomBlockStateProvider):
    type: Literal['minecraft:random_block', 'random_block'] = 'minecraft:random_block'


class TypedBlockStateProviderRandomizedInt(RandomizedIntStateProvider):
    type: Literal['minecraft:randomized_int', 'randomized_int'] = 'minecraft:randomized_int'


class TypedBlockStateProviderRotated(RotatedStateProvider):
    type: Literal['minecraft:rotated', 'rotated'] = 'minecraft:rotated'


class TypedBlockStateProviderRuleBased(RuleBasedBlockStateProvider):
    type: Literal['minecraft:rule_based', 'rule_based'] = 'minecraft:rule_based'


class TypedBlockStateProviderSimple(SimpleStateProvider):
    type: Literal['minecraft:simple', 'simple'] = 'minecraft:simple'


class TypedBlockStateProviderWeighted(WeightedBlockStateProvider):
    type: Literal['minecraft:weighted', 'weighted'] = 'minecraft:weighted'


type TypedBlockStateProvider = TypedBlockStateProviderDefault | TypedBlockStateProviderCopyProperties | TypedBlockStateProviderDualNoise | TypedBlockStateProviderNoise | TypedBlockStateProviderNoiseThreshold | TypedBlockStateProviderRandomBlock | TypedBlockStateProviderRandomizedInt | TypedBlockStateProviderRotated | TypedBlockStateProviderRuleBased | TypedBlockStateProviderSimple | TypedBlockStateProviderWeighted
