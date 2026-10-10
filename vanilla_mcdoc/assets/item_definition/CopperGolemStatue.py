"""
Generated from symbols.json for ::java::assets::item_definition::CopperGolemStatue
Local link to file: vanilla_mcdoc/assets/item_definition/CopperGolemStatue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.CopperGolemStatuePose import CopperGolemStatuePose


class CopperGolemStatue(GeneratedModel):
    pose: CopperGolemStatuePose
    texture: str
