"""
Generated from symbols.json for ::java::util::color::StringARGB
Local link to file: vanilla_mcdoc/util/color/StringARGB.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field


type StringARGB = int | tuple[Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)]] | str
