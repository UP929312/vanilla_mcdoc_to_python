"""
Generated from symbols.json for ::java::data::worldgen::structure::JigsawDistanceLimits
Local link to file: vanilla_mcdoc/data/worldgen/structure/JigsawDistanceLimits.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Generic, TypeVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class JigsawDistanceLimits(GeneratedModel, Generic[T]):
    horizontal: T
    vertical: Annotated[int, Field(ge=1, le=4064)] | None = None  # Defaults to 4064
