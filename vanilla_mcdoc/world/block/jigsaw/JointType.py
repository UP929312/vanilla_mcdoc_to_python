"""
Generated from symbols.json for ::java::world::block::jigsaw::JointType
Local link to file: vanilla_mcdoc/world/block/jigsaw/JointType.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class JointType(StrEnum):
    ROLLABLE = "rollable"  # The structure can be rotated
    ALIGNED = "aligned"  # The structure cannot be transformed
