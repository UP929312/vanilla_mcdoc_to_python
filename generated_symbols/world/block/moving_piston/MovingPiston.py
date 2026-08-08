# Generated from symbols.json for ::java::world::block::moving_piston::MovingPiston
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState
    from generated_symbols.util.direction.DirectionByte import DirectionByte


@dataclass(kw_only=True)
class MovingPiston(BlockEntity):
    blockState: BlockState | None = None  # Moving block represented by the moving piston.
    facing: DirectionByte | None = None  # The direction it is moving.
    progress: float | None = None  # How far it has moved.
    extending: bool | None = None
    source: bool | None = None  # Whether the moving piston is the piston head.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::moving_piston::MovingPiston": {
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
                "desc": "Moving block represented by the moving piston.",
                "key": "blockState",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The direction it is moving.",
                "key": "facing",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::util::direction::DirectionInt",
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
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::util::direction::DirectionByte",
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
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "How far it has moved.",
                "key": "progress",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "extending",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the moving piston is the piston head.",
                "key": "source",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

