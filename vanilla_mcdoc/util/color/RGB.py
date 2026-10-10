"""
Generated from symbols.json for ::java::util::color::RGB
Local link to file: vanilla_mcdoc/util/color/RGB.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field


type RGB = int | tuple[Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)]]
