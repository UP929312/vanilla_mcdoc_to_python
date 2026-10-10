"""
Generated from symbols.json for ::java::data::util::WeightedSoundEvent
Local link to file: vanilla_mcdoc/data/util/WeightedSoundEvent.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class WeightedSoundEvent(GeneratedModel):
    sound_id: Annotated[str, IdSpec(registry='weighed_sound_event', empty='allowed')]
    range: float | None = None  # Range in blocks. If the player is further than this range from the source of the sound, the sound will be inaudible. If omitted, the sound will have a variable range.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::WeightedSoundEvent": {
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
}
