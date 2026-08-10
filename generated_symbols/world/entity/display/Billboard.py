"""
Generated from symbols.json for ::java::world::entity::display::Billboard
Local link to file: generated_symbols/world/entity/display/Billboard.py
"""
# ~~~ CODE ~~~
from enum import Enum


class Billboard(Enum):
    FIXED = "fixed"  # No rotation.
    VERTICAL = "vertical"  # Pivot around the vertical axis.
    HORIZONTAL = "horizontal"  # Pivot around the horizontal axis.
    CENTER = "center"  # Pivot around both axes.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::display::Billboard": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "No rotation.",
                "identifier": "Fixed",
                "value": "fixed"
            },
            {
                "desc": "Pivot around the vertical axis.",
                "identifier": "Vertical",
                "value": "vertical"
            },
            {
                "desc": "Pivot around the horizontal axis.",
                "identifier": "Horizontal",
                "value": "horizontal"
            },
            {
                "desc": "Pivot around both axes.",
                "identifier": "Center",
                "value": "center"
            }
        ]
    }
}

