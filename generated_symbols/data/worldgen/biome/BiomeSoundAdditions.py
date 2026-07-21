# Generated from symbols.json for ::java::data::worldgen::biome::BiomeSoundAdditions
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef


@dataclass(kw_only=True)
class BiomeSoundAdditions:
    sound: SoundEventRef
    tick_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::biome::BiomeSoundAdditions": {
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
                "key": "tick_chance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}

