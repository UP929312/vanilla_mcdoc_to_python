"""
Generated from symbols.json for ::java::world::entity::display::Brightness
Local link to file: generated_symbols/world/entity/display/Brightness.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class Brightness(GeneratedModel):
    sky: Annotated[int, Field(ge=0, le=15)]  # Value of skylight.
    block: Annotated[int, Field(ge=0, le=15)]  # Value of block light.


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

