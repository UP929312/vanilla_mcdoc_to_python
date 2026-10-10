"""
Generated from symbols.json for ::java::data::worldgen::processor_list::Rule
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/Rule.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.processor_list.ProcessorRule import ProcessorRule


class Rule(GeneratedModel):
    rules: list[ProcessorRule]
