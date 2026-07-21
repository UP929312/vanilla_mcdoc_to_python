# Generated from symbols.json for ::java::data::worldgen::processor_list::BlockIgnore
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class BlockIgnore:
    blocks: list[BlockState]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::BlockIgnore": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "blocks",
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

