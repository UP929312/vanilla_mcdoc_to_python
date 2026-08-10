# ~~~ WHAT ARE WE TESTING ~~~

# DecorationStep, an Enum showing it uppercases it's keys and sets the values properly.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::worldgen::DecorationStep
Local link to file: generated_symbols/data/worldgen/DecorationStep.py
"""
# ~~~ CODE ~~~
from enum import Enum


class DecorationStep(Enum):
    RAWGENERATION = "raw_generation"
    LAKES = "lakes"
    LOCALMODIFICATIONS = "local_modifications"
    UNDERGROUNDSTRUCTURES = "underground_structures"
    SURFACESTRUCTURES = "surface_structures"
    STRONGHOLDS = "strongholds"
    UNDERGROUNDORES = "underground_ores"
    UNDERGROUNDDECORATION = "underground_decoration"
    FLUIDSPRINGS = "fluid_springs"
    VEGETALDECORATION = "vegetal_decoration"
    TOPLAYERMODIFICATION = "top_layer_modification"
