"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::BaseNoiseProvider
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_state_provider/BaseNoiseProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.dimension.biome_source.NoiseParameters import NoiseParameters


class BaseNoiseProvider(GeneratedModel):
    seed: int
    noise: NoiseParameters
    scale: Annotated[float, Field(ge=0)]
