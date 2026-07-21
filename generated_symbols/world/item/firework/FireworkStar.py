# Generated from symbols.json for ::java::world::item::firework::FireworkStar
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from generated_symbols.world.item.firework.Explosion import Explosion


@dataclass(kw_only=True)
class FireworkStar(ItemBase):
    Explosion: Explosion | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::firework::FireworkStar": {
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
                "key": "Explosion",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::firework::Explosion"
                },
                "optional": True
            }
        ]
    }
}

