# Generated from symbols.json for ::java::assets::model::ModelDisplay
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.assets.model.CustomizableItemDisplayContext import CustomizableItemDisplayContext


type ModelDisplay = dict[CustomizableItemDisplayContext, Any]


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

