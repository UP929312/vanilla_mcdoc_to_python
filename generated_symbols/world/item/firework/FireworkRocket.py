# Generated from symbols.json for ::java::world::item::firework::FireworkRocket
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from generated_symbols.world.item.firework.Fireworks import Fireworks


@dataclass(kw_only=True)
class FireworkRocket(ItemBase):
    Fireworks: Fireworks | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::firework::FireworkRocket": {
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
                "key": "Fireworks",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::firework::Fireworks"
                },
                "optional": True
            }
        ]
    }
}

