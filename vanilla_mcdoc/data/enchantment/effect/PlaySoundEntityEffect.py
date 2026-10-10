"""
Generated from symbols.json for ::java::data::enchantment::effect::PlaySoundEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/PlaySoundEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef
    from vanilla_mcdoc.data.worldgen.FloatProvider import FloatProvider


class PlaySoundEntityEffect(GeneratedModel):
    sound: SoundEventRef | Annotated[list[SoundEventRef], Field(min_length=1, max_length=255)]
    volume: FloatProvider[Annotated[float, Field(ge=1e-05, le=10)]] | Annotated[float, Field(ge=1e-05, le=10)]
    pitch: FloatProvider[Annotated[float, Field(ge=1e-05, le=2)]] | Annotated[float, Field(ge=1e-05, le=2)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::PlaySoundEntityEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "sound",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::util::SoundEventRef"
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::util::SoundEventRef"
                            },
                            "lengthRange": {
                                "kind": 0,
                                "min": 1,
                                "max": 255
                            },
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
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "volume",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float",
                            "valueRange": {
                                "kind": 0,
                                "min": 1e-05,
                                "max": 10
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "pitch",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float",
                            "valueRange": {
                                "kind": 0,
                                "min": 1e-05,
                                "max": 2
                            }
                        }
                    ]
                }
            }
        ]
    }
}
