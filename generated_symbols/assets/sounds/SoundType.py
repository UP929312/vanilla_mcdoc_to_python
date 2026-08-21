"""
Generated from symbols.json for ::java::assets::sounds::SoundType
Local link to file: generated_symbols/assets/sounds/SoundType.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class SoundType(StrEnum):
    FILE = "file"  # A file.
    SOUNDEVENT = "event"  # An already defined event.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::sounds::SoundType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "A file.",
                "identifier": "File",
                "value": "file"
            },
            {
                "desc": "An already defined event.",
                "identifier": "SoundEvent",
                "value": "event"
            }
        ]
    }
}

