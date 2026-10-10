"""
Generated from symbols.json for ::java::world::entity::mob::mannequin::Mannequin
Local link to file: vanilla_mcdoc/world/entity/mob/mannequin/Mannequin.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.mob.LivingEntity import LivingEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.util.avatar.HumanoidArm import HumanoidArm
    from vanilla_mcdoc.util.avatar.PlayerModelPart import PlayerModelPart
    from vanilla_mcdoc.util.avatar.Profile import Profile
    from vanilla_mcdoc.util.text.Text import Text
    from vanilla_mcdoc.world.entity.mob.EntityEquipment import EntityEquipment
    from vanilla_mcdoc.world.entity.mob.mannequin.MannequinPose import MannequinPose


class Mannequin(LivingEntity):
    profile: Profile | None = None
    hidden_layers: list[PlayerModelPart] | None = None
    main_hand: HumanoidArm | None = None  # Defaults to `right`.
    pose: MannequinPose | None = None  # Defaults to `standing`.
    immovable: bool | None = None  # Defaults to `false`.
    description: Text | None = None  # Text shown below the name tag. Defaults to the translated `entity.minecraft.mannequin.label`.
    hide_description: bool | None = None  # Whether the below name text is displayed. Defaults to `false`.
    equipment: EntityEquipment | None = None  # The equipment items of the mannequin.
