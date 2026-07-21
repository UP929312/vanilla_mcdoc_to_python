# Generated from symbols.json for ::java::data::variants::cow::CowSounds
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef


@dataclass(kw_only=True)
class CowSounds:
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

