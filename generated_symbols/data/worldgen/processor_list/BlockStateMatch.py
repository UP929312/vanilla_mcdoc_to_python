# Generated from symbols.json for ::java::data::worldgen::processor_list::BlockStateMatch
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class BlockStateMatch:
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

