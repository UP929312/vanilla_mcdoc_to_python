# Generated from symbols.json for ::java::world::component::block::PotDecorations
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class PotDecorations:
    back: ItemStackTemplate | None = None
    left: ItemStackTemplate | None = None
    right: ItemStackTemplate | None = None
    front: ItemStackTemplate | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::block::PotDecorations": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "back",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStackTemplate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "left",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStackTemplate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "right",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStackTemplate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "front",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStackTemplate"
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
                        "value": "26.3"
                    }
                }
            }
        ]
    }
}

