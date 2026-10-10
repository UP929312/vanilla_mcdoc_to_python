"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::NoiseGeneratorSettingsRef
Local link to file: vanilla_mcdoc/data/worldgen/noise_settings/NoiseGeneratorSettingsRef.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.worldgen.noise_settings.NoiseGeneratorSettings import NoiseGeneratorSettings
from vanilla_mcdoc.minecraft_types import IdSpec


class NoiseGeneratorSettingsRefStruct(NoiseGeneratorSettings):
    name: Annotated[str, IdSpec(registry='worldgen/noise_settings', definition=True)]


type NoiseGeneratorSettingsRef = Annotated[str, IdSpec(registry='worldgen/noise_settings')] | NoiseGeneratorSettingsRefStruct
