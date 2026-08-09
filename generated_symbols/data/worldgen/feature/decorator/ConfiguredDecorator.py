# Generated from symbols.json for ::java::data::worldgen::feature::decorator::ConfiguredDecorator
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.decorator.CarvingMaskConfig import CarvingMaskConfig
    from generated_symbols.data.worldgen.feature.decorator.CaveSurface import CaveSurface
    from generated_symbols.data.worldgen.feature.decorator.ChanceConfig import ChanceConfig
    from generated_symbols.data.worldgen.feature.decorator.CountConfig import CountConfig
    from generated_symbols.data.worldgen.feature.decorator.CountExtraConfig import CountExtraConfig
    from generated_symbols.data.worldgen.feature.decorator.CountNoiseBiasedConfig import CountNoiseBiasedConfig
    from generated_symbols.data.worldgen.feature.decorator.CountNoiseConfig import CountNoiseConfig
    from generated_symbols.data.worldgen.feature.decorator.DecoratedConfig import DecoratedConfig
    from generated_symbols.data.worldgen.feature.decorator.DepthAverageConfig import DepthAverageConfig
    from generated_symbols.data.worldgen.feature.decorator.HeightmapConfig import HeightmapConfig
    from generated_symbols.data.worldgen.feature.decorator.OldRangeConfig import OldRangeConfig
    from generated_symbols.data.worldgen.feature.decorator.RangeConfig import RangeConfig
    from generated_symbols.data.worldgen.feature.decorator.WaterDepthThresholdConfig import WaterDepthThresholdConfig


@dataclass(kw_only=True)
class ConfigStructDecoratorConfigDarkOakTree:
    pass


@dataclass(kw_only=True)
class ConfiguredDecorator:
    type: Annotated[str, IdSpec(registry='worldgen/decorator')]
    config: CarvingMaskConfig | CaveSurface | ChanceConfig | CountConfig | CountExtraConfig | CountNoiseConfig | CountNoiseBiasedConfig | ConfigStructDecoratorConfigDarkOakTree | DecoratedConfig | DepthAverageConfig | HeightmapConfig | RangeConfig | OldRangeConfig | WaterDepthThresholdConfig


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::decorator::ConfiguredDecorator": {
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
                                    "value": "worldgen/decorator"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "config",
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
                    "registry": "minecraft:decorator_config"
                }
            }
        ]
    }
}

