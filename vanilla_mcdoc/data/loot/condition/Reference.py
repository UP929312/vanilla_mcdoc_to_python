"""
Generated from symbols.json for ::java::data::loot::condition::Reference
Local link to file: vanilla_mcdoc/data/loot/condition/Reference.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class Reference(GeneratedModel):
    name: Annotated[str, IdSpec(registry='predicate')]  # A cyclic reference causes a parsing failure.
