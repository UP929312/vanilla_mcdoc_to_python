"""
Generated from symbols.json for ::java::data::worldgen::processor_list::BlockStateMatch
Local link to file: generated_symbols/data/worldgen/processor_list/BlockStateMatch.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


class BlockStateMatch(GeneratedModel):
    block_state: BlockState


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::BlockStateMatch": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "block_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            }
        ]
    }
}

