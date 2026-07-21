# Generated from symbols.json for ::java::world::block::crafter::Crafter
from dataclasses import dataclass
from typing import Annotated
from generated_symbols.world.block.container.Container9 import Container9


@dataclass(kw_only=True)
class Crafter(Container9):
    crafting_ticks_remaining: int | None = None
    disabled_slots: Annotated[list[Annotated[int, 'Range | `0`-`8` | both inclusive']], 'Length = up to 9 (inclusive)'] | None = None
    triggered: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::crafter::Crafter": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::container::Container9"
                }
            },
            {
                "kind": "pair",
                "key": "crafting_ticks_remaining",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "disabled_slots",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "max": 9
                    },
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 8
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "triggered",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "literal",
                            "value": {
                                "kind": "int",
                                "value": 0
                            }
                        },
                        {
                            "kind": "literal",
                            "value": {
                                "kind": "int",
                                "value": 1
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

