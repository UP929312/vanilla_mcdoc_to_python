"""
Generated from symbols.json for ::java::data::worldgen::processor_list::RandomBlockMatch
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/RandomBlockMatch.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class RandomBlockMatch(GeneratedModel):
    block: Annotated[str, IdSpec(registry='block')] | KnownBlockId
    probability: Annotated[float, Field(ge=0, le=1)]
