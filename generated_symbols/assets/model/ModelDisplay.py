"""
Generated from symbols.json for ::java::assets::model::ModelDisplay
Local link to file: generated_symbols/assets/model/ModelDisplay.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.assets.model.CustomizableItemDisplayContext import CustomizableItemDisplayContext


@dataclass(kw_only=True)
class ModelDisplayValueStruct:
    rotation: tuple[float, float, float] | None = None
    translation: tuple[Annotated[float, 'Range | `-80`-`80` | both inclusive'], Annotated[float, 'Range | `-80`-`80` | both inclusive'], Annotated[float, 'Range | `-80`-`80` | both inclusive']] | None = None
    scale: tuple[Annotated[float, 'Range | `-4`-`4` | both inclusive'], Annotated[float, 'Range | `-4`-`4` | both inclusive'], Annotated[float, 'Range | `-4`-`4` | both inclusive']] | None = None


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

