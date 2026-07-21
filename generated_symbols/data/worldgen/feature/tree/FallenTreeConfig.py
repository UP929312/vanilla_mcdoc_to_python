# Generated from symbols.json for ::java::data::worldgen::feature::tree::FallenTreeConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider
    from generated_symbols.data.worldgen.feature.tree.TreeDecorator import TreeDecorator


@dataclass(kw_only=True)
class FallenTreeConfig:
    trunk_provider: BlockStateProvider
    log_length: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    stump_decorators: list[TreeDecorator]
    log_decorators: list[TreeDecorator]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::FallenTreeConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "trunk_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            },
            {
                "kind": "pair",
                "key": "log_length",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 16
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "stump_decorators",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::feature::tree::TreeDecorator"
                    }
                }
            },
            {
                "kind": "pair",
                "key": "log_decorators",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::feature::tree::TreeDecorator"
                    }
                }
            }
        ]
    }
}

