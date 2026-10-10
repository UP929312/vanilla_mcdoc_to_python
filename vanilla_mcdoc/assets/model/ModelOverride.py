"""
Generated from symbols.json for ::java::assets::model::ModelOverride
Local link to file: vanilla_mcdoc/assets/model/ModelOverride.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.model.ModelRef import ModelRef
    from vanilla_mcdoc.assets.model.Predicates import Predicates


class ModelOverride(GeneratedModel):
    predicate: dict[Predicates, float]
    model: ModelRef
