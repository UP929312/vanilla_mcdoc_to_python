# Generated from symbols.json for ::java::world::block::vault::Vault
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class Vault:
    server_data: Any | None = None
    config: Any | None = None
    shared_data: Any | None = None  # When a player is in range of the vault, the same display item will be shown to all players. This is also used for the items that are being ejected from the vault.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::vault::Vault": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "server_data",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Ticks until the loot table is ran again to update the display item.",
                            "key": "state_updating_resumes_at",
                            "type": {
                                "kind": "long"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "When a player is in this list they can no longer open the vault, but other players can.",
                            "key": "rewarded_players",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "int_array",
                                    "lengthRange": {
                                        "kind": 0,
                                        "min": 4,
                                        "max": 4
                                    }
                                }
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Items that are being ejected from the vault when it is opened. As each item is ejected, it is removed from this list, before ejection, it is previewed as the `display_item`.",
                            "key": "items_to_eject",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "reference",
                                    "path": "::java::world::item::ItemStack"
                                }
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Number of items that the loot table started off the opening with, does not change while items are ejected.",
                            "key": "total_ejections_needed",
                            "type": {
                                "kind": "int"
                            },
                            "optional": True
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "config",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Item required to open the vault.",
                            "key": "key_item",
                            "type": {
                                "kind": "reference",
                                "path": "::java::world::item::ItemStack"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Defaults to \"minecraft:chests/trial_chambers/reward\".",
                            "key": "loot_table",
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "loot_table"
                                            }
                                        }
                                    }
                                ]
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "The loot table to display items in the vault.\nDefaults to use the value in `loot_table` field.",
                            "key": "override_loot_table_to_display",
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "loot_table"
                                            }
                                        }
                                    }
                                ]
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "The range when the vault should activate.",
                            "key": "activation_range",
                            "type": {
                                "kind": "double"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "The range when the vault should deactivate.",
                            "key": "deactivation_range",
                            "type": {
                                "kind": "double"
                            },
                            "optional": True
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "When a player is in range of the vault, the same display item will be shown to all players.\nThis is also used for the items that are being ejected from the vault.",
                "key": "shared_data",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Item that is displayed to players when they are in range of the vault.",
                            "key": "display_item",
                            "type": {
                                "kind": "reference",
                                "path": "::java::world::item::ItemStack"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "connected_players",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "int_array",
                                    "lengthRange": {
                                        "kind": 0,
                                        "min": 4,
                                        "max": 4
                                    },
                                    "attributes": [
                                        {
                                            "name": "uuid"
                                        }
                                    ]
                                }
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "connected_particles_range",
                            "type": {
                                "kind": "double"
                            },
                            "optional": True
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

