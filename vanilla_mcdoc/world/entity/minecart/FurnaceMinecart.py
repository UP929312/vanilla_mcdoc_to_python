"""
Generated from symbols.json for ::java::world::entity::minecart::FurnaceMinecart
Local link to file: vanilla_mcdoc/world/entity/minecart/FurnaceMinecart.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.minecart.Minecart import Minecart


class FurnaceMinecart(Minecart):
    PushX: float | None = None  # Acceleration in x axis.
    PushZ: float | None = None  # Acceleration in z axis.
    Fuel: int | None = None  # Ticks until the fuel runs out.
