"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::MangroveRootPlacement
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/MangroveRootPlacement.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class MangroveRootPlacement(GeneratedModel):
    max_root_width: Annotated[int, Field(ge=1, le=12)]
    max_root_length: Annotated[int, Field(ge=1, le=64)]
    random_skew_chance: Annotated[float, Field(ge=0, le=1)]
    can_grow_through: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId
    muddy_roots_in: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId
    muddy_roots_provider: BlockStateProviderRef
