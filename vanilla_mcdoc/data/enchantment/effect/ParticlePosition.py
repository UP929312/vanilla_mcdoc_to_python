"""
Generated from symbols.json for ::java::data::enchantment::effect::ParticlePosition
Local link to file: vanilla_mcdoc/data/enchantment/effect/ParticlePosition.py
"""
# ~~~ CODE ~~~
from typing import Literal

from vanilla_mcdoc.base import GeneratedModel


class ParticlePosition(GeneratedModel):
    type: Literal['entity_position'] | Literal['in_bounding_box']
    offset: float | None = None  # Defaults to 0.
    scale: float | None = None  # Defaults to 1.
