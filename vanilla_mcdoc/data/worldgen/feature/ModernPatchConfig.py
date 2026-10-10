"""
Generated from symbols.json for ::java::data::worldgen::feature::ModernPatchConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/ModernPatchConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.FeatureRef import FeatureRef


class ModernPatchConfig(GeneratedModel):
    xz_spread: Annotated[int, Field(ge=0)] | None = None  # Defaults to 7.
    y_spread: Annotated[int, Field(ge=0)] | None = None  # Defaults to 3.
    feature: FeatureRef
