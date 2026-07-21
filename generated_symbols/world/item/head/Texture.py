# Generated from symbols.json for ::java::world::item::head::Texture
from dataclasses import dataclass


@dataclass(kw_only=True)
class Texture:
    Signature: str | None = None
    Value: str | None = None  # Base64 encoded JSON value of the texture index.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::head::Texture": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "Signature",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Base64 encoded JSON value of the texture index.",
                "key": "Value",
                "type": {
                    "kind": "string"
                },
                "optional": True
            }
        ]
    }
}

