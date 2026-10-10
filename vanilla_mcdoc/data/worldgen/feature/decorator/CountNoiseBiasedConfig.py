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
