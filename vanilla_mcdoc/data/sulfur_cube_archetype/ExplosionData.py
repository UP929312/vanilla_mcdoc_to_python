"""
Generated from symbols.json for ::java::data::sulfur_cube_archetype::ExplosionData
Local link to file: vanilla_mcdoc/data/sulfur_cube_archetype/ExplosionData.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class ExplosionData(GeneratedModel):
    fuse: Annotated[int, Field(ge=1)]  # The fuse time in ticks when ignited.  When ignited by an explosion, the fuse will be a random value between `explosion_fuse / 8` and `3 * explosion_fuse / 8`.
    power: Annotated[int, Field(ge=0)]  # The explosion power.
    causes_fire: bool  # Whether the explosion causes fire.
