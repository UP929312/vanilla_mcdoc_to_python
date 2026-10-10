"""
Generated from symbols.json for ::java::util::color::StringRGB
Local link to file: vanilla_mcdoc/util/color/StringRGB.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field


type StringRGB = int | tuple[Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)]] | Annotated[str, Field(pattern='^#')]
