"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::NoiseThresholdCountModifier
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/NoiseThresholdCountModifier.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class NoiseThresholdCountModifier(GeneratedModel):
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
