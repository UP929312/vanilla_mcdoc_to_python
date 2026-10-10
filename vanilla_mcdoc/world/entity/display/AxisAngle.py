"""
Generated from symbols.json for ::java::world::entity::display::AxisAngle
Local link to file: vanilla_mcdoc/world/entity/display/AxisAngle.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class AxisAngle(GeneratedModel):
    axis: tuple[float, float, float]  # Local position of the axis in [x, y, z].
    angle: float  # Angle to rotate around the axis in radians.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::display::AxisAngle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Local position of the axis in [x, y, z].",
                "key": "axis",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Angle to rotate around the axis in radians.",
                "key": "angle",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}
