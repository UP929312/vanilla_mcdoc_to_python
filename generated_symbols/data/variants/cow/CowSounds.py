"""
Generated from symbols.json for ::java::data::variants::cow::CowSounds
Local link to file: generated_symbols/data/variants/cow/CowSounds.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef


class CowSounds(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'cow_sound_variant'

    ambient_sound: SoundEventRef
    hurt_sound: SoundEventRef
    death_sound: SoundEventRef
    step_sound: SoundEventRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::cow::CowSounds": {
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
            }
        ]
    }
}
