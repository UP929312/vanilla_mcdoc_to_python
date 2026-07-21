# Generated from symbols.json for ::java::data::worldgen::carver::CanyonConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.worldgen.carver.CarverConfigBase import CarverConfigBase

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.FloatProvider import FloatProvider
    from generated_symbols.data.worldgen.carver.CanyonShape import CanyonShape


@dataclass(kw_only=True)
class CanyonConfig(CarverConfigBase):
    vertical_rotation: FloatProvider[float] | float
    shape: CanyonShape


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::carver::CanyonConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::carver::CarverConfigBase"
                }
            },
            {
                "kind": "pair",
                "key": "vertical_rotation",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "shape",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::carver::CanyonShape"
                }
            }
        ]
    }
}

