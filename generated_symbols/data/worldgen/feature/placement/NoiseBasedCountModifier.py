"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::NoiseBasedCountModifier
Local link to file: generated_symbols/data/worldgen/feature/placement/NoiseBasedCountModifier.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class NoiseBasedCountModifier(GeneratedModel):
    noise_to_count_ratio: int
    noise_factor: float
    noise_offset: float | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::NoiseBasedCountModifier": {
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
