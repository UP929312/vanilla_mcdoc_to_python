# Generated from symbols.json for ::java::data::variants::SoundVariant
from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar('T')

@dataclass(kw_only=True)
class SoundVariant(Generic[T]):
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

