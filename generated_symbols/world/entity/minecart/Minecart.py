# Generated from symbols.json for ::java::world::entity::minecart::Minecart
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from generated_symbols.util.BlockState import BlockState


@dataclass(kw_only=True)
class Minecart(EntityBase):
    DisplayState: BlockState | None = None  # Custom block to display.
    DisplayOffset: int | None = None  # Vertical offset of the block display.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::minecart::Minecart": {
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Whether to display a custom block. Must be True for custom display block to be displayed.",
                "key": "CustomDisplayTile",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Custom block to display.",
                "key": "DisplayState",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::BlockState"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Vertical offset of the block display.",
                "key": "DisplayOffset",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

