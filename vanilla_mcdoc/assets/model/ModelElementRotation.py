"""
Generated from symbols.json for ::java::assets::model::ModelElementRotation
Local link to file: vanilla_mcdoc/assets/model/ModelElementRotation.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from pydantic import Field

from vanilla_mcdoc.assets.model.ModelElementRotationBase import ModelElementRotationBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.direction.Axis import Axis


class ModelElementRotationStruct1(ModelElementRotationBase):
    axis: Axis
    angle: float


class ModelElementRotationStruct2(ModelElementRotationBase):
    __pydantic_extra__: dict[Axis, float] = Field(init=False)  # type: ignore[assignment]


type ModelElementRotation = ModelElementRotationStruct1 | ModelElementRotationStruct2
