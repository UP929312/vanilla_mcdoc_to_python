"""
Generated from symbols.json for ::java::data::variants::instrument::Instrument
Local link to file: generated_symbols/data/variants/instrument/Instrument.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.util.text.Text import Text


class Instrument(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'instrument'

    sound_event: SoundEventRef
    range: Annotated[float, Field(gt=0)]  # Maximum range in blocks that the sound can be heard
    use_duration: Annotated[float, Field(ge=0)]  # Duration of use in seconds, used as item cooldown
    durability_damage: Annotated[int, Field(ge=0)] | None = None
    description: Text


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
