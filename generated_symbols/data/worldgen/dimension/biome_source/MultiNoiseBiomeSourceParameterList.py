"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::MultiNoiseBiomeSourceParameterList
Local link to file: generated_symbols/data/worldgen/dimension/biome_source/MultiNoiseBiomeSourceParameterList.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.biome_source.MultiNoisePreset import MultiNoisePreset


@dataclass(kw_only=True)
class MultiNoiseBiomeSourceParameterList:
    __resource_dir__: ClassVar[str] = 'worldgen/multi_noise_biome_source_parameter_list'

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

