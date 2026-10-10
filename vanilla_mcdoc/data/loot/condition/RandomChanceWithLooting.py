"""
Generated from symbols.json for ::java::data::loot::condition::RandomChanceWithLooting
Local link to file: vanilla_mcdoc/data/loot/condition/RandomChanceWithLooting.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class RandomChanceWithLooting(GeneratedModel):
    chance: Annotated[float, Field(ge=0, le=1)]
    looting_multiplier: float  # Looting adjustment to the base success rate. Formula is `chance + (looting_level * looting_multiplier)` .
