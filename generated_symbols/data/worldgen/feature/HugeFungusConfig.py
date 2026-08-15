"""
Generated from symbols.json for ::java::data::worldgen::feature::HugeFungusConfig
Local link to file: generated_symbols/data/worldgen/feature/HugeFungusConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class HugeFungusConfig:
    hat_state: BlockState
    decor_state: BlockState
    stem_state: BlockState
    valid_base_block: BlockState
    planted: bool | None = None
    replaceable_blocks: BlockPredicate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::HugeFungusConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "hat_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "decor_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "stem_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "valid_base_block",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "planted",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20"
                            }
                        }
                    }
                ],
                "key": "replaceable_blocks",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::BlockPredicate"
                }
            }
        ]
    }
}

