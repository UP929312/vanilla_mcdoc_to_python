# Generated from symbols.json for ::java::assets::shader::post::AuxTarget
from dataclasses import dataclass


@dataclass(kw_only=True)
class AuxTarget:
    name: str
    id: str
    width: int | None = None
    height: int | None = None
    bilinear: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::shader::post::AuxTarget": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "name",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "key": "id",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "key": "width",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "bilinear",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

