# Generated from symbols.json for ::java::data::worldgen::feature::BlockColumnConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.BlockColumnLayer import BlockColumnLayer
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from generated_symbols.util.direction.Direction import Direction


@dataclass(kw_only=True)
class BlockColumnConfig:
    direction: Direction
    allowed_placement: BlockPredicate
    prioritize_tip: bool
    layers: list[BlockColumnLayer]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::BlockColumnConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "direction",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::direction::Direction"
                }
            },
            {
                "kind": "pair",
                "key": "allowed_placement",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::BlockPredicate"
                }
            },
            {
                "kind": "pair",
                "key": "prioritize_tip",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "key": "layers",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::feature::BlockColumnLayer"
                    }
                }
            }
        ]
    }
}

