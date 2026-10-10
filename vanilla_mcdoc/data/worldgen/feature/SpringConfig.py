"""
Generated from symbols.json for ::java::data::worldgen::feature::SpringConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/SpringConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId
    from vanilla_mcdoc.util.fluid_state.FluidState import FluidState


class SpringConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    state: FluidState
    rock_count: int
    hole_count: int
    requires_block_below: bool
    valid_blocks: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId
