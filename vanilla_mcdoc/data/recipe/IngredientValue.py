"""
Generated from symbols.json for ::java::data::recipe::IngredientValue
Local link to file: vanilla_mcdoc/data/recipe/IngredientValue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownItemId import KnownItemId


class IngredientValueStruct1(GeneratedModel):
    item: Annotated[str, IdSpec(registry='item')] | KnownItemId


class IngredientValueStruct2(GeneratedModel):
    tag: Annotated[str, IdSpec(registry='item', tags='implicit')] | KnownItemId


type IngredientValue = IngredientValueStruct1 | IngredientValueStruct2
