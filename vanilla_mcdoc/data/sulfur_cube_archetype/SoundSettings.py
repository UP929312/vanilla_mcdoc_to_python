"""
Generated from symbols.json for ::java::data::sulfur_cube_archetype::SoundSettings
Local link to file: vanilla_mcdoc/data/sulfur_cube_archetype/SoundSettings.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class SoundSettings(GeneratedModel):
    hit_sound: SoundEventRef
    push_sound: SoundEventRef
    push_sound_impulse_threshold: float  # Minimum impact speed required to trigger the sound.
    push_sound_cooldown: float  # Cooldown in seconds for the sound effect.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::sulfur_cube_archetype::SoundSettings": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "hit_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                }
            },
            {
                "kind": "pair",
                "key": "push_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                }
            },
            {
                "kind": "pair",
                "desc": "Minimum impact speed required to trigger the sound.",
                "key": "push_sound_impulse_threshold",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "desc": "Cooldown in seconds for the sound effect.",
                "key": "push_sound_cooldown",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}
