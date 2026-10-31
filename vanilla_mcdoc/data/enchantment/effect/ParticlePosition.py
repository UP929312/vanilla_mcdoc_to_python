"""
Generated from symbols.json for ::java::data::enchantment::effect::ParticlePosition
Local link to file: vanilla_mcdoc/data/enchantment/effect/ParticlePosition.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ParticlePositionType import ParticlePositionType


class ParticlePositionUnknown(GeneratedModel):
    type: ParticlePositionType
    offset: float | None = None  # Defaults to 0.
    scale: float | None = None  # Defaults to 1.


class ParticlePositionEntityPosition(GeneratedModel):
    type: Literal['minecraft:entity_position', 'entity_position'] = 'minecraft:entity_position'
    offset: float | None = None  # Defaults to 0.
    scale: Annotated[float, Field(ge=1.0, le=1.0)] | None = 1.0  # Defaults to 1.


type ParticlePosition = ParticlePositionUnknown | ParticlePositionEntityPosition
