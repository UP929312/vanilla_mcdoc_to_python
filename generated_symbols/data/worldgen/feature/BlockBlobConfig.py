"""
Generated from symbols.json for ::java::data::worldgen::feature::BlockBlobConfig
Local link to file: generated_symbols/data/worldgen/feature/BlockBlobConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from generated_symbols.util.block_state.BlockState import BlockState


class BlockBlobConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    state: BlockState
    can_place_on: BlockPredicate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::BlockBlobConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "can_place_on",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::BlockPredicate"
                }
            }
        ]
    }
}

