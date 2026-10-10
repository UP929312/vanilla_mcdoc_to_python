"""
Generated from symbols.json for ::java::data::worldgen::processor_list::BlockRot
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/BlockRot.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class BlockRot(GeneratedModel):
    integrity: Annotated[float, Field(ge=0, le=1)]
    rottable_blocks: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | None = None
