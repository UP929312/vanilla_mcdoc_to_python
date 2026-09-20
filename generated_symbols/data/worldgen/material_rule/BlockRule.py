"""
Generated from symbols.json for ::java::data::worldgen::material_rule::BlockRule
Local link to file: generated_symbols/data/worldgen/material_rule/BlockRule.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


class BlockRule(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_rule'

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

