"""
Generated from symbols.json for ::java::world::block::conduit::Conduit
Local link to file: vanilla_mcdoc/world/block/conduit/Conduit.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.world.block.BlockEntity import BlockEntity


class Conduit(BlockEntity):
    Target: MinecraftUUID | None = None  # The hostile mob that the conduit is currently attacking.
