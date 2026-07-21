# Generated from symbols.json for ::java::world::entity::mob::MobBase
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any
from generated_symbols.world.entity.mob.LivingEntity import LivingEntity

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.DropChances import DropChances
    from generated_symbols.world.entity.mob.EntityEquipment import EntityEquipment


@dataclass(kw_only=True)
class MobBase(LivingEntity):
    equipment: EntityEquipment | None = None  # The equipment items of the mob, such as armor or weapons.
    drop_chances: DropChances | None = None  # Chances of the mob dropping an equipment slot on death.
    DeathLootTable: str | None = None  # Loot table that is dropped when the mob dies.
    DeathLootTableSeed: int | None = None  # Seed for generating the death loot table.
    CanPickUpLoot: bool | None = None  # Whether it can pick up loot.
    PersistenceRequired: bool | None = None  # Whether it should not despawn naturally.
    LeftHanded: bool | None = None  # Whether it is left handed.
    NoAI: bool | None = None  # Whether it should have an AI.
    leash: tuple[int, int, int] | Any | None = None  # What the leash is attached to.
    home_radius: int | None = None  # Defaults to -1, which represents "no home".
    home_pos: tuple[int, int, int] | None = None  # This field will be discarded if `home_radius` is less than 0.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::MobBase": {
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
                "kind": "spread",
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
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
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
                            "desc": "Chance to drop the items it is holding, in [main hand, offhand].\n\n`0.0` is hardcoded to be unaffected by enchantments. \\\nValues between `0.0` and `1.0` (inclusive) randomizes durability of the dropped item.",
                            "key": "HandDropChances",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "float"
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
                            "desc": "Chance to drop the items it is wearing, in [feet, legs, body, head].\n\n`0.0` is hardcoded to be unaffected by enchantments. \\\nValues between `0.0` and `1.0` (inclusive) randomizes durability of the dropped item.",
                            "key": "ArmorDropChances",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "float"
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
                                            "value": "1.20.5"
                                        }
                                    }
                                }
                            ],
                            "desc": "Used for wolf armor & llama carpet decoration.",
                            "key": "body_armor_item",
                            "type": {
                                "kind": "reference",
                                "path": "::java::world::item::ItemStack"
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
                                            "value": "1.20.5"
                                        }
                                    }
                                }
                            ],
                            "desc": "Chance to drop the item it is wearing.",
                            "key": "body_armor_drop_chance",
                            "type": {
                                "kind": "float"
                            },
                            "optional": True
                        }
                    ]
                }
            },
            {
                "kind": "spread",
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
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "The equipment items of the mob, such as armor or weapons.",
                            "key": "equipment",
                            "type": {
                                "kind": "reference",
                                "path": "::java::world::entity::mob::EntityEquipment"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Chances of the mob dropping an equipment slot on death.",
                            "key": "drop_chances",
                            "type": {
                                "kind": "reference",
                                "path": "::java::world::entity::mob::DropChances"
                            },
                            "optional": True
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Loot table that is dropped when the mob dies.",
                "key": "DeathLootTable",
                "type": {
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
                                            "value": "loot_table"
                                        }
                                    },
                                    "empty": {
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
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Seed for generating the death loot table.",
                "key": "DeathLootTableSeed",
                "type": {
                    "kind": "long",
                    "attributes": [
                        {
                            "name": "random"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it can pick up loot.",
                "key": "CanPickUpLoot",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it should not despawn naturally.",
                "key": "PersistenceRequired",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it is left handed.",
                "key": "LeftHanded",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it should have an AI.",
                "key": "NoAI",
                "type": {
                    "kind": "boolean"
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "desc": "What the leash is attached to.",
                "key": "Leash",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::world::entity::mob::UUIDLeash"
                        },
                        {
                            "kind": "reference",
                            "path": "::java::world::entity::mob::BlockLeash"
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "desc": "What the leash is attached to.",
                "key": "leash",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int_array",
                            "lengthRange": {
                                "kind": 0,
                                "min": 3,
                                "max": 3
                            }
                        },
                        {
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "pair",
                                    "key": "UUID",
                                    "type": {
                                        "kind": "int_array",
                                        "lengthRange": {
                                            "kind": 0,
                                            "min": 4,
                                            "max": 4
                                        }
                                    },
                                    "optional": True
                                }
                            ]
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
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "desc": "Defaults to -1, which represents \"no home\".",
                "key": "home_radius",
                "type": {
                    "kind": "int"
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
                "desc": "This field will be discarded if `home_radius` is less than 0.",
                "key": "home_pos",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            }
        ]
    }
}

