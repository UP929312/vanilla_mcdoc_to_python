# Generated from symbols.json for ::java::assets::waypoint_style::WaypointStyle
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class WaypointStyle:
    sprites: Annotated[list[str], 'Length = 1 (inclusive) and above']
    near_distance: Annotated[int, 'Range | `0`-`60000000` | both inclusive'] | None = None  # Defaults to 128.
    far_distance: Annotated[int, 'Range | `0`-`60000000` | both inclusive'] | None = None  # Defaults to 322.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::waypoint_style::WaypointStyle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Defaults to 128.",
                "key": "near_distance",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 60000000
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to 322.",
                "key": "far_distance",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 60000000
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "sprites",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "id",
                                "value": {
                                    "kind": "tree",
                                    "values": {
                                        "registry": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "texture"
                                            }
                                        },
                                        "path": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "gui/sprites/hud/locator_bar_dot/"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}

