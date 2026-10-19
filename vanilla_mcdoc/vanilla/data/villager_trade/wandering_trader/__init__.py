"""Vanilla's data/villager_trade/wandering_trader/ files"""
from vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionDiscard, LootFunctionEnchantWithLevels, LootFunctionFiltered, LootFunctionSetPotion
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.component.DataComponentExactPredicate import DataComponentExactPredicate
from vanilla_mcdoc.world.component.item.PotionContents import PotionContents
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

BAKED_POTATO_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:baked_potato', count=4),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=2,
    reputation_discount=0.05,
)

EMERALD_ACACIA_LOG = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:acacia_log', count=8),
    reputation_discount=0.05,
)

EMERALD_ACACIA_SAPLING = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:acacia_sapling'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_ALLIUM = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:allium'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_AZURE_BLUET = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:azure_bluet'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_BEETROOT_SEEDS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:beetroot_seeds'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_BIRCH_LOG = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:birch_log', count=8),
    reputation_discount=0.05,
)

EMERALD_BIRCH_SAPLING = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:birch_sapling'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_BLACK_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:black_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_BLUE_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:blue_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_BLUE_ICE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=6),
    gives=ItemStackOfComponent(id='minecraft:blue_ice'),
    max_uses=6,
    reputation_discount=0.05,
)

EMERALD_BLUE_ORCHID = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:blue_orchid'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_BRAIN_CORAL_BLOCK = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:brain_coral_block'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_BROWN_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:brown_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_BROWN_MUSHROOM = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:brown_mushroom', count=3),
    reputation_discount=0.05,
)

EMERALD_BUBBLE_CORAL_BLOCK = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:bubble_coral_block'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_CACTUS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:cactus'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_CHERRY_LOG = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:cherry_log', count=8),
    reputation_discount=0.05,
)

EMERALD_CHERRY_SAPLING = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:cherry_sapling'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_CORNFLOWER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:cornflower'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_CYAN_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:cyan_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_DANDELION = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:dandelion'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_DARK_OAK_LOG = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:dark_oak_log', count=8),
    reputation_discount=0.05,
)

EMERALD_DARK_OAK_SAPLING = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:dark_oak_sapling'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_DRY_TALL_GRASS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:tall_dry_grass'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_ENCHANTED_IRON_PICKAXE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:iron_pickaxe'),
    given_item_modifier=[
        LootFunctionEnchantWithLevels(
            levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=19),
            options='#minecraft:on_traded_equipment',
            include_additional_cost_component=True,
            type='minecraft:enchant_with_levels',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_pickaxe',
                predicates={'minecraft:enchantments': [EnchantmentPredicate()]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=1,
    reputation_discount=0.2,
)

EMERALD_FERN = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:fern'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_FIREFLY_BUSH = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:firefly_bush'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_FIRE_CORAL_BLOCK = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:fire_coral_block'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_FISH_BUCKET = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:tropical_fish_bucket'),
    reputation_discount=0.05,
)

EMERALD_GLOWSTONE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:glowstone'),
    max_uses=5,
    reputation_discount=0.05,
)

EMERALD_GOLDEN_DANDELION = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:golden_dandelion'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_GRAY_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:gray_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_GREEN_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:green_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_GUNPOWDER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:gunpowder', count=4),
    max_uses=2,
    reputation_discount=0.05,
)

EMERALD_HORN_CORAL_BLOCK = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:horn_coral_block'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_ICE_CRYSTAL = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:ice_crystal'),
    max_uses=5,
    reputation_discount=0.05,
)

EMERALD_ICICLE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:icicle', count=2),
    max_uses=5,
    reputation_discount=0.05,
)

EMERALD_JUNGLE_LOG = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:jungle_log', count=8),
    reputation_discount=0.05,
)

EMERALD_JUNGLE_SAPLING = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:jungle_sapling'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_KELP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:kelp'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_LIGHT_BLUE_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:light_blue_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_LIGHT_GRAY_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:light_gray_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_LILY_OF_THE_VALLEY = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:lily_of_the_valley'),
    max_uses=7,
    reputation_discount=0.05,
)

EMERALD_LILY_PAD = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:lily_pad', count=5),
    max_uses=2,
    reputation_discount=0.05,
)

EMERALD_LIME_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:lime_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_LONG_INVISIBILITY_POTION = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:potion'),
    given_item_modifier=LootFunctionSetPotion(id='minecraft:long_invisibility', type='minecraft:set_potion'),
    max_uses=1,
    reputation_discount=0.05,
)

EMERALD_MAGENTA_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:magenta_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_MANGROVE_LOG = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:mangrove_log', count=8),
    reputation_discount=0.05,
)

EMERALD_MANGROVE_PROPAGULE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:mangrove_propagule'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_MELON_SEEDS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:melon_seeds'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_MOSS_BLOCK = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:moss_block', count=2),
    max_uses=5,
    reputation_discount=0.05,
)

EMERALD_NAME_TAG = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:name_tag'),
    max_uses=5,
    reputation_discount=0.05,
)

EMERALD_NAUTILUS_SHELL = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:nautilus_shell'),
    max_uses=5,
    reputation_discount=0.05,
)

EMERALD_OAK_LOG = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:oak_log', count=8),
    reputation_discount=0.05,
)

EMERALD_OAK_SAPLING = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:oak_sapling'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_OPEN_EYEBLOSSOM = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:open_eyeblossom'),
    max_uses=7,
    reputation_discount=0.05,
)

EMERALD_ORANGE_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:orange_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_ORANGE_TULIP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:orange_tulip'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_OXEYE_DAISY = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:oxeye_daisy'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_PACKED_ICE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:packed_ice'),
    max_uses=6,
    reputation_discount=0.05,
)

EMERALD_PALE_HANGING_MOSS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:pale_hanging_moss', count=3),
    reputation_discount=0.05,
)

EMERALD_PALE_MOSS_BLOCK = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:pale_moss_block', count=2),
    max_uses=5,
    reputation_discount=0.05,
)

EMERALD_PALE_OAK_LOG = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:pale_oak_log', count=8),
    reputation_discount=0.05,
)

EMERALD_PALE_OAK_SAPLING = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:pale_oak_sapling'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_PINK_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:pink_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_PINK_TULIP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:pink_tulip'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_PODZOL = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:podzol', count=3),
    max_uses=6,
    reputation_discount=0.05,
)

EMERALD_POINTED_DRIPSTONE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:pointed_dripstone', count=2),
    max_uses=5,
    reputation_discount=0.05,
)

EMERALD_POPLAR_LOG = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:poplar_log', count=8),
    reputation_discount=0.05,
)

EMERALD_POPLAR_SAPLING = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:poplar_sapling'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_POPPY = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:poppy'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_PUFFERFISH_BUCKET = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:pufferfish_bucket'),
    reputation_discount=0.05,
)

EMERALD_PUMPKIN = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:pumpkin'),
    reputation_discount=0.05,
)

EMERALD_PUMPKIN_SEEDS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:pumpkin_seeds'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_PURPLE_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:purple_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_RED_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:red_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_RED_MUSHROOM = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:red_mushroom', count=3),
    reputation_discount=0.05,
)

EMERALD_RED_SAND = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:red_sand', count=4),
    max_uses=6,
    reputation_discount=0.05,
)

EMERALD_RED_TULIP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:red_tulip'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_ROOTED_DIRT = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:rooted_dirt', count=2),
    max_uses=5,
    reputation_discount=0.05,
)

EMERALD_SAND = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:sand', count=8),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_SEA_PICKLE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:sea_pickle'),
    max_uses=5,
    reputation_discount=0.05,
)

EMERALD_SHELF_MUSHROOM = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:shelf_mushroom', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_SLIME_BALL = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=4),
    gives=ItemStackOfComponent(id='minecraft:slime_ball'),
    max_uses=5,
    reputation_discount=0.05,
)

EMERALD_SMALL_DRIPLEAF = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:small_dripleaf', count=2),
    max_uses=5,
    reputation_discount=0.05,
)

EMERALD_SPRUCE_LOG = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:spruce_log', count=8),
    reputation_discount=0.05,
)

EMERALD_SPRUCE_SAPLING = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:spruce_sapling'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_SUGAR_CANE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:sugar_cane'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_SULFUR_SPIKE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:sulfur_spike', count=2),
    max_uses=5,
    reputation_discount=0.05,
)

EMERALD_TUBE_CORAL_BLOCK = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:tube_coral_block'),
    max_uses=8,
    reputation_discount=0.05,
)

EMERALD_VINE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:vine', count=3),
    reputation_discount=0.05,
)

EMERALD_WHEAT_SEEDS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:wheat_seeds'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_WHITE_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:white_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_WHITE_TULIP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:white_tulip'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_WILDFLOWERS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:wildflowers'),
    max_uses=12,
    reputation_discount=0.05,
)

EMERALD_YELLOW_DYE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:yellow_dye', count=3),
    max_uses=12,
    reputation_discount=0.05,
)

FERMENTED_SPIDER_EYE_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:fermented_spider_eye'),
    gives=ItemStackOfComponent(id='minecraft:emerald', count=3),
    max_uses=2,
    reputation_discount=0.05,
)

HAY_BLOCK_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:hay_block'),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=2,
    reputation_discount=0.05,
)

MILK_BUCKET_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:milk_bucket'),
    gives=ItemStackOfComponent(id='minecraft:emerald', count=2),
    max_uses=2,
    reputation_discount=0.05,
)

WATER_BOTTLE_EMERALD = VillagerTrade(
    wants=TradeCost(
        id='minecraft:potion',
        components=DataComponentExactPredicate(potion_contents=PotionContents(potion='minecraft:water')),
    ),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=2,
    reputation_discount=0.05,
)

WATER_BUCKET_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:water_bucket'),
    gives=ItemStackOfComponent(id='minecraft:emerald', count=2),
    max_uses=2,
    reputation_discount=0.05,
)
