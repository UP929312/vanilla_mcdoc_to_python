# Generated from symbols.json for ::java::data::enchantment::effect::PlaySoundEntityEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.data.worldgen.FloatProvider import FloatProvider


@dataclass(kw_only=True)
class PlaySoundEntityEffect:
    sound: SoundEventRef | Annotated[list[SoundEventRef], 'Length = 1-255 (both inclusive)']
    volume: FloatProvider[Annotated[float, 'Range | `1e-05`-`10` | both inclusive']] | Annotated[float, 'Range | `1e-05`-`10` | both inclusive']
    pitch: FloatProvider[Annotated[float, 'Range | `1e-05`-`2` | both inclusive']] | Annotated[float, 'Range | `1e-05`-`2` | both inclusive']


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

