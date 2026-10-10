"""
Generated from symbols.json for ::java::world::component::item::ItemDamageFunction
Local link to file: vanilla_mcdoc/world/component/item/ItemDamageFunction.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class ItemDamageFunction(GeneratedModel):
    threshold: Annotated[float, Field(ge=0)]  # Minimum amount of damage dealt by the attack before this item damage is applied to the item.
    base: float  # Constant amount of damage applied to the item, if `threshold` is passed.
    factor: float  # Fraction of the dealt damage that should be applied to the item, if `threshold` is passed.
