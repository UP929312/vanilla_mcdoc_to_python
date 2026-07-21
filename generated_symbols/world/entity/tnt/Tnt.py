# Generated from symbols.json for ::java::world::entity::tnt::Tnt
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class Tnt(EntityBase):
    fuse: int | None = None  # Ticks until it explodes.
    block_state: BlockState | None = None  # Defaults to tnt.
    explosion_power: Annotated[float, 'Range | `0`-`128` | both inclusive'] | None = None
    owner: tuple[int, int, int, int] | None = None  # The entity that primed this TNT.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::tnt::Tnt": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::EntityBase"
                }
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
                                "value": "1.20.3"
                            }
                        }
                    }
                ],
                "desc": "Ticks until it explodes.",
                "key": "Fuse",
                "type": {
                    "kind": "short"
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
                "desc": "Ticks until it explodes.",
                "key": "fuse",
                "type": {
                    "kind": "short"
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
                "desc": "Defaults to tnt.",
                "key": "block_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
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
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "key": "explosion_power",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 128
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
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "desc": "The entity that primed this TNT.",
                "key": "owner",
                "type": {
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
                },
                "optional": True
            }
        ]
    }
}

