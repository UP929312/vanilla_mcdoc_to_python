"""
Generated from symbols.json for ::java::data::worldgen::density_function::NoiseRange
Local link to file: vanilla_mcdoc/data/worldgen/density_function/NoiseRange.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field


type NoiseRange = Annotated[float, Field(ge=-1000000, le=1000000)]
