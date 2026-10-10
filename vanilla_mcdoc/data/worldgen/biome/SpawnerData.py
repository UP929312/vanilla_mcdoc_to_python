"""
Generated from symbols.json for ::java::data::worldgen::biome::SpawnerData
Local link to file: vanilla_mcdoc/data/worldgen/biome/SpawnerData.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class SpawnerData(GeneratedModel):
    type: Annotated[str, IdSpec(registry='entity_type')]
    count: IntProvider[int] | int
