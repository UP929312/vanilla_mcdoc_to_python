"""
Generated from symbols.json for ::java::data::trim::OldTrimMaterialOverrides
Local link to file: vanilla_mcdoc/data/trim/OldTrimMaterialOverrides.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.minecraft_types import NamespacedId

if TYPE_CHECKING:
    from vanilla_mcdoc.data.trim.ArmorMaterial import ArmorMaterial


type OldTrimMaterialOverrides = dict[NamespacedId[ArmorMaterial], str]
