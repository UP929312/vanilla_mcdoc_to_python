# Generated from symbols.json for ::java::data::util::RandomValueBounds
from dataclasses import dataclass


@dataclass(kw_only=True)
class RandomValueBoundsStruct1:
    min: float
    max: float

type RandomValueBounds = float | RandomValueBoundsStruct1


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

