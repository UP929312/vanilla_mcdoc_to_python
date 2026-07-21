# Generated from symbols.json for ::java::world::block::furnace::Furnace
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.block.BlockEntity import BlockEntity
from generated_symbols.world.block.Lockable import Lockable
from generated_symbols.world.block.Nameable import Nameable

if TYPE_CHECKING:
    from generated_symbols.util.slot.SlottedItem import SlottedItem


@dataclass(kw_only=True)
class Furnace(BlockEntity, Nameable, Lockable):
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`2` | both inclusive']]], 'Length = 0-3 (both inclusive)'] | None = None  # The items in this furnace, with slots: * 0: Item being smelted * 1: Fuel * 2: Output
    cooking_total_time: int | None = None  # The total amount of time the current cooking process will take. Defaults to `0`.
    cooking_time_spent: int | None = None  # The amount of time that the current cooking process has taken so far. Defaults to `0`.
    lit_time_remaining: int | None = None  # The amount of burn time remaining. Defaults to `0`.
    lit_total_time: int | None = None  # The total amount of burn time that was added in the last refuel. Defaults to `0`.
    speed_multiplier: float | None = None  # Used to speed up or slow down the next cooking process. Defaults to `1`.
    RecipesUsed: dict[str, int] | None = None  # Recipes that have been used since the last time a result item was removed from the GUI. Used to calculate the experience to give to the player.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::furnace::Furnace": {
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
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::Nameable"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::Lockable"
                }
            },
            {
                "kind": "pair",
                "desc": "The items in this furnace, with slots:\n* 0: Item being smelted\n* 1: Fuel\n* 2: Output",
                "key": "Items",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::util::slot::SlottedItem"
                        },
                        "typeArgs": [
                            {
                                "kind": "byte",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 0,
                                    "max": 2
                                }
                            }
                        ]
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 3
                    }
                },
                "optional": True
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Ticks until the current fuel runs out.",
                            "key": "BurnTime",
                            "type": {
                                "kind": "short"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Ticks the item has been smelting for.",
                            "key": "CookTime",
                            "type": {
                                "kind": "short"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Total ticks the item will take to be smelted.",
                            "key": "CookTimeTotal",
                            "type": {
                                "kind": "short"
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "The total amount of time the current cooking process will take. Defaults to `0`.",
                            "key": "cooking_total_time",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "short",
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
                                        ]
                                    },
                                    {
                                        "kind": "int",
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
                                        ]
                                    }
                                ]
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "The amount of time that the current cooking process has taken so far. Defaults to `0`.",
                            "key": "cooking_time_spent",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "short",
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
                                        ]
                                    },
                                    {
                                        "kind": "int",
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
                                        ]
                                    }
                                ]
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "The amount of burn time remaining. Defaults to `0`.",
                            "key": "lit_time_remaining",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "short",
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
                                        ]
                                    },
                                    {
                                        "kind": "int",
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
                                        ]
                                    }
                                ]
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "The total amount of burn time that was added in the last refuel. Defaults to `0`.",
                            "key": "lit_total_time",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "short",
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
                                        ]
                                    },
                                    {
                                        "kind": "int",
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
                                            "value": "26.3"
                                        }
                                    }
                                }
                            ],
                            "desc": "Used to speed up or slow down the next cooking process. Defaults to `1`.",
                            "key": "speed_multiplier",
                            "type": {
                                "kind": "float"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Recipes that have been used since the last time a result item was removed from the GUI. Used to calculate the experience to give to the player.",
                "key": "RecipesUsed",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "How many times this recipe has been used.",
                            "key": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "recipe"
                                            }
                                        }
                                    }
                                ]
                            },
                            "type": {
                                "kind": "int"
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

