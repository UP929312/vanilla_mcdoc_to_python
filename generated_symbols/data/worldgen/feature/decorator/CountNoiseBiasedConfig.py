# Generated from symbols.json for ::java::data::worldgen::feature::decorator::CountNoiseBiasedConfig
from dataclasses import dataclass


@dataclass(kw_only=True)
class CountNoiseBiasedConfig:
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

