"""
Generated from symbols.json for ::java::data::worldgen::biome::BiomeMusic
Local link to file: generated_symbols/data/worldgen/biome/BiomeMusic.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef


class BiomeMusic(GeneratedModel):
    sound: SoundEventRef
    min_delay: Annotated[int, Field(ge=0)]
    max_delay: Annotated[int, Field(ge=0)]
    replace_current_music: bool | None = None  # Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::biome::BiomeMusic": {
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
                "key": "min_delay",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "key": "max_delay",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "replace_current_music",
                            "type": {
                                "kind": "boolean"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Defaults to `False`.",
                            "key": "replace_current_music",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        }
                    ]
                }
            }
        ]
    }
}
