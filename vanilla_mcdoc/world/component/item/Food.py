"""
Generated from symbols.json for ::java::world::component::item::Food
Local link to file: vanilla_mcdoc/world/component/item/Food.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class Food(GeneratedModel):
    nutrition: Annotated[int, Field(ge=0)]  # Food points/haunches restored when eaten (capped to 20.0).
    saturation: float  # Exact value added to the player's saturation level, capped at whatever the [new] food points value is.
    can_always_eat: bool | None = None  # Whether the item can be eaten when the player's food points/haunches are full. Defaults to `false`
