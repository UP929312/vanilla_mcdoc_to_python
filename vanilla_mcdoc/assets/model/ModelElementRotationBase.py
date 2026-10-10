"""
Generated from symbols.json for ::java::assets::model::ModelElementRotationBase
Local link to file: vanilla_mcdoc/assets/model/ModelElementRotationBase.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class ModelElementRotationBase(GeneratedModel):
    origin: tuple[float, float, float]
    rescale: bool | None = None  # Defaults to `false`.
