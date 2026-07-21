# Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::MultiNoiseBiomeSourceParameterList
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.biome_source.MultiNoisePreset import MultiNoisePreset


@dataclass(kw_only=True)
class MultiNoiseBiomeSourceParameterList:
    preset: MultiNoisePreset


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::biome_source::MultiNoiseBiomeSourceParameterList": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "preset",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::MultiNoisePreset",
                    "attributes": [
                        {
                            "name": "id"
                        }
                    ]
                }
            }
        ]
    }
}

