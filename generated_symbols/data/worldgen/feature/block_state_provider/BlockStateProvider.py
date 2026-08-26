"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::BlockStateProvider
Local link to file: generated_symbols/data/worldgen/feature/block_state_provider/BlockStateProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.worldgen.feature.block_state_provider.BaseNoiseProvider import BaseNoiseProvider
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.dimension.biome_source.NoiseParameters import NoiseParameters
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from generated_symbols.registry.KnownBlockId import KnownBlockId
    from generated_symbols.util.InclusiveRange import InclusiveRange
    from generated_symbols.util.NonEmptyWeightedList import NonEmptyWeightedList
    from generated_symbols.util.block_state.BlockState import BlockState
    from generated_symbols.util.direction.Direction import Direction


@dataclass(kw_only=True)
class RulesStruct:
    if_true: BlockPredicate
    then: BlockStateProvider


@dataclass(kw_only=True)
class BlockStateProviderCopyPropertiesProvider:
    type: Literal['minecraft:copy_properties_provider']
    source: BlockStateProvider


@dataclass(kw_only=True)
class BlockStateProviderDualNoiseProvider(BaseNoiseProvider):
    type: Literal['minecraft:dual_noise_provider']
    variety: InclusiveRange[Annotated[int, 'Range | `1`-`64` | both inclusive']] | Annotated[int, 'Range | `1`-`64` | both inclusive']
    slow_noise: NoiseParameters
    slow_scale: Annotated[float, 'Range | `0` and above | inclusive']
    states: list[BlockState]


@dataclass(kw_only=True)
class BlockStateProviderNoiseProvider(BaseNoiseProvider):
    type: Literal['minecraft:noise_provider']
    states: list[BlockState]


@dataclass(kw_only=True)
class BlockStateProviderNoiseThresholdProvider(BaseNoiseProvider):
    type: Literal['minecraft:noise_threshold_provider']
    threshold: Annotated[float, 'Range | `-1`-`1` | both inclusive']
    high_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    default_state: BlockState
    low_states: list[BlockState]
    high_states: list[BlockState]


@dataclass(kw_only=True)
class BlockStateProviderRandomBlockProvider:
    type: Literal['minecraft:random_block_provider']
    blocks: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]


@dataclass(kw_only=True)
class BlockStateProviderRandomizedIntStateProvider:
    type: Literal['minecraft:randomized_int_state_provider']
    property: str
    values: IntProvider[int] | int
    source: BlockStateProvider


@dataclass(kw_only=True)
class BlockStateProviderRotatedBlockProvider:
    type: Literal['minecraft:rotated_block_provider']
    state: BlockStateProvider
    direction: Direction | None = None


@dataclass(kw_only=True)
class BlockStateProviderRuleBasedStateProvider:
    type: Literal['minecraft:rule_based_state_provider']
    fallback: BlockStateProvider | None = None
    rules: list[RulesStruct]


@dataclass(kw_only=True)
class BlockStateProviderSimpleStateProvider:
    type: Literal['minecraft:simple_state_provider']
    state: BlockState


@dataclass(kw_only=True)
class BlockStateProviderWeightedStateProvider:
    type: Literal['minecraft:weighted_state_provider']
    entries: NonEmptyWeightedList[BlockState]


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

