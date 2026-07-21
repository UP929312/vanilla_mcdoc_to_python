# Generated from symbols.json for ::java::assets::item_definition::GrassTint
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class GrassTint:
    temperature: Annotated[float, 'Range | `0`-`1` | both inclusive']
    downfall: Annotated[float, 'Range | `0`-`1` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::GrassTint": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "temperature",
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
                "key": "downfall",
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

