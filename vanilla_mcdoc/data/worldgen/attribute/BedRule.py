"""
Generated from symbols.json for ::java::data::worldgen::attribute::BedRule
Local link to file: vanilla_mcdoc/data/worldgen/attribute/BedRule.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.BedRuleType import BedRuleType
    from vanilla_mcdoc.util.text.Text import Text


class BedRule(GeneratedModel):
    can_sleep: BedRuleType
    can_set_spawn: BedRuleType
    destroy_on_use: bool | None = None
    destroy_on_leave: bool | None = None
    error_message: Text | None = None
