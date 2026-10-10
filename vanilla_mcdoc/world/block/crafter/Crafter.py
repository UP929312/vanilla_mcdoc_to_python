"""
Generated from symbols.json for ::java::world::block::crafter::Crafter
Local link to file: vanilla_mcdoc/world/block/crafter/Crafter.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.world.block.container.Container9 import Container9


class Crafter(Container9):
    crafting_ticks_remaining: int | None = None
    disabled_slots: Annotated[list[Annotated[int, Field(ge=0, le=8)]], Field(max_length=9)] | None = None
    triggered: Literal[0] | Literal[1] | None = None
