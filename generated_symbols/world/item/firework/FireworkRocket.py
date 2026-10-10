"""
Generated from symbols.json for ::java::world::item::firework::FireworkRocket
Local link to file: generated_symbols/world/item/firework/FireworkRocket.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from pydantic import Field

from generated_symbols.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from generated_symbols.world.item.firework.Fireworks import Fireworks


class FireworkRocket(ItemBase):
    Fireworks_: Fireworks | None = Field(default=None, alias='Fireworks')


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

