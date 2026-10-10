"""
Generated from symbols.json for ::java::data::worldgen::BottomBiasHeightProvider
Local link to file: vanilla_mcdoc/data/worldgen/BottomBiasHeightProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.data.worldgen.UniformHeightProvider import UniformHeightProvider


class BottomBiasHeightProvider(UniformHeightProvider):
    inner: Annotated[int, Field(ge=1)] | None = None
