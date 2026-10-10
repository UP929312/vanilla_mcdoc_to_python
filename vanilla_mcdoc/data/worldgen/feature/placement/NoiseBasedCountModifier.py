"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::NoiseBasedCountModifier
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/NoiseBasedCountModifier.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class NoiseBasedCountModifier(GeneratedModel):
    noise_to_count_ratio: int
    noise_factor: float
    noise_offset: float | None = None
