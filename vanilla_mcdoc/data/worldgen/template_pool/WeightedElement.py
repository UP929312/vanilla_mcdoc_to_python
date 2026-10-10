"""
Generated from symbols.json for ::java::data::worldgen::template_pool::WeightedElement
Local link to file: vanilla_mcdoc/data/worldgen/template_pool/WeightedElement.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.template_pool.Element import Element


class WeightedElement(GeneratedModel):
    weight: Annotated[int, Field(ge=1, le=150)]
    element: Element
