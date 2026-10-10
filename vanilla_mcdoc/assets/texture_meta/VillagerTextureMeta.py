"""
Generated from symbols.json for ::java::assets::texture_meta::VillagerTextureMeta
Local link to file: vanilla_mcdoc/assets/texture_meta/VillagerTextureMeta.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.texture_meta.VillagerHatType import VillagerHatType


class VillagerTextureMeta(GeneratedModel):
    hat: VillagerHatType | None = None  # Determines whether the villager's 'profession' hat layer should allow the 'type' hat layer to render or not.  Defaults to `none`.
