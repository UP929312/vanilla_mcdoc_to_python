"""
Generated from symbols.json for ::java::data::worldgen::processor_list::CompositeMatch
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/CompositeMatch.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.processor_list.RuleTest import RuleTest


class CompositeMatch(GeneratedModel):
    rules: list[RuleTest]
