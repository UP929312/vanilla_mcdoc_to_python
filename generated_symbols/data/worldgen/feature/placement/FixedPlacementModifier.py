# Generated from symbols.json for ::java::data::worldgen::feature::placement::FixedPlacementModifier
from dataclasses import dataclass


@dataclass(kw_only=True)
class FixedPlacementModifier:
    positions: list[tuple[int, int, int]]  # Fixed list of block positions to place the feature at.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::FixedPlacementModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Fixed list of block positions to place the feature at.",
                "key": "positions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "list",
                        "item": {
                            "kind": "int"
                        },
                        "lengthRange": {
                            "kind": 0,
                            "min": 3,
                            "max": 3
                        }
                    }
                }
            }
        ]
    }
}

