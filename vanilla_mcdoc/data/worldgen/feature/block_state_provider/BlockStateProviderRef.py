"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef
Local link to file: generated_symbols/data/worldgen/feature/block_state_provider/BlockStateProviderRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider


type BlockStateProviderRef = BlockStateProvider | Annotated[str, IdSpec(registry='worldgen/block_state_provider')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
            },
            {
                "kind": "string",
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
                    },
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "worldgen/block_state_provider"
                            }
                        }
                    }
                ]
            }
        ]
    }
}
