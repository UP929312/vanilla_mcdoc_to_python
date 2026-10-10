"""
Generated from symbols.json for ::java::util::block_state::FullBlockState
Local link to file: vanilla_mcdoc/util/block_state/FullBlockState.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class FullBlockState(GeneratedModel):
    id: Annotated[str, IdSpec(registry='block')] | KnownBlockId
    properties: dict[str, str] | None = None
