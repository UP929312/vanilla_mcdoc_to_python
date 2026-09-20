"""
Generated from symbols.json for ::java::data::variants::SoundVariant
Local link to file: generated_symbols/data/variants/SoundVariant.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from generated_symbols.base import GeneratedModel


T = TypeVar('T')

class SoundVariant(GeneratedModel, Generic[T]):
    adult_sounds: T
    baby_sounds: T


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::SoundVariant": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "adult_sounds",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::variants::T"
                    }
                },
                {
                    "kind": "pair",
                    "key": "baby_sounds",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::variants::T"
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::variants::T"
            }
        ]
    }
}

