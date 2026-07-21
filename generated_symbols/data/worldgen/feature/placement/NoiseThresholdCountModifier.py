# Generated from symbols.json for ::java::data::worldgen::feature::placement::NoiseThresholdCountModifier
from dataclasses import dataclass


@dataclass(kw_only=True)
class NoiseThresholdCountModifier:
    noise_level: float
    below_noise: int
    above_noise: int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::NoiseThresholdCountModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "noise_level",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "below_noise",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "above_noise",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}

