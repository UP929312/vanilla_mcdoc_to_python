# Generated from symbols.json for ::java::world::entity::display::Brightness
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class Brightness:
    sky: Annotated[int, 'Range | `0`-`15` | both inclusive']  # Value of skylight.
    block: Annotated[int, 'Range | `0`-`15` | both inclusive']  # Value of block light.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::display::Brightness": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Value of skylight.",
                "key": "sky",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 15
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Value of block light.",
                "key": "block",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 15
                    }
                }
            }
        ]
    }
}

