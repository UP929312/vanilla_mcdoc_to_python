"""
Generated from symbols.json for ::java::data::worldgen::feature::RandomBooleanSelector
Local link to file: vanilla_mcdoc/data/worldgen/feature/RandomBooleanSelector.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.FeatureRef import FeatureRef


class RandomBooleanSelector(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    feature_false: FeatureRef
    feature_true: FeatureRef
