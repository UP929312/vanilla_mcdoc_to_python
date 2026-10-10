"""
Generated from symbols.json for ::java::world::block::beacon::Beacon
Local link to file: vanilla_mcdoc/world/block/beacon/Beacon.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.block.BlockEntity import BlockEntity
from vanilla_mcdoc.world.block.Lockable import Lockable
from vanilla_mcdoc.world.block.Nameable import Nameable


class Beacon(BlockEntity, Lockable, Nameable):
    Levels: int | None = None  # Number of levels from the pyramid.
    primary_effect: Annotated[str, IdSpec(registry='mob_effect')] | None = None
    secondary_effect: Annotated[str, IdSpec(registry='mob_effect')] | None = None
