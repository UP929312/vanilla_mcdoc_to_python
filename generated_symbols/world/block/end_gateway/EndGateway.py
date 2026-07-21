# Generated from symbols.json for ::java::world::block::end_gateway::EndGateway
from dataclasses import dataclass
from generated_symbols.world.block.BlockEntity import BlockEntity


@dataclass(kw_only=True)
class EndGateway(BlockEntity):
    Age: int | None = None  # In game ticks.
    ExactTeleport: bool | None = None  # Whether to teleport to the exact location.
    exit_portal: tuple[int, int, int] | None = None  # Coordinates of where to teleport entities to.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::end_gateway::EndGateway": {
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
                "kind": "pair",
                "desc": "In game ticks.",
                "key": "Age",
                "type": {
                    "kind": "long"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether to teleport to the exact location.",
                "key": "ExactTeleport",
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
                "desc": "Coordinates of where to teleport entities to.",
                "key": "ExitPortal",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::end_gateway::ExitPortal"
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
                "desc": "Coordinates of where to teleport entities to.",
                "key": "exit_portal",
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

