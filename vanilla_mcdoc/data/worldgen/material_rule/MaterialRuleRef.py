"""
Generated from symbols.json for ::java::data::worldgen::material_rule::MaterialRuleRef
Local link to file: vanilla_mcdoc/data/worldgen/material_rule/MaterialRuleRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.material_rule.MaterialRule import MaterialRule
    from vanilla_mcdoc.registry.KnownMaterialRuleId import KnownMaterialRuleId


type MaterialRuleRef = Annotated[str, IdSpec(registry='material_rule')] | KnownMaterialRuleId | MaterialRule
