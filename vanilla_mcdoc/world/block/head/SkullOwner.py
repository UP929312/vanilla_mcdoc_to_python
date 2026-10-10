"""
Generated from symbols.json for ::java::world::block::head::SkullOwner
Local link to file: vanilla_mcdoc/world/block/head/SkullOwner.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import MinecraftUUID

if TYPE_CHECKING:
    from vanilla_mcdoc.world.block.head.Properties import Properties


class SkullOwner(GeneratedModel):
    Id: MinecraftUUID | None = None  # Optional.
    Name: str | None = None  # Name of the owner, if missing appears as a steve head.
    Properties_: Properties | None = Field(default=None, alias='Properties')
