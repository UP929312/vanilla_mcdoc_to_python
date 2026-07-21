# Generated from symbols.json for ::java::world::component::item::Fireworks
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.world.component.item.Explosion import Explosion


@dataclass(kw_only=True)
class Fireworks:
    explosions: Annotated[list[Explosion], 'Length = 0-256 (both inclusive)'] | None = None
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

