"""
Generated from symbols.json for ::java::world::component::item::TooltipDisplay
Local link to file: vanilla_mcdoc/world/component/item/TooltipDisplay.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class TooltipDisplay(GeneratedModel):
    hide_tooltip: bool | None = None  # If `true`, the item will have no tooltip when hovered. Defaults to `false`.
    hidden_components: list[Annotated[str, IdSpec(registry='data_component_type')]] | None = None  # List of components that should be hidden in the item tooltip.
