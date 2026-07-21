# Generated from symbols.json for ::java::world::item::map::Decoration
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.item.map.IconByteId import IconByteId


@dataclass(kw_only=True)
class Decoration:
    type: IconByteId  # Decoration type.
    x: float  # World x position.
    z: float  # World z position.
    rot: float  # Rotation of the decoration, measured in degrees clockwise.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::map::Decoration": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Decoration type.",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::map::IconByteId"
                }
            },
            {
                "kind": "pair",
                "desc": "World x position.",
                "key": "x",
                "type": {
                    "kind": "double"
                }
            },
            {
                "kind": "pair",
                "desc": "World z position.",
                "key": "z",
                "type": {
                    "kind": "double"
                }
            },
            {
                "kind": "pair",
                "desc": "Rotation of the decoration, measured in degrees clockwise.",
                "key": "rot",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}

