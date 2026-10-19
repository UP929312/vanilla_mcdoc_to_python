"""Vanilla's data/enchantment_provider/raid/ files"""
from vanilla_mcdoc.data.enchantment.provider.EnchantmentProvider import EnchantmentProviderSingle

PILLAGER_POST_WAVE_3 = EnchantmentProviderSingle(enchantment='minecraft:quick_charge', level=1, type='minecraft:single')

PILLAGER_POST_WAVE_5 = EnchantmentProviderSingle(enchantment='minecraft:quick_charge', level=2, type='minecraft:single')

VINDICATOR = EnchantmentProviderSingle(enchantment='minecraft:sharpness', level=1, type='minecraft:single')

VINDICATOR_POST_WAVE_5 = EnchantmentProviderSingle(enchantment='minecraft:sharpness', level=2, type='minecraft:single')
