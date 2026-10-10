"""
Generated from symbols.json for ::java::world::component::item::Enchantments
Local link to file: vanilla_mcdoc/world/component/item/Enchantments.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.EnchantmentLevels import EnchantmentLevels


class Enchantments(GeneratedModel):
    levels: EnchantmentLevels
    show_in_tooltip: bool | None = None
