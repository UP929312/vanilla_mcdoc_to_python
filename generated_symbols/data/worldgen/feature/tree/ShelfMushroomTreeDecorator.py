"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::ShelfMushroomTreeDecorator
Local link to file: generated_symbols/data/worldgen/feature/tree/ShelfMushroomTreeDecorator.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class ShelfMushroomTreeDecorator:
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::ShelfMushroomTreeDecorator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "probability",
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

