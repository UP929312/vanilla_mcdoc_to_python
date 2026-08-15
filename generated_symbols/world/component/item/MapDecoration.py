"""
Generated from symbols.json for ::java::world::component::item::MapDecoration
Local link to file: generated_symbols/world/component/item/MapDecoration.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class MapDecoration:
    type: Annotated[str, IdSpec(registry='map_decoration_type')]  # Decoration type.
    x: float  # World x position.
    z: float  # World z position.
    rotation: float  # Rotation of the decoration, measured in degrees clockwise.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::MapDecoration": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Decoration type.",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "map_decoration_type"
                                }
                            }
                        }
                    ]
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
                "key": "rotation",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}

