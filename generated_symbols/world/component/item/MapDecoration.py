# Generated from symbols.json for ::java::world::component::item::MapDecoration
from dataclasses import dataclass


@dataclass(kw_only=True)
class MapDecoration:
    type: str  # Decoration type.
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

