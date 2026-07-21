# Generated from symbols.json for ::java::util::GlobalPos
from dataclasses import dataclass


@dataclass(kw_only=True)
class GlobalPos:
    pos: tuple[int, int, int]  # Coordinates of the location in [x, y, z]
    dimension: str  # Dimension of the location


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::GlobalPos": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Coordinates of the location in [x, y, z]",
                "key": "pos",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Dimension of the location",
                "key": "dimension",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "dimension"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

