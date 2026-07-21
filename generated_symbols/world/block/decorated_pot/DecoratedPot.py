# Generated from symbols.json for ::java::world::block::decorated_pot::DecoratedPot
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from generated_symbols.world.component.block.PotDecorations import PotDecorations
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class DecoratedPot(BlockEntity):
    sherds: PotDecorations | None = None  # Item ID of what was used for each side of the pot.  Decoration textures are determined by `provides_pottery_pattern` component on the sherd items.
    LootTable: str | None = None  # Loot table that will populate this container.
    LootTableSeed: int | None = None  # Seed of the loot table.
    item: ItemStack | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::decorated_pot::DecoratedPot": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::BlockEntity"
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Item ID of what was used for each side of the pot. \\\nOnly vanilla pottery sherds have hardcoded decoration textures. \\\nOther items are treated like brick.",
                            "key": "sherds",
                            "type": {
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
                                                    "value": "item"
                                                }
                                            }
                                        }
                                    ]
                                },
                                "lengthRange": {
                                    "kind": 0,
                                    "max": 4
                                }
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Item ID of what was used for each side of the pot. \\\nDecoration textures are determined by `provides_pottery_pattern` component on the sherd items.",
                            "key": "sherds",
                            "type": {
                                "kind": "reference",
                                "path": "::java::world::component::block::PotDecorations"
                            },
                            "optional": True
                        }
                    ]
                }
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
                                "value": "1.20.3"
                            }
                        }
                    }
                ],
                "desc": "Loot table that will populate this container.",
                "key": "LootTable",
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
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.3"
                            }
                        }
                    }
                ],
                "desc": "Seed of the loot table.",
                "key": "LootTableSeed",
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
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.3"
                            }
                        }
                    }
                ],
                "key": "item",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            }
        ]
    }
}

