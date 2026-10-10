"""
Generated from symbols.json for ::java::data::worldgen::biome::BiomeEffects
Local link to file: vanilla_mcdoc/data/worldgen/biome/BiomeEffects.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.biome.GrassColorModifier import GrassColorModifier
    from vanilla_mcdoc.util.color.StringRGB import StringRGB


class BiomeEffects(GeneratedModel):
    water_color: StringRGB
    grass_color: StringRGB | None = None
    foliage_color: StringRGB | None = None
    dry_foliage_color: StringRGB | None = None
    grass_color_modifier: GrassColorModifier | None = None
