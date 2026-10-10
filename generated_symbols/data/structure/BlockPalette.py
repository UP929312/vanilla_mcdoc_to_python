"""
Generated from symbols.json for ::java::data::structure::BlockPalette
Local link to file: generated_symbols/data/structure/BlockPalette.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


class BlockPaletteStruct1(GeneratedModel):
    palette: list[BlockState]


class BlockPaletteStruct2(GeneratedModel):
    palettes: list[list[BlockState]]  # Sets of different block states used in the structure, a random palette gets selected based on coordinates.


type BlockPalette = BlockPaletteStruct1 | BlockPaletteStruct2


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::structure::BlockPalette": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "palette",
                        "type": {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::util::block_state::BlockState"
                            }
                        }
                    }
                ]
            },
            {
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
        ]
    }
}
