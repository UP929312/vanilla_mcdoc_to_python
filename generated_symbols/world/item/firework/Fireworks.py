# Generated from symbols.json for ::java::world::item::firework::Fireworks
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.item.firework.Explosion import Explosion


@dataclass(kw_only=True)
class Fireworks:
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

