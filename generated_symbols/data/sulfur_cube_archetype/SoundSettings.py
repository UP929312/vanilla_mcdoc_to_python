# Generated from symbols.json for ::java::data::sulfur_cube_archetype::SoundSettings
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef


@dataclass(kw_only=True)
class SoundSettings:
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

