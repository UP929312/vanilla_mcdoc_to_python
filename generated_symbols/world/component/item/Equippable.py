# Generated from symbols.json for ::java::world::component::item::Equippable
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.util.slot.EquipmentSlot import EquipmentSlot


@dataclass(kw_only=True)
class Equippable:
    slot: EquipmentSlot
    equip_sound: SoundEventRef | None = None  # Sound event to play when the item is equipped. If not specified, the default armor equip sound will be played.
    asset_id: str | None = None
    camera_overlay: str | None = None  # The overlay texture that should render in first person when equipped.
    allowed_entities: str | list[str] | None = None  # Limits which entities can equip this item.
    dispensable: bool | None = None  # Whether the item can be equipped by using a dispenser. Defaults to `true`.
    swappable: bool | None = None  # Whether the item can be equipped by right-clicking. Defaults to `true`.
    damage_on_hurt: bool | None = None  # Whether the item will be damaged when the wearer is damaged. Defaults to `true`.
    equip_on_interact: bool | None = None  # Whether players can equip this item onto a target mob by right-clicking it (as long as this item can be equipped on the target at all). The item will not be equipped if the target already has an item in the relevant slot. Defaults to `false`.
    can_be_sheared: bool | None = None  # Whether players can use shears to remove this item from a mob by right-clicking it (as long as other shearing conditions are satisfied). Defaults to `false`.
    shearing_sound: SoundEventRef | None = None  # Sound event to play when the item is sheared from a mob. If not specified, the default shearing sound (`item.shears.snip`) will be played.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::Equippable": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "slot",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::slot::EquipmentSlot"
                }
            },
            {
                "kind": "pair",
                "desc": "Sound event to play when the item is equipped.\nIf not specified, the default armor equip sound will be played.",
                "key": "equip_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "desc": "The equipment model to use when equipped.\nFalls back to rendering as the item itself when in the head slot (or no rendering if not applicable).",
                "key": "model",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "equipment"
                                }
                            }
                        }
                    ]
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "key": "asset_id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "equipment"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The overlay texture that should render in first person when equipped.",
                "key": "camera_overlay",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "texture"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Limits which entities can equip this item.",
                "key": "allowed_entities",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "entity_type"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "entity_type"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the item can be equipped by using a dispenser. Defaults to `True`.",
                "key": "dispensable",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the item can be equipped by right-clicking. Defaults to `True`.",
                "key": "swappable",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the item will be damaged when the wearer is damaged. Defaults to `True`.",
                "key": "damage_on_hurt",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether players can equip this item onto a target mob by right-clicking it (as long as this item can be equipped on the target at all).\nThe item will not be equipped if the target already has an item in the relevant slot.\nDefaults to `False`.",
                "key": "equip_on_interact",
                "type": {
                    "kind": "boolean"
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
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "desc": "Whether players can use shears to remove this item from a mob by right-clicking it (as long as other shearing conditions are satisfied).\nDefaults to `False`.",
                "key": "can_be_sheared",
                "type": {
                    "kind": "boolean"
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
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "desc": "Sound event to play when the item is sheared from a mob.\nIf not specified, the default shearing sound (`item.shears.snip`) will be played.",
                "key": "shearing_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            }
        ]
    }
}

