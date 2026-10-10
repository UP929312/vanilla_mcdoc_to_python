"""
Generated from symbols.json for ::java::world::component::item::VillagerFood
Local link to file: vanilla_mcdoc/world/component/item/VillagerFood.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class VillagerFood(GeneratedModel):
    nutrition: Annotated[int, Field(ge=1)]  # How much hunger the item satiates in the Villager once eaten.
