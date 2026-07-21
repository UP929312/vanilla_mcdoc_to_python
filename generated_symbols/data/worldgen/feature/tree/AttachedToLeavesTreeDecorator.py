# Generated from symbols.json for ::java::data::worldgen::feature::tree::AttachedToLeavesTreeDecorator
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider
    from generated_symbols.util.direction.Direction import Direction


@dataclass(kw_only=True)
class AttachedToLeavesTreeDecorator:
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']
    exclusion_radius_xz: Annotated[int, 'Range | `0`-`16` | both inclusive']
    exclusion_radius_y: Annotated[int, 'Range | `0`-`16` | both inclusive']
    required_empty_blocks: Annotated[int, 'Range | `1`-`16` | both inclusive']
    block_provider: BlockStateProvider
    directions: Annotated[list[Direction], 'Length = 1 (inclusive) and above']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::AttachedToLeavesTreeDecorator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "exclusion_radius_xz",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 16
                    }
                }
            },
            {
                "kind": "pair",
                "key": "exclusion_radius_y",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 16
                    }
                }
            },
            {
                "kind": "pair",
                "key": "required_empty_blocks",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 16
                    }
                }
            },
            {
                "kind": "pair",
                "key": "block_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            },
            {
                "kind": "pair",
                "key": "directions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::direction::Direction"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}

