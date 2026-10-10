"""
Generated from symbols.json for ::java::world::item::firework::Fireworks
Local link to file: vanilla_mcdoc/world/item/firework/Fireworks.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.firework.Explosion import Explosion


class Fireworks(GeneratedModel):
    Flight: int | None = None  # Duration of flight.
    Explosions: list[Explosion] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::firework::Fireworks": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Duration of flight.",
                "key": "Flight",
                "type": {
                    "kind": "byte"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Explosions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::item::firework::Explosion"
                    }
                },
                "optional": True
            }
        ]
    }
}
