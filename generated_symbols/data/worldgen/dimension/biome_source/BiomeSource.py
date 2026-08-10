"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::BiomeSource
Local link to file: generated_symbols/data/worldgen/dimension/biome_source/BiomeSource.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.worldgen.dimension.biome_source.MultiNoiseBase import MultiNoiseBase
from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.biome_source.ClimateParameters import ClimateParameters


@dataclass(kw_only=True)
class BiomesStruct:
    biome: Annotated[str, IdSpec(registry='worldgen/biome')]
    parameters: ClimateParameters


@dataclass(kw_only=True)
class BiomeSourceCheckerboard:
    type: Literal['minecraft:checkerboard']
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    scale: Annotated[int, 'Range | `0`-`62` | both inclusive'] | None = None


@dataclass(kw_only=True)
class BiomeSourceFixed:
    type: Literal['minecraft:fixed']
    biome: Annotated[str, IdSpec(registry='worldgen/biome')]


@dataclass(kw_only=True)
class BiomeSourceMultiNoiseNone(MultiNoiseBase):
    type: Literal['minecraft:multi_noise']
    biomes: list[BiomesStruct]
    preset: Annotated[str, IdSpec(registry='worldgen/multi_noise_biome_source_parameter_list')] | None = None


@dataclass(kw_only=True)
class BiomeSourceMultiNoiseUnknown(MultiNoiseBase):
    type: Literal['minecraft:multi_noise']
    preset: Annotated[str, IdSpec(registry='worldgen/multi_noise_biome_source_parameter_list')] | None = None


type BiomeSourceMultiNoise = BiomeSourceMultiNoiseNone | BiomeSourceMultiNoiseUnknown

@dataclass(kw_only=True)
class BiomeSourceTheEnd:
    type: Literal['minecraft:the_end']


@dataclass(kw_only=True)
class BiomeSourceVanillaLayered:
    type: Literal['minecraft:vanilla_layered']
    seed: int
    large_biomes: bool | None = None
    legacy_biome_init_layer: bool | None = None


type BiomeSource = BiomeSourceCheckerboard | BiomeSourceFixed | BiomeSourceMultiNoise | BiomeSourceTheEnd | BiomeSourceVanillaLayered


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

