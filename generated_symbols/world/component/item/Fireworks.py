"""
Generated from symbols.json for ::java::world::component::item::Fireworks
Local link to file: generated_symbols/world/component/item/Fireworks.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.world.component.item.Explosion import Explosion


class Fireworks(GeneratedModel):
    explosions: Annotated[list[Explosion], Field(min_length=0, max_length=256)] | None = None
    flight_duration: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::Fireworks": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "explosions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::component::item::Explosion"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 256
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "flight_duration",
                "type": {
                    "kind": "byte"
                },
                "optional": True
            }
        ]
    }
}

