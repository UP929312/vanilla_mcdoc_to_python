# Generated from symbols.json for ::java::world::item::leather_armor::LeatherArmor
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from generated_symbols.world.item.leather_armor.ColorDisplay import ColorDisplay


@dataclass(kw_only=True)
class LeatherArmor(ItemBase):
    display: ColorDisplay | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::leather_armor::LeatherArmor": {
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
                "key": "display",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::leather_armor::ColorDisplay"
                },
                "optional": True
            }
        ]
    }
}

