"""
Generated from symbols.json for ::java::data::worldgen::feature::TargetBlock
Local link to file: generated_symbols/data/worldgen/feature/TargetBlock.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.RuleTest import RuleTest
    from generated_symbols.util.block_state.BlockState import BlockState


class TargetBlock(GeneratedModel):
    target: RuleTest
    state: BlockState


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::TargetBlock": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "target",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::processor_list::RuleTest"
                }
            },
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

