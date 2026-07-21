# Generated from symbols.json for ::java::assets::item_definition::UseDuration
from dataclasses import dataclass


@dataclass(kw_only=True)
class UseDuration:
    remaining: bool | None = None  # If true, returns remaining item use ticks. If false, returns item use ticks so far. Defaults to false.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::UseDuration": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If True, returns remaining item use ticks.\nIf False, returns item use ticks so far.\nDefaults to False.",
                "key": "remaining",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

