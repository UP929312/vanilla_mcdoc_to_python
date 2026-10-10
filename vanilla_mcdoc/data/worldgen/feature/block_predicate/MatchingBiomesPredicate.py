"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::MatchingBiomesPredicate
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_predicate/MatchingBiomesPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class MatchingBiomesPredicate(GeneratedModel):
    biomes: Annotated[str, IdSpec(registry='biome', tags='allowed')] | list[Annotated[str, IdSpec(registry='biome')]]
