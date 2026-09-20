"""
Generated from symbols.json for ::java::data::worldgen::structure::OceanRuin
Local link to file: generated_symbols/data/worldgen/structure/OceanRuin.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure.BiomeTemperature import BiomeTemperature


class OceanRuin(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    biome_temp: BiomeTemperature
    large_probability: Annotated[float, Field(ge=0, le=1)]
    cluster_probability: Annotated[float, Field(ge=0, le=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::OceanRuin": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "biome_temp",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure::BiomeTemperature"
                }
            },
            {
                "kind": "pair",
                "key": "large_probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "cluster_probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}

