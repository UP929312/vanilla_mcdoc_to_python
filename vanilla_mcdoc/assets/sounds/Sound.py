"""
Generated from symbols.json for ::java::assets::sounds::Sound
Local link to file: vanilla_mcdoc/assets/sounds/Sound.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.sounds.SoundType import SoundType


class Sound(GeneratedModel):
    type: SoundType | None = None  # Changes how `name` is interpreted. Defaults to `file`.
    name: Annotated[str, IdSpec(registry='sound')] | Annotated[str, IdSpec(registry='weighed_sound_event')]
    volume: Annotated[float, Field(gt=0)] | None = None  # Defaults to 1.0.
    pitch: Annotated[float, Field(gt=0)] | None = None  # Default is 1.0.
    weight: Annotated[int, Field(ge=1)] | None = None  # Chance that this sound is selected to play. Defaults to 1.
    preload: bool | None = None  # Whether the sound should be loaded when loading the pack instead of when the sound is played. Used by the underwater ambience. Defaults to false.
    stream: bool | None = None  # If true it will be streamed from its file. Sounds longer than a few seconds should enable this to avoid lag. Defaults to false. When false many instances of the sound can be ran at the same time. When true only allows 4 instances (of that type) can be played.
    attenuation_distance: int | None = None  # Modify sound reduction rate based on distance. Defaults to 16.
