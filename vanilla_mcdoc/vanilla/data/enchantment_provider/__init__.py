"""Vanilla's data/enchantment_provider/ files"""
from vanilla_mcdoc.data.enchantment.provider.EnchantmentProvider import EnchantmentProviderByCostWithDifficulty, EnchantmentProviderSingle

ENDERMAN_LOOT_DROP = EnchantmentProviderSingle(enchantment='minecraft:silk_touch', level=1, type='minecraft:single')

MOB_SPAWN_EQUIPMENT = EnchantmentProviderByCostWithDifficulty(
    enchantments='#minecraft:on_mob_spawn_equipment',
    min_cost=5,
    max_cost_span=17,
    type='minecraft:by_cost_with_difficulty',
)

PILLAGER_SPAWN_CROSSBOW = EnchantmentProviderSingle(enchantment='minecraft:piercing', level=1, type='minecraft:single')
