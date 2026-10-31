"""
Generated from symbols.json for ::java::world::entity::mob::zombie::DrowningTracker
Local link to file: vanilla_mcdoc/world/entity/mob/zombie/DrowningTracker.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class DrowningTracker(GeneratedModel):
    DrownedConversionTime: int | None = None  # Ticks until it converts.
    InWaterTime: int | None = None  # Ticks it has been in the water.
