"""
Generated from symbols.json for ::java::world::block::sculk_catalyst::ChargeCursor
Local link to file: generated_symbols/world/block/sculk_catalyst/ChargeCursor.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.direction.Direction import Direction


class ChargeCursor(GeneratedModel):
    pos: tuple[int, int, int]
    charge: Annotated[int, Field(ge=0, le=1000)] | None = None
    decay_delay: Annotated[int, Field(ge=0, le=1)] | None = None
    update_delay: Annotated[int, Field(ge=0)] | None = None
    facings: list[Direction] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::sculk_catalyst::ChargeCursor": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "pos",
                "type": {
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
            },
            {
                "kind": "pair",
                "key": "charge",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1000
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "decay_delay",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "update_delay",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "facings",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::direction::Direction"
                    }
                },
                "optional": True
            }
        ]
    }
}

