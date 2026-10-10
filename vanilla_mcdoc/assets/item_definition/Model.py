"""
Generated from symbols.json for ::java::assets::item_definition::Model
Local link to file: vanilla_mcdoc/assets/item_definition/Model.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.ModelTint import ModelTint
    from vanilla_mcdoc.assets.model.ModelRef import ModelRef
    from vanilla_mcdoc.world.entity.display.Transformation import Transformation


class Model(GeneratedModel):
    model: ModelRef
    tints: list[ModelTint] | None = None
    transformation: Transformation | None = None
