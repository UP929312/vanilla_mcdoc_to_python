"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::AttachedToLeavesTreeDecorator
Local link to file: generated_symbols/data/worldgen/feature/tree/AttachedToLeavesTreeDecorator.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from generated_symbols.util.direction.Direction import Direction


class AttachedToLeavesTreeDecorator(GeneratedModel):
    probability: Annotated[float, Field(ge=0, le=1)]
    exclusion_radius_xz: Annotated[int, Field(ge=0, le=16)]
    exclusion_radius_y: Annotated[int, Field(ge=0, le=16)]
    required_empty_blocks: Annotated[int, Field(ge=1, le=16)]
    block_provider: BlockStateProviderRef
    directions: Annotated[list[Direction], Field(min_length=1)]


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
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef"
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
