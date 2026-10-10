"""
Generated from symbols.json for ::java::util::memory::LikedPlayer
Local link to file: vanilla_mcdoc/util/memory/LikedPlayer.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class LikedPlayer(ExpirableValue):
    value: MinecraftUUID  # The UUID of the player entity that the allay likes.
