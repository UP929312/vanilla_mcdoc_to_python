"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::CountNoiseBiasedConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/decorator/CountNoiseBiasedConfig.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class CountNoiseBiasedConfig(GeneratedModel):
    noise_to_count_ratio: int
    noise_factor: float
    noise_offset: float | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::decorator::CountNoiseBiasedConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "noise_to_count_ratio",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "noise_factor",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "noise_offset",
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ]
    }
}
