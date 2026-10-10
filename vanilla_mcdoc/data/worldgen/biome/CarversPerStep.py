"""
Generated from symbols.json for ::java::data::worldgen::biome::CarversPerStep
Local link to file: vanilla_mcdoc/data/worldgen/biome/CarversPerStep.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.CarveStep import CarveStep
    from vanilla_mcdoc.data.worldgen.carver.CarverListRef import CarverListRef


type CarversPerStep = dict[CarveStep, CarverListRef]
