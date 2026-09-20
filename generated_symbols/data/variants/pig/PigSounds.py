"""
Generated from symbols.json for ::java::data::variants::pig::PigSounds
Local link to file: generated_symbols/data/variants/pig/PigSounds.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef


class PigSounds(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'pig_sound_variant'

    ambient_sound: SoundEventRef
    hurt_sound: SoundEventRef
    death_sound: SoundEventRef
    step_sound: SoundEventRef
    eat_sound: SoundEventRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::pig::PigSounds": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "ambient_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                }
            },
            {
                "kind": "pair",
                "key": "hurt_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                }
            },
            {
                "kind": "pair",
                "key": "death_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                }
            },
            {
                "kind": "pair",
                "key": "step_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                }
            },
            {
                "kind": "pair",
                "key": "eat_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                }
            }
        ]
    }
}

