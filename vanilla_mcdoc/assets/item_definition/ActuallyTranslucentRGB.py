"""
Generated from symbols.json for ::java::assets::item_definition::ActuallyTranslucentRGB
Local link to file: vanilla_mcdoc/assets/item_definition/ActuallyTranslucentRGB.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field


type ActuallyTranslucentRGB = int | tuple[Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)]]
