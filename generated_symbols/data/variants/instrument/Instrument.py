# Generated from symbols.json for ::java::data::variants::instrument::Instrument
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class Instrument:
    sound_event: SoundEventRef
    range: Annotated[float, 'Range | Min `0` and above | inclusive']  # Maximum range in blocks that the sound can be heard
    use_duration: Annotated[float, 'Range | Min `0` and above | inclusive']  # Duration of use in seconds, used as item cooldown
    description: Text
    durability_damage: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::instrument::Instrument": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "sound_event",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                }
            },
            {
                "kind": "pair",
                "desc": "Maximum range in blocks that the sound can be heard",
                "key": "range",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 2,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Duration of use in seconds, used as item cooldown",
                "key": "use_duration",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "float",
                            "valueRange": {
                                "kind": 2,
                                "min": 0
                            },
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "float",
                            "valueRange": {
                                "kind": 0,
                                "min": 0
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
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
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "durability_damage",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "description",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                }
            }
        ]
    }
}

