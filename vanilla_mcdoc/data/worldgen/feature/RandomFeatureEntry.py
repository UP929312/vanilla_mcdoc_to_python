"""
Generated from symbols.json for ::java::data::worldgen::feature::RandomFeatureEntry
Local link to file: vanilla_mcdoc/data/worldgen/feature/RandomFeatureEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.FeatureRef import FeatureRef


class RandomFeatureEntry(GeneratedModel):
    chance: Annotated[float, Field(ge=0, le=1)]
    feature: FeatureRef
