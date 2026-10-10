"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::MultiNoise
Local link to file: vanilla_mcdoc/data/worldgen/dimension/biome_source/MultiNoise.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.worldgen.dimension.biome_source.DirectMultiNoise import DirectMultiNoise
from vanilla_mcdoc.data.worldgen.dimension.biome_source.MultiNoiseBase import MultiNoiseBase
from vanilla_mcdoc.minecraft_types import IdSpec


class MultiNoiseNone(DirectMultiNoise, MultiNoiseBase):
    preset: Annotated[str, IdSpec(registry='worldgen/multi_noise_biome_source_parameter_list')] | None = None


class MultiNoiseUnknown(MultiNoiseBase):
    preset: Annotated[str, IdSpec(registry='worldgen/multi_noise_biome_source_parameter_list')] | None = None


type MultiNoise = MultiNoiseNone | MultiNoiseUnknown


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::biome_source::MultiNoise": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::MultiNoiseBase"
                }
            },
            {
                "kind": "pair",
                "key": "preset",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::worldgen::dimension::biome_source::MultiNoisePreset",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.18"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::worldgen::dimension::biome_source::MultiNoisePreset",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.18"
                                        }
                                    }
                                },
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.19.4"
                                        }
                                    }
                                },
                                {
                                    "name": "id"
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.19.4"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/multi_noise_biome_source_parameter_list"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "preset"
                            ]
                        }
                    ],
                    "registry": "minecraft:multi_noise_biome_source"
                }
            }
        ]
    }
}
