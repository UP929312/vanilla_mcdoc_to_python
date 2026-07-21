# Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::RandomizedIntStateProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider


@dataclass(kw_only=True)
class RandomizedIntStateProvider:
    property: str
    values: IntProvider[int] | int
    source: BlockStateProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_state_provider::RandomizedIntStateProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "property",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "key": "values",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "source",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            }
        ]
    }
}

