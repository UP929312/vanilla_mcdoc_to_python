"""
Generated from symbols.json for ::java::world::entity::mob::armor_stand::ArmorStand
Local link to file: vanilla_mcdoc/world/entity/mob/armor_stand/ArmorStand.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from pydantic import Field

from vanilla_mcdoc.world.entity.mob.LivingEntity import LivingEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.EntityEquipment import EntityEquipment
    from vanilla_mcdoc.world.entity.mob.armor_stand.Pose import Pose


class ArmorStand(LivingEntity):
    equipment: EntityEquipment | None = None  # The equipment items of the armor stand.
    Invisible: bool | None = None  # Whether it should be invisible.
    Marker: bool | None = None  # Whether it has no hitbox.
    NoBasePlate: bool | None = None  # Whether it should have a no base plate.
    ShowArms: bool | None = None  # Whether it should show its arms.
    Small: bool | None = None  # Whether it is small.
    DisabledSlots: int | None = None  # A bitfield of the slots that cannot be used.
    Pose_: Pose | None = Field(default=None, alias='Pose')  # Body part rotations.
