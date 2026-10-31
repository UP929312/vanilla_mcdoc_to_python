"""
Generated from symbols.json for ::java::data::worldgen::template_pool::ElementBase
Local link to file: vanilla_mcdoc/data/worldgen/template_pool/ElementBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.template_pool.DensityPredicate import DensityPredicate
    from vanilla_mcdoc.data.worldgen.template_pool.Projection import Projection


class ElementBase(GeneratedModel):
    projection: Projection
    corner_constraint: Annotated[list[DensityPredicate], Field(min_length=1, max_length=10)] | None = None
