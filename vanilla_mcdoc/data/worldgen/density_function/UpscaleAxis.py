"""
Generated from symbols.json for ::java::data::worldgen::density_function::UpscaleAxis
Local link to file: vanilla_mcdoc/data/worldgen/density_function/UpscaleAxis.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.UpscaleMode import UpscaleMode


class UpscaleAxis(GeneratedModel):
    mode: UpscaleMode
    cell_size: Annotated[int, Field(ge=1, le=64)]
