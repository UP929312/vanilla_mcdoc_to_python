"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::RandomSpreadFoliagePlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/RandomSpreadFoliagePlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class RandomSpreadFoliagePlacer(GeneratedModel):
    foliage_height: IntProvider[Annotated[int, Field(ge=1, le=512)]] | Annotated[int, Field(ge=1, le=512)]
    leaf_placement_attempts: Annotated[int, Field(ge=0, le=256)]
