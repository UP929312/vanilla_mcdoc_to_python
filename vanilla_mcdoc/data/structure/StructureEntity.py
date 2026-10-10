"""
Generated from symbols.json for ::java::data::structure::StructureEntity
Local link to file: vanilla_mcdoc/data/structure/StructureEntity.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.AnyEntity import AnyEntity


class StructureEntity(GeneratedModel):
    pos: tuple[Annotated[float, Field(ge=0)], Annotated[float, Field(ge=0)], Annotated[float, Field(ge=0)]]
    blockPos: tuple[Annotated[int, Field(ge=0)], Annotated[int, Field(ge=0)], Annotated[int, Field(ge=0)]]
    nbt: AnyEntity
