"""
Generated from symbols.json for ::java::data::variants::wolf::WolfSounds
Local link to file: generated_symbols/data/variants/wolf/WolfSounds.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef


@dataclass(kw_only=True)
class WolfSounds:
    __resource_dir__: ClassVar[str] = 'wolf_sound_variant'

    ambient_sound: SoundEventRef
    death_sound: SoundEventRef
    growl_sound: SoundEventRef
    hurt_sound: SoundEventRef
    pant_sound: SoundEventRef
    whine_sound: SoundEventRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::wolf::WolfSounds": {
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
                "key": "death_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                }
            },
            {
                "kind": "pair",
                "key": "growl_sound",
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
                "key": "pant_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                }
            },
            {
                "kind": "pair",
                "key": "whine_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                }
            }
        ]
    }
}

