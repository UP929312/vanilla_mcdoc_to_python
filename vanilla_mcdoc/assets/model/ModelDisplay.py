"""
Generated from symbols.json for ::java::assets::model::ModelDisplay
Local link to file: generated_symbols/assets/model/ModelDisplay.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.model.CustomizableItemDisplayContext import CustomizableItemDisplayContext


class ModelDisplayValueStruct(GeneratedModel):
    rotation: tuple[float, float, float] | None = None
    translation: tuple[Annotated[float, Field(ge=-80, le=80)], Annotated[float, Field(ge=-80, le=80)], Annotated[float, Field(ge=-80, le=80)]] | None = None
    scale: tuple[Annotated[float, Field(ge=-4, le=4)], Annotated[float, Field(ge=-4, le=4)], Annotated[float, Field(ge=-4, le=4)]] | None = None


type ModelDisplay = dict[CustomizableItemDisplayContext, ModelDisplayValueStruct]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::model::ModelDisplay": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::assets::model::CustomizableItemDisplayContext"
                },
                "type": {
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
        ]
    }
}
