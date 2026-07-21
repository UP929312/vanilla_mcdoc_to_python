# Generated from symbols.json for ::java::world::block::sculk_catalyst::ChargeCursor
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.direction.Direction import Direction


@dataclass(kw_only=True)
class ChargeCursor:
    pos: tuple[int, int, int]
    charge: Annotated[int, 'Range | `0`-`1000` | both inclusive'] | None = None
    decay_delay: Annotated[int, 'Range | `0`-`1` | both inclusive'] | None = None
    update_delay: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None
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

