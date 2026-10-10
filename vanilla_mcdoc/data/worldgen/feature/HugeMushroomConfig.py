"""
Generated from symbols.json for ::java::data::worldgen::feature::HugeMushroomConfig
Local link to file: generated_symbols/data/worldgen/feature/HugeMushroomConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class HugeMushroomConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    cap_provider: BlockStateProviderRef
    stem_provider: BlockStateProviderRef
    foliage_radius: int
    can_place_on: BlockPredicate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::HugeMushroomConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "cap_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef"
                }
            },
            {
                "kind": "pair",
                "key": "stem_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef"
                }
            },
            {
                "kind": "pair",
                "key": "foliage_radius",
                "type": {
                    "kind": "int"
                }
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
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "key": "can_place_on",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::BlockPredicate"
                }
            }
        ]
    }
}
