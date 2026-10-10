"""
Generated from symbols.json for ::java::pack::PackFormat
Local link to file: vanilla_mcdoc/pack/PackFormat.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field


type PackFormat = int | tuple[int] | tuple[int, Annotated[int, Field(ge=0)]]
