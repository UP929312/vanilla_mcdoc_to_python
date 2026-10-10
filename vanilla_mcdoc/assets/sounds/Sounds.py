"""
Generated from symbols.json for ::java::assets::sounds::Sounds
Local link to file: vanilla_mcdoc/assets/sounds/Sounds.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.sounds.SoundEventRegistration import SoundEventRegistration


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
