# Generated from symbols.json for ::java::data::structure::RandomizedPalette
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class RandomizedPalette:
    palettes: list[list[BlockState]]  # Sets of different block states used in the structure, a random palette gets selected based on coordinates.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::structure::RandomizedPalette": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Sets of different block states used in the structure, a random palette gets selected based on coordinates.",
                "key": "palettes",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "list",
                        "item": {
                            "kind": "reference",
                            "path": "::java::util::block_state::BlockState"
                        }
                    }
                }
            }
        ]
    }
}

