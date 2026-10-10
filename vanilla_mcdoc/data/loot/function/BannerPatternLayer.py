"""
Generated from symbols.json for ::java::data::loot::function::BannerPatternLayer
Local link to file: vanilla_mcdoc/data/loot/function/BannerPatternLayer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.DyeColor import DyeColor


class BannerPatternLayer(GeneratedModel):
    pattern: Annotated[str, IdSpec(registry='banner_pattern')]
    color: DyeColor
