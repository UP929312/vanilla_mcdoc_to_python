"""
Generated from symbols.json for ::java::data::variants::SpawnCondition
Local link to file: vanilla_mcdoc/data/variants/SpawnCondition.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.data.variants.BiomeCheck import BiomeCheck
from vanilla_mcdoc.data.variants.MoonBrightnessCheck import MoonBrightnessCheck
from vanilla_mcdoc.data.variants.StructureCheck import StructureCheck


class SpawnConditionBiome(BiomeCheck):
    type: Literal['minecraft:biome', 'biome'] = 'minecraft:biome'


class SpawnConditionMoonBrightness(MoonBrightnessCheck):
    type: Literal['minecraft:moon_brightness', 'moon_brightness'] = 'minecraft:moon_brightness'


class SpawnConditionStructure(StructureCheck):
    type: Literal['minecraft:structure', 'structure'] = 'minecraft:structure'


type SpawnCondition = Annotated[
    SpawnConditionBiome | SpawnConditionMoonBrightness | SpawnConditionStructure,
    Field(discriminator='type'),
]
