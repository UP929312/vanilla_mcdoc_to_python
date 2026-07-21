# Generated from symbols.json for ::java::data::worldgen::structure::OceanRuin
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure.BiomeTemperature import BiomeTemperature


@dataclass(kw_only=True)
class OceanRuin:
    biome_temp: BiomeTemperature
    large_probability: Annotated[float, 'Range | `0`-`1` | both inclusive']
    cluster_probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


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

