"""
Generated from symbols.json for ::java::data::worldgen::biome::GrassColorModifier
Local link to file: vanilla_mcdoc/data/worldgen/biome/GrassColorModifier.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class GrassColorModifier(StrEnum):
    NONE = "none"
    DARKFOREST = "dark_forest"  # Grass color will be average of the base color and `#28340a`.
    SWAMP = "swamp"  # Grass color will be either `#4c763c` or `#6a7039`, depending on block position.  The base color is ignored.
