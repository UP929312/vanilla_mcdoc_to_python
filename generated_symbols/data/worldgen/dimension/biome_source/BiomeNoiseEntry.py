# Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::BiomeNoiseEntry
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.biome_source.ClimateParameters import ClimateParameters


@dataclass(kw_only=True)
class BiomeNoiseEntry:
    biome: str
    parameters: ClimateParameters


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::biome_source::BiomeNoiseEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "biome",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/biome"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "parameters",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::ClimateParameters"
                }
            }
        ]
    }
}

