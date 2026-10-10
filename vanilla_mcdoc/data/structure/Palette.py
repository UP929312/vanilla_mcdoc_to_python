"""
Generated from symbols.json for ::java::data::structure::Palette
Local link to file: vanilla_mcdoc/data/structure/Palette.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class Palette(GeneratedModel):
    palette: list[BlockState]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::structure::Palette": {
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
    }
}
