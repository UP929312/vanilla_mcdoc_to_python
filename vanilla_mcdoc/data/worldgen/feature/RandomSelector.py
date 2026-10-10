"""
Generated from symbols.json for ::java::data::worldgen::feature::RandomSelector
Local link to file: vanilla_mcdoc/data/worldgen/feature/RandomSelector.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.FeatureRef import FeatureRef


class FeaturesStruct(GeneratedModel):
    chance: Annotated[float, Field(ge=0, le=1)]
    feature: FeatureRef


class RandomSelector(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    features: list[FeaturesStruct]
    default: FeatureRef
