"""
Generated from symbols.json for ::java::data::variants::chicken::ChickenSounds
Local link to file: generated_symbols/data/variants/chicken/ChickenSounds.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef


@dataclass(kw_only=True)
class ChickenSounds:
    __resource_dir__: ClassVar[str] = 'chicken_sound_variant'

    ambient_sound: SoundEventRef
    hurt_sound: SoundEventRef
    death_sound: SoundEventRef
    step_sound: SoundEventRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::chicken::ChickenSounds": {
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

