# Generated from symbols.json for ::java::world::component::item::blocks_attacks
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.world.component.item.DamageReduction import DamageReduction
    from generated_symbols.world.component.item.ItemDamageFunction import ItemDamageFunction


@dataclass(kw_only=True)
class blocks_attacks:
    block_delay_seconds: Annotated[float, 'Range | Min `0` and above | inclusive'] | None = None  # Number of seconds that right-click must be held before successfully blocking attacks. Defaults to `0`.
    disable_cooldown_scale: Annotated[float, 'Range | Min `0` and above | inclusive'] | None = None  # Multiplier applied to the number of seconds that the item will be on cooldown for when attacked by a disabling attack (`disable_blocking_for_seconds` on the `weapon` component). Defaults to `1`. If `0`, this item can never be disabled by attacks.
    damage_reductions: list[DamageReduction] | None = None  # Controls how much damage should be blocked in a given attack. If not specified, all damage is blocked. Each entry in the list contributes an amount of damage to be blocked, optionally filtered by a damage type. Each entry adds to blocked damage, determined by `clamp(base + factor * dealt_damage, 0, dealt_damage)`. The final damage applied in the attack to the entity is determined by `dealt_damage - clamp(blocked_damage, 0, dealt_damage)`.
    item_damage: ItemDamageFunction | None = None  # Controls how much damage should be applied to the item from a given attack. If not specified, a point of durability is removed for every point of damage dealt. The final damage applied to the item is determined by `floor(base + factor * dealt_damage)`. The final value may be negative, causing the item to be repaired.
    block_sound: SoundEventRef | None = None  # Sound played when an attack is successfully blocked.
    disabled_sound: SoundEventRef | None = None  # Sound played when the item goes on its disabled cooldown due to an attack.
    bypassed_by: str | list[str] | None = None  # Damage types in this tag are bypassing the blocking


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::blocks_attacks": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Number of seconds that right-click must be held before successfully blocking attacks.\nDefaults to `0`.",
                "key": "block_delay_seconds",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Multiplier applied to the number of seconds that the item will be on cooldown for when attacked by a disabling attack (`disable_blocking_for_seconds` on the `weapon` component).\nDefaults to `1`.\nIf `0`, this item can never be disabled by attacks.",
                "key": "disable_cooldown_scale",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Controls how much damage should be blocked in a given attack. If not specified, all damage is blocked.\nEach entry in the list contributes an amount of damage to be blocked, optionally filtered by a damage type.\nEach entry adds to blocked damage, determined by `clamp(base + factor * dealt_damage, 0, dealt_damage)`.\nThe final damage applied in the attack to the entity is determined by `dealt_damage - clamp(blocked_damage, 0, dealt_damage)`.",
                "key": "damage_reductions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::component::item::DamageReduction"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Controls how much damage should be applied to the item from a given attack.\nIf not specified, a point of durability is removed for every point of damage dealt.\nThe final damage applied to the item is determined by `floor(base + factor * dealt_damage)`.\nThe final value may be negative, causing the item to be repaired.",
                "key": "item_damage",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::ItemDamageFunction"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Sound played when an attack is successfully blocked.",
                "key": "block_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Sound played when the item goes on its disabled cooldown due to an attack.",
                "key": "disabled_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Damage types in this tag are bypassing the blocking",
                "key": "bypassed_by",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.1"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "damage_type"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "required"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.1"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "damage_type"
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
                                                "value": "damage_type"
                                            }
                                        }
                                    }
                                ]
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.1"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

