# Generated from symbols.json for ::java::assets::model::ModelElementRotationBase
from dataclasses import dataclass


@dataclass(kw_only=True)
class ModelElementRotationBase:
    origin: tuple[float, float, float]
    rescale: bool | None = None  # Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::model::ModelElementRotationBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "origin",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Defaults to `False`.",
                "key": "rescale",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

