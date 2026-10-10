"""
Generated from symbols.json for ::java::world::item::map::FilledMap
Local link to file: generated_symbols/world/item/map/FilledMap.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.world.item.Display import Display
from generated_symbols.world.item.ItemBase import ItemBase
from generated_symbols.world.item.map.Decoration import Decoration


class DecorationsStruct(Decoration):
    id: str  # An arbitrary unique string identifying the decoration.


class DisplayStruct(Display):
    MapColor: int | None = None  # Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.


class FilledMap(ItemBase):
    map: int | None = None  # Map number, representing the shared state holding map contents and markers.
    map_scale_direction: Annotated[int, Field(ge=1)] | None = None  # Amount to increase the current map scale by when crafting.
    map_to_lock: bool | None = None  # Whether the map should be locked after being taken out of the cartography table.
    Decorations: list[DecorationsStruct] | None = None  # Decorations on the map.
    display: DisplayStruct | None = None  # Display for the item.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::map::FilledMap": {
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
                "desc": "Map number, representing the shared state holding map contents and markers.",
                "key": "map",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Amount to increase the current map scale by when crafting.",
                "key": "map_scale_direction",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the map should be locked after being taken out of the cartography table.",
                "key": "map_to_lock",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Decorations on the map.",
                "key": "Decorations",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "spread",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::world::item::map::Decoration"
                                }
                            },
                            {
                                "kind": "pair",
                                "desc": "An arbitrary unique string identifying the decoration.",
                                "key": "id",
                                "type": {
                                    "kind": "string"
                                }
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Display for the item.",
                "key": "display",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "spread",
                            "type": {
                                "kind": "reference",
                                "path": "::java::world::item::Display"
                            }
                        },
                        {
                            "kind": "pair",
                            "desc": "Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.",
                            "key": "MapColor",
                            "type": {
                                "kind": "int",
                                "attributes": [
                                    {
                                        "name": "color",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "composite_rgb"
                                            }
                                        }
                                    }
                                ]
                            },
                            "optional": True
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}
