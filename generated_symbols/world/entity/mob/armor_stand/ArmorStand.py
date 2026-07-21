# Generated from symbols.json for ::java::world::entity::mob::armor_stand::ArmorStand
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.LivingEntity import LivingEntity

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.EntityEquipment import EntityEquipment
    from generated_symbols.world.entity.mob.armor_stand.Pose import Pose


@dataclass(kw_only=True)
class ArmorStand(LivingEntity):
    equipment: EntityEquipment | None = None  # The equipment items of the armor stand.
    Invisible: bool | None = None  # Whether it should be invisible.
    Marker: bool | None = None  # Whether it has no hitbox.
    NoBasePlate: bool | None = None  # Whether it should have a no base plate.
    ShowArms: bool | None = None  # Whether it should show its arms.
    Small: bool | None = None  # Whether it is small.
    DisabledSlots: int | None = None  # A bitfield of the slots that cannot be used.
    Pose: Pose | None = None  # Body part rotations.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::armor_stand::ArmorStand": {
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
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "[main hand, offhand]",
                "key": "HandItems",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "union",
                        "members": [
                            {
                                "kind": "reference",
                                "path": "::java::world::item::ItemStack"
                            },
                            {
                                "kind": "struct",
                                "fields": []
                            }
                        ]
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 2,
                        "max": 2
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "[feet, legs, body, head]",
                "key": "ArmorItems",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "union",
                        "members": [
                            {
                                "kind": "reference",
                                "path": "::java::world::item::ItemStack"
                            },
                            {
                                "kind": "struct",
                                "fields": []
                            }
                        ]
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 4,
                        "max": 4
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "The equipment items of the armor stand.",
                "key": "equipment",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::EntityEquipment"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it should be invisible.",
                "key": "Invisible",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it has no hitbox.",
                "key": "Marker",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it should have a no base plate.",
                "key": "NoBasePlate",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it should show its arms.",
                "key": "ShowArms",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it is small.",
                "key": "Small",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "bitfield",
                        "value": {
                            "kind": "reference",
                            "path": "::java::world::entity::mob::armor_stand::DisabledSlots"
                        }
                    }
                ],
                "desc": "A bitfield of the slots that cannot be used.",
                "key": "DisabledSlots",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Body part rotations.",
                "key": "Pose",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::armor_stand::Pose"
                },
                "optional": True
            }
        ]
    }
}

