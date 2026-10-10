"""
Generated from symbols.json for ::java::world::component::item::EnchantmentLevels
Local link to file: vanilla_mcdoc/world/component/item/EnchantmentLevels.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.minecraft_types import IdSpec


type EnchantmentLevels = dict[Annotated[str, IdSpec(registry='enchantment')], Annotated[int, Field(ge=1, le=255)]]
