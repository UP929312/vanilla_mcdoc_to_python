"""
Generated from symbols.json for ::java::data::enchantment::effect::PlaySoundEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/PlaySoundEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef
    from vanilla_mcdoc.data.worldgen.FloatProvider import FloatProvider


class PlaySoundEntityEffect(GeneratedModel):
    sound: SoundEventRef | Annotated[list[SoundEventRef], Field(min_length=1, max_length=255)]
    volume: FloatProvider[Annotated[float, Field(ge=1e-05, le=10)]] | Annotated[float, Field(ge=1e-05, le=10)]
    pitch: FloatProvider[Annotated[float, Field(ge=1e-05, le=2)]] | Annotated[float, Field(ge=1e-05, le=2)]
