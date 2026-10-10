"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::RandomBlockStateProvider
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_state_provider/RandomBlockStateProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class RandomBlockStateProvider(GeneratedModel):
    blocks: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]
