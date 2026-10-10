"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::BiomeSource
Local link to file: generated_symbols/data/worldgen/dimension/biome_source/BiomeSource.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from generated_symbols.data.worldgen.dimension.biome_source.Checkerboard import Checkerboard
from generated_symbols.data.worldgen.dimension.biome_source.DirectMultiNoise import DirectMultiNoise
from generated_symbols.data.worldgen.dimension.biome_source.Fixed import Fixed
from generated_symbols.data.worldgen.dimension.biome_source.MultiNoiseBase import MultiNoiseBase
from generated_symbols.data.worldgen.dimension.biome_source.TheEnd import TheEnd
from minecraft_registry import IdSpec


class BiomeSourceCheckerboard(Checkerboard):
    type: Literal['minecraft:checkerboard', 'checkerboard'] = 'minecraft:checkerboard'


class BiomeSourceFixed(Fixed):
    type: Literal['minecraft:fixed', 'fixed'] = 'minecraft:fixed'


class BiomeSourceMultiNoiseNone(DirectMultiNoise, MultiNoiseBase):
    type: Literal['minecraft:multi_noise', 'multi_noise'] = 'minecraft:multi_noise'
    preset: Annotated[str, IdSpec(registry='worldgen/multi_noise_biome_source_parameter_list')] | None = None


class BiomeSourceMultiNoiseUnknown(MultiNoiseBase):
    type: Literal['minecraft:multi_noise', 'multi_noise'] = 'minecraft:multi_noise'
    preset: Annotated[str, IdSpec(registry='worldgen/multi_noise_biome_source_parameter_list')] | None = None


type BiomeSourceMultiNoise = BiomeSourceMultiNoiseNone | BiomeSourceMultiNoiseUnknown

class BiomeSourceTheEnd(TheEnd):
    type: Literal['minecraft:the_end', 'the_end'] = 'minecraft:the_end'


type BiomeSource = Annotated[
    BiomeSourceCheckerboard | BiomeSourceFixed | BiomeSourceMultiNoise | BiomeSourceTheEnd,
    Field(discriminator='type'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::biome_source::BiomeSource": {
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
                                    "value": "worldgen/biome_source"
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
                    "registry": "minecraft:biome_source"
                }
            }
        ]
    }
}

