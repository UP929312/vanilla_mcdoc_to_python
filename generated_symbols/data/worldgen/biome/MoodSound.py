# Generated from symbols.json for ::java::data::worldgen::biome::MoodSound
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef


@dataclass(kw_only=True)
class MoodSound:
    sound: SoundEventRef
    tick_delay: int
    block_search_extent: int
    offset: float


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::biome::MoodSound": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                }
            },
            {
                "kind": "pair",
                "key": "tick_delay",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "block_search_extent",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "offset",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}

