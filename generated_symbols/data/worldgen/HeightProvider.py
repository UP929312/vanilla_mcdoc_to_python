"""
Generated from symbols.json for ::java::data::worldgen::HeightProvider
Local link to file: generated_symbols/data/worldgen/HeightProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from generated_symbols.data.worldgen.BottomBiasHeightProvider import BottomBiasHeightProvider
from generated_symbols.data.worldgen.ConstantHeightProvider import ConstantHeightProvider
from generated_symbols.data.worldgen.TrapezoidHeightProvider import TrapezoidHeightProvider
from generated_symbols.data.worldgen.UniformHeightProvider import UniformHeightProvider
from generated_symbols.data.worldgen.WeightListHeightProvider import WeightListHeightProvider

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.VerticalAnchor import VerticalAnchor


@dataclass(kw_only=True)
class HeightProviderStructBiasedToBottom(BottomBiasHeightProvider):
    type: Literal['minecraft:biased_to_bottom'] = 'minecraft:biased_to_bottom'


@dataclass(kw_only=True)
class HeightProviderStructConstant(ConstantHeightProvider):
    type: Literal['minecraft:constant'] = 'minecraft:constant'


@dataclass(kw_only=True)
class HeightProviderStructTrapezoid(TrapezoidHeightProvider):
    type: Literal['minecraft:trapezoid'] = 'minecraft:trapezoid'


@dataclass(kw_only=True)
class HeightProviderStructUniform(UniformHeightProvider):
    type: Literal['minecraft:uniform'] = 'minecraft:uniform'


@dataclass(kw_only=True)
class HeightProviderStructVeryBiasedToBottom(BottomBiasHeightProvider):
    type: Literal['minecraft:very_biased_to_bottom'] = 'minecraft:very_biased_to_bottom'


@dataclass(kw_only=True)
class HeightProviderStructWeightedList(WeightListHeightProvider):
    type: Literal['minecraft:weighted_list'] = 'minecraft:weighted_list'


type HeightProviderStruct = HeightProviderStructBiasedToBottom | HeightProviderStructConstant | HeightProviderStructTrapezoid | HeightProviderStructUniform | HeightProviderStructVeryBiasedToBottom | HeightProviderStructWeightedList

type HeightProvider = HeightProviderStruct | VerticalAnchor


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::HeightProvider": {
        "kind": "union",
        "members": [
            {
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
                                            "value": "height_provider_type"
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
                            "registry": "minecraft:height_provider"
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::worldgen::VerticalAnchor"
            }
        ]
    }
}

