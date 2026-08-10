"""
Generated from symbols.json for ::java::world::block::head::Texture
Local link to file: generated_symbols/world/block/head/Texture.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass


@dataclass(kw_only=True)
class Texture:
    Signature: str | None = None
    Value: str | None = None  # Base64 encoded JSON value of the texture index.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::head::Texture": {
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

