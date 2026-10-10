"""
Generated from symbols.json for ::java::world::component::item::SwingAnimation
Local link to file: vanilla_mcdoc/world/component/item/SwingAnimation.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.SwingAnimationType import SwingAnimationType


class SwingAnimation(GeneratedModel):
    type: SwingAnimationType | None = None  # The animation type to play when attacking or interacting using this item. Defaults to `whack`.
    duration: Annotated[int, Field(ge=0)] | None = None  # The animation duration in ticks. Defaults to 6
