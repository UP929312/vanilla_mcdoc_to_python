"""
Generated from symbols.json for ::java::util::memory::AngryAt
Local link to file: vanilla_mcdoc/util/memory/AngryAt.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class AngryAt(ExpirableValue):
    value: MinecraftUUID  # The target of the piglin or piglin brute.
