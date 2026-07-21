# Generated from symbols.json for ::java::data::worldgen::feature::EndSpike
from dataclasses import dataclass


@dataclass(kw_only=True)
class EndSpike:
    centerX: int
    centerZ: int
    radius: int
    height: int
    guarded: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::EndSpike": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "centerX",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "centerZ",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "radius",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "guarded",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

