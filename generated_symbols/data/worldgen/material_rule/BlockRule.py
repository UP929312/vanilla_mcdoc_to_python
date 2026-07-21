# Generated from symbols.json for ::java::data::worldgen::material_rule::BlockRule
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class BlockRule:
    result_state: BlockState


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::material_rule::BlockRule": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "result_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            }
        ]
    }
}

