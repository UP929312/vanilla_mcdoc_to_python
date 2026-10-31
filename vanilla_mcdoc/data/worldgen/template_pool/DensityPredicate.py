"""
Generated from symbols.json for ::java::data::worldgen::template_pool::DensityPredicate
Local link to file: vanilla_mcdoc/data/worldgen/template_pool/DensityPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.template_pool.CornersToCheck import CornersToCheck
    from vanilla_mcdoc.util.InclusiveRange import InclusiveRange


class DensityPredicate(GeneratedModel):
    density_function: Annotated[str, IdSpec(registry='worldgen/density_function')]
    acceptable_density: InclusiveRange[float] | float | tuple[float, float]
    padding: Annotated[int, Field(ge=0, le=8)] | None = None  # Defaults to 0.
    corners: CornersToCheck | None = None  # Defaults to `all`.
    required_corners: Annotated[int, Field(ge=1, le=8)]
