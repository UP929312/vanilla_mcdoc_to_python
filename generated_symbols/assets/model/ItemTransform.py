"""
Generated from symbols.json for ::java::assets::model::ItemTransform
Local link to file: generated_symbols/assets/model/ItemTransform.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field


class ItemTransform(GeneratedModel):
    rotation: tuple[float, float, float] | None = None
    translation: tuple[Annotated[float, Field(ge=-80, le=80)], Annotated[float, Field(ge=-80, le=80)], Annotated[float, Field(ge=-80, le=80)]] | None = None
    scale: tuple[Annotated[float, Field(ge=-4, le=4)], Annotated[float, Field(ge=-4, le=4)], Annotated[float, Field(ge=-4, le=4)]] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::model::ItemTransform": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "rotation",
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
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "translation",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float",
                        "valueRange": {
                            "kind": 0,
                            "min": -80,
                            "max": 80
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "scale",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float",
                        "valueRange": {
                            "kind": 0,
                            "min": -4,
                            "max": 4
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            }
        ]
    }
}

