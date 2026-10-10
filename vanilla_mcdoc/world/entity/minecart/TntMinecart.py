"""
Generated from symbols.json for ::java::world::entity::minecart::TntMinecart
Local link to file: vanilla_mcdoc/world/entity/minecart/TntMinecart.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.world.entity.minecart.Minecart import Minecart


class TntMinecart(Minecart):
    fuse: int | None = None  # Ticks until it explodes.
    explosion_power: Annotated[float, Field(ge=0, le=128)] | None = None
    explosion_speed_factor: Annotated[float, Field(ge=0, le=128)] | None = None  # Controls the amount of added damage depending on the speed of the minecart.
