"""
Generated from symbols.json for ::java::assets::item_definition::HangingSign
Local link to file: vanilla_mcdoc/assets/item_definition/HangingSign.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.HangingSignAttachment import HangingSignAttachment
    from vanilla_mcdoc.assets.item_definition.WoodType import WoodType


class HangingSign(GeneratedModel):
    wood_type: WoodType
    texture: Annotated[str, IdSpec(registry='texture', path='entity/signs/hanging/')] | None = None
    attachment: HangingSignAttachment | None = None  # Defaults to `ceiling_middle`.
