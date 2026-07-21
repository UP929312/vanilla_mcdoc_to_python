# Generated from symbols.json for ::java::world::entity::display::Transformation
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.entity.display.Rotation import Rotation


@dataclass(kw_only=True)
class TransformationStruct1:
    translation: tuple[float, float, float]  # Translation in [x, y, z].
    left_rotation: Rotation  # Using this rotation is enough for most transformations.
    right_rotation: Rotation  # For more complex transformations. Applied **before** scaling.
    scale: tuple[float, float, float]  # Scale in [x, y, z].

type Transformation = TransformationStruct1 | tuple[float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::display::Transformation": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "desc": "Translation in [x, y, z].",
                        "key": "translation",
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
                        "desc": "Using this rotation is enough for most transformations.",
                        "key": "left_rotation",
                        "type": {
                            "kind": "reference",
                            "path": "::java::world::entity::display::Rotation"
                        }
                    },
                    {
                        "kind": "pair",
                        "desc": "For more complex transformations. Applied **before** scaling.",
                        "key": "right_rotation",
                        "type": {
                            "kind": "reference",
                            "path": "::java::world::entity::display::Rotation"
                        }
                    },
                    {
                        "kind": "pair",
                        "desc": "Scale in [x, y, z].",
                        "key": "scale",
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
                    }
                ],
                "attributes": [
                    {
                        "name": "canonical"
                    }
                ]
            },
            {
                "kind": "union",
                "members": [
                    {
                        "kind": "list",
                        "item": {
                            "kind": "float"
                        },
                        "lengthRange": {
                            "kind": 0,
                            "min": 16,
                            "max": 16
                        }
                    }
                ]
            }
        ]
    }
}

