# Generated from symbols.json for ::java::assets::item_definition::UseCycle
from dataclasses import dataclass


@dataclass(kw_only=True)
class UseCycle:
    period: float | None = None  # returns remaining item use ticks modulo `period`. Defaults to 1.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::UseCycle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "returns remaining item use ticks modulo `period`.\nDefaults to 1.",
                "key": "period",
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ]
    }
}

