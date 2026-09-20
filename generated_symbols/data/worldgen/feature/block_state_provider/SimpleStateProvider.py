"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::SimpleStateProvider
Local link to file: generated_symbols/data/worldgen/feature/block_state_provider/SimpleStateProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


class SimpleStateProvider(GeneratedModel):
    state: BlockState


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_state_provider::SimpleStateProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            }
        ]
    }
}

