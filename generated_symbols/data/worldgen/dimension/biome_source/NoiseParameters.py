# Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::NoiseParameters
from dataclasses import dataclass


@dataclass(kw_only=True)
class NoiseParameters:
    firstOctave: int
    amplitudes: list[float]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::biome_source::NoiseParameters": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "firstOctave",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "amplitudes",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "double"
                    }
                }
            }
        ]
    }
}

