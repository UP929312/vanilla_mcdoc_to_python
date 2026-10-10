"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::PlaceOnGroundTreeDecorator
Local link to file: generated_symbols/data/worldgen/feature/tree/PlaceOnGroundTreeDecorator.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class PlaceOnGroundTreeDecorator(GeneratedModel):
    tries: Annotated[int, Field(ge=1)] | None = None  # Defaults to `128`.
    radius: Annotated[int, Field(ge=0)] | None = None  # Defaults to `2`.
    height: Annotated[int, Field(ge=0)] | None = None  # Defaults to `1`.
    block_state_provider: BlockStateProviderRef  # The block to place on the ground.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::PlaceOnGroundTreeDecorator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Defaults to `128`.",
                "key": "tries",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to `2`.",
                "key": "radius",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to `1`.",
                "key": "height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The block to place on the ground.",
                "key": "block_state_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef"
                }
            }
        ]
    }
}
