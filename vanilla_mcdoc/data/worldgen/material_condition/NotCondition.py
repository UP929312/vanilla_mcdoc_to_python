"""
Generated from symbols.json for ::java::data::worldgen::material_condition::NotCondition
Local link to file: vanilla_mcdoc/data/worldgen/material_condition/NotCondition.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.material_condition.MaterialConditionRef import MaterialConditionRef


class NotCondition(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    invert: MaterialConditionRef
