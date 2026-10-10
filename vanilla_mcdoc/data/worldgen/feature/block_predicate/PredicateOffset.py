"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::PredicateOffset
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_predicate/PredicateOffset.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class PredicateOffset(GeneratedModel):
    offset: tuple[Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)]] | None = None  # The block offset to check.
