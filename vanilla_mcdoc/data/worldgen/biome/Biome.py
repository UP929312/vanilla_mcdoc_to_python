"""
Generated from symbols.json for ::java::data::worldgen::biome::Biome
Local link to file: vanilla_mcdoc/data/worldgen/biome/Biome.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.PositionalEnvironmentAttributeMap import PositionalEnvironmentAttributeMap
    from vanilla_mcdoc.data.worldgen.biome.BiomeEffects import BiomeEffects
    from vanilla_mcdoc.data.worldgen.biome.TemperatureModifier import TemperatureModifier
    from vanilla_mcdoc.data.worldgen.carver.CarverListRef import CarverListRef
    from vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef


class Biome(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/biome'

    attributes: PositionalEnvironmentAttributeMap | None = None
    temperature: float
    downfall: float
    has_precipitation: bool
    temperature_modifier: TemperatureModifier | None = None
    effects: BiomeEffects
    carvers: CarverListRef
    features: Annotated[list[list[PlacedFeatureRef] | Annotated[str, IdSpec(registry='worldgen/placed_feature', tags='required')]], Field(max_length=11)]
