"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::CountNoiseConfig
Local link to file: generated_symbols/data/worldgen/feature/decorator/CountNoiseConfig.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class CountNoiseConfig(GeneratedModel):
    noise_level: float
    below_noise: int
    above_noise: int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::decorator::CountNoiseConfig": {
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

