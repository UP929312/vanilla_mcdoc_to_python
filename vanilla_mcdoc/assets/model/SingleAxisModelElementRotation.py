"""
Generated from symbols.json for ::java::assets::model::SingleAxisModelElementRotation
Local link to file: vanilla_mcdoc/assets/model/SingleAxisModelElementRotation.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.assets.model.ModelElementRotationBase import ModelElementRotationBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.direction.Axis import Axis


class SingleAxisModelElementRotation(ModelElementRotationBase):
    axis: Axis
    angle: float
