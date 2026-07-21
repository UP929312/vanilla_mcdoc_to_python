# Generated from symbols.json for ::java::world::block::brewing_stand::BrewingStand
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.block.BlockEntity import BlockEntity
from generated_symbols.world.block.Lockable import Lockable
from generated_symbols.world.block.Nameable import Nameable

if TYPE_CHECKING:
    from generated_symbols.util.slot.SlottedItem import SlottedItem


@dataclass(kw_only=True)
class BrewingStand(BlockEntity, Nameable, Lockable):
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`4` | both inclusive']]], 'Length = 0-5 (both inclusive)'] | None = None  # * 0: left brewing slot * 1: middle brewing slot * 2: right brewing slot * 3: ingredient slot * 4: fuel slot
    BrewTime: int | None = None  # Number of ticks until the brewing is complete.
    Fuel: int | None = None  # Amount of fuel the brewing stand has left.
    total_brew_time: int | None = None  # The total amount of time the current brewing process will take. Defaults to `400`.
    total_fuel: int | None = None  # The amount of fuel that was added in the last refuel. Defaults to `20`.
    speed_multiplier: float | None = None  # Used to speed up or slow down the next brewing process. Defaults to `1`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::brewing_stand::BrewingStand": {
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
                "desc": "* 0: left brewing slot\n* 1: middle brewing slot\n* 2: right brewing slot\n* 3: ingredient slot\n* 4: fuel slot",
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
                                    "max": 4
                                }
                            }
                        ]
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 5
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Number of ticks until the brewing is complete.",
                "key": "BrewTime",
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
                "desc": "Amount of fuel the brewing stand has left.",
                "key": "Fuel",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "byte",
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
                "desc": "The total amount of time the current brewing process will take. Defaults to `400`.",
                "key": "total_brew_time",
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "desc": "The amount of fuel that was added in the last refuel. Defaults to `20`.",
                "key": "total_fuel",
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "desc": "Used to speed up or slow down the next brewing process. Defaults to `1`.",
                "key": "speed_multiplier",
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ]
    }
}

