"""
Generated from symbols.json for ::java::data::util::RandomValueBounds
Local link to file: vanilla_mcdoc/data/util/RandomValueBounds.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class RandomValueBoundsStruct(GeneratedModel):
    min: float
    max: float


type RandomValueBounds = float | RandomValueBoundsStruct


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::RandomValueBounds": {
        "kind": "union",
        "members": [
            {
                "kind": "float"
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "min",
                        "type": {
                            "kind": "float"
                        }
                    },
                    {
                        "kind": "pair",
                        "key": "max",
                        "type": {
                            "kind": "float"
                        }
                    }
                ]
            }
        ]
    }
}
