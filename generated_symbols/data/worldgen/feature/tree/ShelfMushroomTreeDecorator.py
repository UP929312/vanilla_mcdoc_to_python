# Generated from symbols.json for ::java::data::worldgen::feature::tree::ShelfMushroomTreeDecorator
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

