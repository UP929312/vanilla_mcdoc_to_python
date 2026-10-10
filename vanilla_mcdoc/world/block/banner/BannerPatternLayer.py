"""
Generated from symbols.json for ::java::world::block::banner::BannerPatternLayer
Local link to file: vanilla_mcdoc/world/block/banner/BannerPatternLayer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.variants.banner_pattern.BannerPattern import BannerPattern
    from vanilla_mcdoc.util.DyeColor import DyeColor


class BannerPatternLayer(GeneratedModel):
    color: DyeColor  # The dye color of the pattern.
    pattern: Annotated[str, IdSpec(registry='banner_pattern')] | BannerPattern  # The banner pattern.
