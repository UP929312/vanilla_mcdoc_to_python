# Generated from symbols.json for ::java::world::item::head::PlayerHead
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from generated_symbols.world.item.head.SkullOwner import SkullOwner


@dataclass(kw_only=True)
class PlayerHead(ItemBase):
    SkullOwner: SkullOwner | str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::head::PlayerHead": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemBase"
                }
            },
            {
                "kind": "pair",
                "key": "SkullOwner",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::world::item::head::SkullOwner"
                        },
                        {
                            "kind": "string"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

