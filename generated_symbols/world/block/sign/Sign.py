# Generated from symbols.json for ::java::world::block::sign::Sign
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from generated_symbols.world.component.block.SignText import SignText


@dataclass(kw_only=True)
class Sign(BlockEntity):
    back_text: SignText | None = None
    front_text: SignText | None = None
    is_waxed: bool | None = None  # Whether the sign has been made uneditable by applying wax.
    allow_op_features: bool | None = None  # Whether placed signs resolve text components. Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::sign::Sign": {
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
                "key": "back_text",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::block::SignText"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "front_text",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::block::SignText"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the sign has been made uneditable by applying wax.",
                "key": "is_waxed",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether placed signs resolve text components.\nDefaults to `False`.",
                "key": "allow_op_features",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ],
        "attributes": [
            {
                "name": "since",
                "value": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "1.20"
                    }
                }
            }
        ]
    }
}

