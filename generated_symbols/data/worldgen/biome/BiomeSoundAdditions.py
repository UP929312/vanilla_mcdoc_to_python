"""
Generated from symbols.json for ::java::data::worldgen::biome::BiomeSoundAdditions
Local link to file: generated_symbols/data/worldgen/biome/BiomeSoundAdditions.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef


class BiomeSoundAdditions(GeneratedModel):
    sound: SoundEventRef
    tick_chance: Annotated[float, Field(ge=0, le=1)]


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

