"""
Generated from symbols.json for ::java::data::enchantment::provider::ByCostEnchantmentProvider
Local link to file: vanilla_mcdoc/data/enchantment/provider/ByCostEnchantmentProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.provider.EnchantmentsType import EnchantmentsType
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class ByCostEnchantmentProvider(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'enchantment_provider'

    enchantments: EnchantmentsType
    cost: IntProvider[int] | int  # Cost to use for the Enchanting process.
