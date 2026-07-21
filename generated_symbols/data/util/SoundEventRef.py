# Generated from symbols.json for ::java::data::util::SoundEventRef
from dataclasses import dataclass


@dataclass(kw_only=True)
class SoundEventRefStruct1:
    sound_id: str
    range: float | None = None  # Range in blocks. If the player is further than this range from the source of the sound, the sound will be inaudible. If omitted, the sound will have a variable range.

type SoundEventRef = str | SoundEventRefStruct1


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::SoundEventRef": {
        "kind": "union",
        "members": [
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "sound_event"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19.3"
                            }
                        }
                    },
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "weighed_sound_event"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "sound_id",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "weighed_sound_event"
                                                }
                                            },
                                            "empty": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "kind": "pair",
                        "desc": "Range in blocks. If the player is further than this range from the source of the sound, the sound will be inaudible. If omitted, the sound will have a variable range.",
                        "key": "range",
                        "type": {
                            "kind": "float"
                        },
                        "optional": True
                    }
                ],
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19.3"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

