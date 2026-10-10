"""
Generated from symbols.json for ::java::world::component::block::SignText
Local link to file: vanilla_mcdoc/world/component/block/SignText.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.DyeColor import DyeColor
    from vanilla_mcdoc.world.component.block.SignLines import SignLines


class SignText(GeneratedModel):
    messages: SignLines
    filtered_messages: SignLines | None = None  # Shown to players with the profanity filter enabled on Realms.
    color: DyeColor | None = None
    has_glowing_text: bool | None = None
