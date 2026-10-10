"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::VolumeMatchPredicate
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_predicate/VolumeMatchPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate


class VolumeMatchPredicate(GeneratedModel):
    min: tuple[Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)]]
    max: tuple[Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)]]
    match: BlockPredicate
