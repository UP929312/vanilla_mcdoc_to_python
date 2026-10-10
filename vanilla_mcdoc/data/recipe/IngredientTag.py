"""
Generated from symbols.json for ::java::data::recipe::IngredientTag
Local link to file: vanilla_mcdoc/data/recipe/IngredientTag.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownItemId import KnownItemId


class IngredientTag(GeneratedModel):
    tag: Annotated[str, IdSpec(registry='item', tags='implicit')] | KnownItemId
