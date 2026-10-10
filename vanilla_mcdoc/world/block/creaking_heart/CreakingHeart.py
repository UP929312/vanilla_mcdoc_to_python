"""
Generated from symbols.json for ::java::world::block::creaking_heart::CreakingHeart
Local link to file: vanilla_mcdoc/world/block/creaking_heart/CreakingHeart.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.world.block.BlockEntity import BlockEntity


class CreakingHeart(BlockEntity):
    creaking: MinecraftUUID | None = None  # The creaking mob that is linked to this heart.
