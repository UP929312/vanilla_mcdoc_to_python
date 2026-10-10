"""
Generated from symbols.json for ::java::data::worldgen::processor_list::BlockMatch
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/BlockMatch.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class BlockMatch(GeneratedModel):
    block: Annotated[str, IdSpec(registry='block')] | KnownBlockId
