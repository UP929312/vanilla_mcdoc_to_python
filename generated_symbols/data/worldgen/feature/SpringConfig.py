# Generated from symbols.json for ::java::data::worldgen::feature::SpringConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.fluid_state.FluidState import FluidState


@dataclass(kw_only=True)
class SpringConfig:
    state: FluidState
    rock_count: int
    hole_count: int
    requires_block_below: bool
    valid_blocks: list[str] | str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::SpringConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::fluid_state::FluidState"
                }
            },
            {
                "kind": "pair",
                "key": "rock_count",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "hole_count",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "requires_block_below",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "key": "valid_blocks",
                "type": {
                    "kind": "union",
                    "members": [
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
                                                "value": "block"
                                            }
                                        }
                                    }
                                ]
                            }
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
                                            "value": "1.18.2"
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
                                                    "value": "block"
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
                        }
                    ]
                }
            }
        ]
    }
}

