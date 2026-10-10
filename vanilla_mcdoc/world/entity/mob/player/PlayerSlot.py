"""
Generated from symbols.json for ::java::world::entity::mob::player::PlayerSlot
Local link to file: vanilla_mcdoc/world/entity/mob/player/PlayerSlot.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field


type PlayerSlot = Annotated[int, Field(ge=0, le=35)]
