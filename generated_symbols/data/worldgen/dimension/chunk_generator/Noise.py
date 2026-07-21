# Generated from symbols.json for ::java::data::worldgen::dimension::chunk_generator::Noise
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.biome_source.BiomeSource import BiomeSource
    from generated_symbols.data.worldgen.noise_settings.NoiseGeneratorSettingsRef import NoiseGeneratorSettingsRef


@dataclass(kw_only=True)
class Noise:
    settings: NoiseGeneratorSettingsRef
    biome_source: BiomeSource


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::chunk_generator::Noise": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "seed",
                "type": {
                    "kind": "long",
                    "attributes": [
                        {
                            "name": "random"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "settings",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::noise_settings::NoiseGeneratorSettingsRef"
                }
            },
            {
                "kind": "pair",
                "key": "biome_source",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::BiomeSource"
                }
            }
        ]
    }
}

