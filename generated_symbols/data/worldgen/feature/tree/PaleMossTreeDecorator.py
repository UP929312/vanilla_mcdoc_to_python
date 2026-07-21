# Generated from symbols.json for ::java::data::worldgen::feature::tree::PaleMossTreeDecorator
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class PaleMossTreeDecorator:
    leaves_probability: Annotated[float, 'Range | `0`-`1` | both inclusive']
    trunk_probability: Annotated[float, 'Range | `0`-`1` | both inclusive']
    ground_probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::PaleMossTreeDecorator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "leaves_probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "trunk_probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "ground_probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}

