"""
Generated from symbols.json for ::java::assets::item_definition::Banner
Local link to file: vanilla_mcdoc/assets/item_definition/Banner.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.BannerAttachment import BannerAttachment
    from vanilla_mcdoc.util.color.DyeColor import DyeColor


class Banner(GeneratedModel):
    color: DyeColor
    attachment: BannerAttachment | None = None  # Defaults to `ground`.
