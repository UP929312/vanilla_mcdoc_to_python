"""
Generated from symbols.json for ::java::world::entity::mob::armor_stand::Pose
Local link to file: vanilla_mcdoc/world/entity/mob/armor_stand/Pose.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class Pose(GeneratedModel):
    Body: tuple[float, float, float] | None = None
    LeftArm: tuple[float, float, float] | None = None
    RightArm: tuple[float, float, float] | None = None
    LeftLeg: tuple[float, float, float] | None = None
    RightLeg: tuple[float, float, float] | None = None
    Head: tuple[float, float, float] | None = None
