# Generated from symbols.json for ::java::world::entity::display::Rotation
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.entity.display.AxisAngle import AxisAngle


type Rotation = tuple[float, float, float, float] | AxisAngle


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::display::Rotation": {
        "kind": "union",
        "members": [
            {
                "kind": "list",
                "item": {
                    "kind": "float"
                },
                "lengthRange": {
                    "kind": 0,
                    "min": 4,
                    "max": 4
                },
                "attributes": [
                    {
                        "name": "canonical"
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::world::entity::display::AxisAngle"
            }
        ]
    }
}

