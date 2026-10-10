"""
Generated from symbols.json for ::java::data::worldgen::processor_list::TagMatch
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/TagMatch.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class TagMatch(GeneratedModel):
    tag: Annotated[str, IdSpec(registry='block', tags='implicit')] | KnownBlockId
