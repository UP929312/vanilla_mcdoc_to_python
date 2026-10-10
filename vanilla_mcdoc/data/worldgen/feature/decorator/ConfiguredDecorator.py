"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::ConfiguredDecorator
Local link to file: vanilla_mcdoc/data/worldgen/feature/decorator/ConfiguredDecorator.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.decorator.CarvingMaskConfig import CarvingMaskConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.CaveSurface import CaveSurface
    from vanilla_mcdoc.data.worldgen.feature.decorator.ChanceConfig import ChanceConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.CountConfig import CountConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.CountExtraConfig import CountExtraConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.CountNoiseBiasedConfig import CountNoiseBiasedConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.CountNoiseConfig import CountNoiseConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.DecoratedConfig import DecoratedConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.HeightmapConfig import HeightmapConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.RangeConfig import RangeConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.WaterDepthThresholdConfig import WaterDepthThresholdConfig


class ConfigStructDecoratorConfigDarkOakTree(GeneratedModel):
    pass


class ConfiguredDecorator(GeneratedModel):
    type: Annotated[str, IdSpec(registry='worldgen/decorator')]
    config: CarvingMaskConfig | CaveSurface | ChanceConfig | CountConfig | CountExtraConfig | CountNoiseConfig | CountNoiseBiasedConfig | ConfigStructDecoratorConfigDarkOakTree | DecoratedConfig | HeightmapConfig | RangeConfig | WaterDepthThresholdConfig


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
