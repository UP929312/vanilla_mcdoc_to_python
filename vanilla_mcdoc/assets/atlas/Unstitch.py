"""
Generated from symbols.json for ::java::assets::atlas::Unstitch
Local link to file: vanilla_mcdoc/assets/atlas/Unstitch.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.atlas.UnstitchRegion import UnstitchRegion


class Unstitch(GeneratedModel):
    resource: Annotated[str, IdSpec(registry='texture')]
    divisor_x: float | None = None  # If set to the resource width, regions will use pixel coordinates.
    divisor_y: float | None = None  # If set to the resource height, regions will use pixel coordinates.
    regions: list[UnstitchRegion]
