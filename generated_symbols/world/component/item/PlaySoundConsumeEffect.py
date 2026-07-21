# Generated from symbols.json for ::java::world::component::item::PlaySoundConsumeEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef


@dataclass(kw_only=True)
class PlaySoundConsumeEffect:
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

