"""
Generated from symbols.json for ::java::data::worldgen::feature::BlockColumnConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/BlockColumnConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.BlockColumnLayer import BlockColumnLayer
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.util.direction.Direction import Direction


class BlockColumnConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

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
