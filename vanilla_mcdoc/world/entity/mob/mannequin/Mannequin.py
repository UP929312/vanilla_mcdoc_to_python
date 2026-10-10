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


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::mannequin::Mannequin": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::LivingEntity"
                }
            },
            {
                "kind": "pair",
                "key": "profile",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::avatar::Profile"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "hidden_layers",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::avatar::PlayerModelPart"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to `right`.",
                "key": "main_hand",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::avatar::HumanoidArm"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to `standing`.",
                "key": "pose",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::mannequin::MannequinPose"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to `False`.",
                "key": "immovable",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Text shown below the name tag.\nDefaults to the translated `entity.minecraft.mannequin.label`.",
                "key": "description",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the below name text is displayed.\nDefaults to `False`.",
                "key": "hide_description",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The equipment items of the mannequin.",
                "key": "equipment",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::EntityEquipment"
                },
                "optional": True
            }
        ]
    }
}
