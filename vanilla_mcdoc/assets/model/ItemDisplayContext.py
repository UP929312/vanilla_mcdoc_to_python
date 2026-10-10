"""
Generated from symbols.json for ::java::assets::model::ItemDisplayContext
Local link to file: vanilla_mcdoc/assets/model/ItemDisplayContext.py
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
