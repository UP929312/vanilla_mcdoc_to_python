"""
Generated from symbols.json for ::java::assets::item_definition::StandingSign
Local link to file: vanilla_mcdoc/assets/item_definition/StandingSign.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.StandingSignAttachment import StandingSignAttachment
    from vanilla_mcdoc.assets.item_definition.WoodType import WoodType


class StandingSign(GeneratedModel):
    wood_type: WoodType
    texture: Annotated[str, IdSpec(registry='texture', path='entity/signs/')] | None = None
    attachement: StandingSignAttachment | None = None  # There is an extra "e" in the field name. See MC-307498.  Defaults to `ground`.
