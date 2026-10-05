"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::TypedBlockStateProvider
Local link to file: generated_symbols/data/worldgen/feature/block_state_provider/TypedBlockStateProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from generated_symbols.base import GeneratedModel
from generated_symbols.data.worldgen.feature.RuleBasedBlockStateProvider import RuleBasedBlockStateProvider
from generated_symbols.data.worldgen.feature.block_state_provider.CopyPropertiesProvider import CopyPropertiesProvider
from generated_symbols.data.worldgen.feature.block_state_provider.DualNoiseProvider import DualNoiseProvider
from generated_symbols.data.worldgen.feature.block_state_provider.NoiseProvider import NoiseProvider
from generated_symbols.data.worldgen.feature.block_state_provider.NoiseThresholdProvider import NoiseThresholdProvider
from generated_symbols.data.worldgen.feature.block_state_provider.RandomBlockStateProvider import RandomBlockStateProvider
from generated_symbols.data.worldgen.feature.block_state_provider.RandomizedIntStateProvider import RandomizedIntStateProvider
from generated_symbols.data.worldgen.feature.block_state_provider.RotatedStateProvider import RotatedStateProvider
from generated_symbols.data.worldgen.feature.block_state_provider.SimpleStateProvider import SimpleStateProvider
from generated_symbols.data.worldgen.feature.block_state_provider.WeightedBlockStateProvider import WeightedBlockStateProvider
from minecraft_registry import IdSpec


class TypedBlockStateProviderNone(GeneratedModel):
    type: Annotated[str, IdSpec(registry='worldgen/block_state_provider_type')]


class TypedBlockStateProviderCopyProperties(CopyPropertiesProvider):
    type: Literal['minecraft:copy_properties'] = 'minecraft:copy_properties'


class TypedBlockStateProviderDualNoise(DualNoiseProvider):
    type: Literal['minecraft:dual_noise'] = 'minecraft:dual_noise'


class TypedBlockStateProviderNoise(NoiseProvider):
    type: Literal['minecraft:noise'] = 'minecraft:noise'


class TypedBlockStateProviderNoiseThreshold(NoiseThresholdProvider):
    type: Literal['minecraft:noise_threshold'] = 'minecraft:noise_threshold'


class TypedBlockStateProviderRandomBlock(RandomBlockStateProvider):
    type: Literal['minecraft:random_block'] = 'minecraft:random_block'


class TypedBlockStateProviderRandomizedInt(RandomizedIntStateProvider):
    type: Literal['minecraft:randomized_int'] = 'minecraft:randomized_int'


class TypedBlockStateProviderRotated(RotatedStateProvider):
    type: Literal['minecraft:rotated'] = 'minecraft:rotated'


class TypedBlockStateProviderRuleBased(RuleBasedBlockStateProvider):
    type: Literal['minecraft:rule_based'] = 'minecraft:rule_based'


class TypedBlockStateProviderSimple(SimpleStateProvider):
    type: Literal['minecraft:simple'] = 'minecraft:simple'


class TypedBlockStateProviderWeighted(WeightedBlockStateProvider):
    type: Literal['minecraft:weighted'] = 'minecraft:weighted'


type TypedBlockStateProvider = TypedBlockStateProviderNone | TypedBlockStateProviderCopyProperties | TypedBlockStateProviderDualNoise | TypedBlockStateProviderNoise | TypedBlockStateProviderNoiseThreshold | TypedBlockStateProviderRandomBlock | TypedBlockStateProviderRandomizedInt | TypedBlockStateProviderRotated | TypedBlockStateProviderRuleBased | TypedBlockStateProviderSimple | TypedBlockStateProviderWeighted


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_state_provider::TypedBlockStateProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/block_state_provider_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:block_state_provider"
                }
            }
        ]
    }
}

