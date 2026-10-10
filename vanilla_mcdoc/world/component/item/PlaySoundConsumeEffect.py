"""
Generated from symbols.json for ::java::world::component::item::PlaySoundConsumeEffect
Local link to file: generated_symbols/world/component/item/PlaySoundConsumeEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef


class PlaySoundConsumeEffect(GeneratedModel):
    sound: SoundEventRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::PlaySoundConsumeEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                }
            }
        ]
    }
}
