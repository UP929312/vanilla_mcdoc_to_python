"""
Generated from symbols.json for ::java::world::entity::mob::zombie::FreezingTracker
Local link to file: vanilla_mcdoc/world/entity/mob/zombie/FreezingTracker.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class FreezingTracker(GeneratedModel):
    FrostbiteConversionTime: int | None = None  # Ticks until it converts.
    FreezingTime: int | None = None  # Ticks it has been in the powdered snow.
