"""
Generated from symbols.json for ::java::data::worldgen::feature::EndSpike
Local link to file: vanilla_mcdoc/data/worldgen/feature/EndSpike.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class EndSpike(GeneratedModel):
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
