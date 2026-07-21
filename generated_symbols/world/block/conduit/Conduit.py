# Generated from symbols.json for ::java::world::block::conduit::Conduit
from dataclasses import dataclass
from generated_symbols.world.block.BlockEntity import BlockEntity


@dataclass(kw_only=True)
class Conduit(BlockEntity):
    Target: tuple[int, int, int, int] | None = None  # The hostile mob that the conduit is currently attacking.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::conduit::Conduit": {
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
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "The hostile mob that the conduit is currently attacking.",
                "key": "target_uuid",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::conduit::TargetUuid",
                    "attributes": [
                        {
                            "name": "uuid"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "The hostile mob that the conduit is currently attacking.",
                "key": "Target",
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

