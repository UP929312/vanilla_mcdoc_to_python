"""
Generated from symbols.json for ::java::data::worldgen::feature::RandomPatchConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/RandomPatchConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.FeatureRef import FeatureRef


class RandomPatchConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    tries: Annotated[int, Field(ge=1)] | None = None  # How many attempts will be made to find a placement. Defaults to 128.
    xz_spread: Annotated[int, Field(ge=0)] | None = None  # Defaults to 7.
    y_spread: Annotated[int, Field(ge=0)] | None = None  # Defaults to 3.
    feature: FeatureRef
