"""
Generated from symbols.json for ::java::data::worldgen::material_condition::NoiseThresholdCondition
Local link to file: vanilla_mcdoc/data/worldgen/material_condition/NoiseThresholdCondition.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class NoiseThresholdCondition(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    noise: Annotated[str, IdSpec(registry='worldgen/noise')]
    min_threshold: float
    max_threshold: float
    is_3d: bool | None = None  # Defaults to `false`.
