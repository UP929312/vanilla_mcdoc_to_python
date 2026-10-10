"""
Generated from symbols.json for ::java::assets::item_definition::Composite
Local link to file: vanilla_mcdoc/assets/item_definition/Composite.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.ItemModel import ItemModel
    from vanilla_mcdoc.world.entity.display.Transformation import Transformation


class Composite(GeneratedModel):
    models: list[ItemModel]
    transformation: Transformation | None = None
