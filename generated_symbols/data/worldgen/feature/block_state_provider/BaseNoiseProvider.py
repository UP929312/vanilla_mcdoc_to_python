# Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::BaseNoiseProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.biome_source.NoiseParameters import NoiseParameters


@dataclass(kw_only=True)
class BaseNoiseProvider:
    seed: int
    noise: NoiseParameters
    scale: Annotated[float, 'Range | Min `0` and above | inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_state_provider::BaseNoiseProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "seed",
                "type": {
                    "kind": "int",
                    "attributes": [
                        {
                            "name": "random"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "noise",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::NoiseParameters"
                }
            },
            {
                "kind": "pair",
                "key": "scale",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            }
        ]
    }
}

