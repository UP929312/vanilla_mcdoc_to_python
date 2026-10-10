"""
Generated from symbols.json for ::java::world::component::item::PlaySoundConsumeEffect
Local link to file: vanilla_mcdoc/world/component/item/PlaySoundConsumeEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class PlaySoundConsumeEffect(GeneratedModel):
    sound: SoundEventRef
