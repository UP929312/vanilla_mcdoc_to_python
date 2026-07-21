# Generated from symbols.json for ::java::assets::sounds::Sounds
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.sounds.SoundEventRegistration import SoundEventRegistration


type Sounds = dict[str, SoundEventRegistration]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::sounds::Sounds": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string"
                },
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::sounds::SoundEventRegistration"
                }
            }
        ]
    }
}

