"""
Generated from symbols.json for ::java::data::worldgen::material_rule::OreVeinifier
Local link to file: vanilla_mcdoc/data/worldgen/material_rule/OreVeinifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class OreVeinifier(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_rule'

    ore_block: BlockState
    raw_ore_block: BlockState
    filler_block: BlockState
    raw_ore_chance: Annotated[float, Field(ge=0, le=1)]
    density: DensityFunctionRef
    richness: DensityFunctionRef
    filler_gap: DensityFunctionRef
