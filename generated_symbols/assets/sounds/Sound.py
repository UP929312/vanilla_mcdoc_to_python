# Generated from symbols.json for ::java::assets::sounds::Sound
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Any

if TYPE_CHECKING:
    from generated_symbols.assets.sounds.SoundType import SoundType


@dataclass(kw_only=True)
class Sound:
    name: Any
    type: SoundType | None = None  # Changes how `name` is interpreted. Defaults to `file`.
    volume: Annotated[float, 'Range | Min `0` and above | inclusive'] | None = None  # Defaults to 1.0.
    pitch: Annotated[float, 'Range | Min `0` and above | inclusive'] | None = None  # Default is 1.0.
    weight: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Chance that this sound is selected to play. Defaults to 1.
    preload: bool | None = None  # Whether the sound should be loaded when loading the pack instead of when the sound is played. Used by the underwater ambience. Defaults to false.
    stream: bool | None = None  # If true it will be streamed from its file. Sounds longer than a few seconds should enable this to avoid lag. Defaults to false. When false many instances of the sound can be ran at the same time. When true only allows 4 instances (of that type) can be played.
    attenuation_distance: int | None = None  # Modify sound reduction rate based on distance. Defaults to 16.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::sounds::Sound": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Changes how `name` is interpreted. Defaults to `file`.",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::sounds::SoundType"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "name",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:sound_type"
                }
            },
            {
                "kind": "pair",
                "desc": "Defaults to 1.0.",
                "key": "volume",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 2,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Default is 1.0.",
                "key": "pitch",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 2,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Chance that this sound is selected to play. Defaults to 1.",
                "key": "weight",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the sound should be loaded when loading the pack instead of when the sound is played. Used by the underwater ambience. Defaults to False.",
                "key": "preload",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If True it will be streamed from its file. Sounds longer than a few seconds should enable this to avoid lag. Defaults to False.\nWhen False many instances of the sound can be ran at the same time. When True only allows 4 instances (of that type) can be played.",
                "key": "stream",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Modify sound reduction rate based on distance. Defaults to 16.",
                "key": "attenuation_distance",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

