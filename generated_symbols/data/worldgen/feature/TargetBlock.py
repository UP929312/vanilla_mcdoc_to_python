# Generated from symbols.json for ::java::data::worldgen::feature::TargetBlock
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.RuleTest import RuleTest
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class TargetBlock:
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

