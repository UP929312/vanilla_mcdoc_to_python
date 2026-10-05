"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::BlockStateProvider
Local link to file: generated_symbols/data/worldgen/feature/block_state_provider/BlockStateProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.TypedBlockStateProvider import TypedBlockStateProvider
    from generated_symbols.util.block_state.FullBlockState import FullBlockState


type BlockStateProvider = TypedBlockStateProvider | FullBlockState


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_state_provider::BlockStateProvider": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::worldgen::feature::block_state_provider::TypedBlockStateProvider"
            },
            {
                "kind": "reference",
                "path": "::java::util::block_state::FullBlockState",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

