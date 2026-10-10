"""
Generated from symbols.json for ::java::assets::waypoint_style::WaypointStyle
Local link to file: generated_symbols/assets/waypoint_style/WaypointStyle.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec


class WaypointStyle(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'waypoint_style'

    near_distance: Annotated[int, Field(ge=0, le=60000000)] | None = None  # Defaults to 128.
    far_distance: Annotated[int, Field(ge=0, le=60000000)] | None = None  # Defaults to 322.
    sprites: Annotated[list[Annotated[str, IdSpec(registry='texture', path='gui/sprites/hud/locator_bar_dot/')]], Field(min_length=1)]


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
