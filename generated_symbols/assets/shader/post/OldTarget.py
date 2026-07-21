# Generated from symbols.json for ::java::assets::shader::post::OldTarget
from dataclasses import dataclass


@dataclass(kw_only=True)
class OldTarget:
    name: str
    width: int | None = None
    height: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::shader::post::OldTarget": {
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
            }
        ]
    }
}

