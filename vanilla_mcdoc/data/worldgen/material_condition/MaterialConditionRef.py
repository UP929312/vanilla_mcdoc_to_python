"""
Generated from symbols.json for ::java::data::worldgen::material_condition::MaterialConditionRef
Local link to file: vanilla_mcdoc/data/worldgen/material_condition/MaterialConditionRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.material_condition.MaterialCondition import MaterialCondition
    from vanilla_mcdoc.registry.KnownMaterialConditionId import KnownMaterialConditionId


type MaterialConditionRef = Annotated[str, IdSpec(registry='material_condition')] | KnownMaterialConditionId | MaterialCondition
