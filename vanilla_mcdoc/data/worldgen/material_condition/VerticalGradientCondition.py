"""
Generated from symbols.json for ::java::data::worldgen::material_condition::VerticalGradientCondition
Local link to file: vanilla_mcdoc/data/worldgen/material_condition/VerticalGradientCondition.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.VerticalAnchor import VerticalAnchor


class VerticalGradientCondition(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    random_name: str
    true_at_and_below: VerticalAnchor
    false_at_and_above: VerticalAnchor
