"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::BlockStateProvider
Local link to file: generated_symbols/data/worldgen/feature/block_state_provider/BlockStateProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

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


@dataclass(kw_only=True)
class BlockStateProviderCopyPropertiesProvider(CopyPropertiesProvider):
    type: Literal['minecraft:copy_properties_provider']


@dataclass(kw_only=True)
class BlockStateProviderDualNoiseProvider(DualNoiseProvider):
    type: Literal['minecraft:dual_noise_provider']


@dataclass(kw_only=True)
class BlockStateProviderNoiseProvider(NoiseProvider):
    type: Literal['minecraft:noise_provider']


@dataclass(kw_only=True)
class BlockStateProviderNoiseThresholdProvider(NoiseThresholdProvider):
    type: Literal['minecraft:noise_threshold_provider']


@dataclass(kw_only=True)
class BlockStateProviderRandomBlockProvider(RandomBlockStateProvider):
    type: Literal['minecraft:random_block_provider']


@dataclass(kw_only=True)
class BlockStateProviderRandomizedIntStateProvider(RandomizedIntStateProvider):
    type: Literal['minecraft:randomized_int_state_provider']


@dataclass(kw_only=True)
class BlockStateProviderRotatedBlockProvider(RotatedStateProvider):
    type: Literal['minecraft:rotated_block_provider']


@dataclass(kw_only=True)
class BlockStateProviderRuleBasedStateProvider(RuleBasedBlockStateProvider):
    type: Literal['minecraft:rule_based_state_provider']


@dataclass(kw_only=True)
class BlockStateProviderSimpleStateProvider(SimpleStateProvider):
    type: Literal['minecraft:simple_state_provider']


@dataclass(kw_only=True)
class BlockStateProviderWeightedStateProvider(WeightedBlockStateProvider):
    type: Literal['minecraft:weighted_state_provider']


type BlockStateProvider = BlockStateProviderCopyPropertiesProvider | BlockStateProviderDualNoiseProvider | BlockStateProviderNoiseProvider | BlockStateProviderNoiseThresholdProvider | BlockStateProviderRandomBlockProvider | BlockStateProviderRandomizedIntStateProvider | BlockStateProviderRotatedBlockProvider | BlockStateProviderRuleBasedStateProvider | BlockStateProviderSimpleStateProvider | BlockStateProviderWeightedStateProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_state_provider::BlockStateProvider": {
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

