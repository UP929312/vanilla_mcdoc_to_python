"""
Generated from symbols.json for ::java::data::worldgen::dimension::chunk_generator::FlatGeneratorLayer
Local link to file: vanilla_mcdoc/data/worldgen/dimension/chunk_generator/FlatGeneratorLayer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class FlatGeneratorLayer(GeneratedModel):
    height: Annotated[int, Field(ge=0, le=4096)]
    block: Annotated[str, IdSpec(registry='block')] | KnownBlockId
