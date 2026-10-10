"""
Generated from symbols.json for ::java::assets::texture_meta::NineSliceBorder
Local link to file: vanilla_mcdoc/assets/texture_meta/NineSliceBorder.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class NineSliceBorder(GeneratedModel):
    left: Annotated[int, Field(ge=0)]
    top: Annotated[int, Field(ge=0)]
    right: Annotated[int, Field(ge=0)]
    bottom: Annotated[int, Field(ge=0)]
