"""
Generated from symbols.json for ::java::data::worldgen::material_rule::OreVeinifier
Local link to file: generated_symbols/data/worldgen/material_rule/OreVeinifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from generated_symbols.util.block_state.BlockState import BlockState


class OreVeinifier(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_rule'

    ore_block: BlockState
    raw_ore_block: BlockState
    filler_block: BlockState
    raw_ore_chance: Annotated[float, Field(ge=0, le=1)]
    density: DensityFunctionRef
    richness: DensityFunctionRef
    filler_gap: DensityFunctionRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::material_rule::OreVeinifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "ore_block",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "raw_ore_block",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "filler_block",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "raw_ore_chance",
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
                "key": "density",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "richness",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "filler_gap",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            }
        ]
    }
}

