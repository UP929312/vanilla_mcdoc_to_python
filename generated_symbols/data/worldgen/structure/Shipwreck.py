# Generated from symbols.json for ::java::data::worldgen::structure::Shipwreck
from dataclasses import dataclass


@dataclass(kw_only=True)
class Shipwreck:
    is_beached: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::Shipwreck": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "is_beached",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

