"""
Generated from symbols.json for ::java::assets::model::ItemDisplayContext
Local link to file: generated_symbols/assets/model/ItemDisplayContext.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class ItemDisplayContext(StrEnum):
    NONE = "none"
    FIRSTPERSONRIGHTHAND = "firstperson_righthand"
    FIRSTPERSONLEFTHAND = "firstperson_lefthand"
    THIRDPERSONRIGHTHAND = "thirdperson_righthand"
    THIRDPERSONLEFTHAND = "thirdperson_lefthand"
    GUI = "gui"
    HEAD = "head"
    GROUND = "ground"
    FIXED = "fixed"
    ONSHELF = "on_shelf"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::model::ItemDisplayContext": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "None",
                "value": "none"
            },
            {
                "identifier": "FirstPersonRighthand",
                "value": "firstperson_righthand"
            },
            {
                "identifier": "FirstPersonLefthand",
                "value": "firstperson_lefthand"
            },
            {
                "identifier": "ThirdPersonRighthand",
                "value": "thirdperson_righthand"
            },
            {
                "identifier": "ThirdPersonLefthand",
                "value": "thirdperson_lefthand"
            },
            {
                "identifier": "Gui",
                "value": "gui"
            },
            {
                "identifier": "Head",
                "value": "head"
            },
            {
                "identifier": "Ground",
                "value": "ground"
            },
            {
                "identifier": "Fixed",
                "value": "fixed"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.9"
                            }
                        }
                    }
                ],
                "identifier": "OnShelf",
                "value": "on_shelf"
            }
        ]
    }
}

