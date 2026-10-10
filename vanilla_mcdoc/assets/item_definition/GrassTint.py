"""
Generated from symbols.json for ::java::assets::item_definition::GrassTint
Local link to file: vanilla_mcdoc/assets/item_definition/GrassTint.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class GrassTint(GeneratedModel):
    temperature: Annotated[float, Field(ge=0, le=1)]
    downfall: Annotated[float, Field(ge=0, le=1)]
