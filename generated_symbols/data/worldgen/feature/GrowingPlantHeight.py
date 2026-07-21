# Generated from symbols.json for ::java::data::worldgen::feature::GrowingPlantHeight
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


@dataclass(kw_only=True)
class GrowingPlantHeight:
    weight: int
    data: IntProvider[int] | int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::GrowingPlantHeight": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "weight",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "data",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int"
                        }
                    ]
                }
            }
        ]
    }
}

