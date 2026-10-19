"""Vanilla's data/tags/enchantment/ files"""
from vanilla_mcdoc.data.tag.Tag import Tag

CURSE = Tag(values=['minecraft:binding_curse', 'minecraft:vanishing_curse'])

DOUBLE_TRADE_PRICE = Tag(values=['#minecraft:treasure'])

IN_ENCHANTING_TABLE = Tag(values=['#minecraft:non_treasure'])

NON_TREASURE = Tag(
    values=[
        'minecraft:protection',
        'minecraft:fire_protection',
        'minecraft:feather_falling',
        'minecraft:blast_protection',
        'minecraft:projectile_protection',
        'minecraft:respiration',
        'minecraft:aqua_affinity',
        'minecraft:thorns',
        'minecraft:depth_strider',
        'minecraft:sharpness',
        'minecraft:smite',
        'minecraft:bane_of_arthropods',
        'minecraft:knockback',
        'minecraft:fire_aspect',
        'minecraft:looting',
        'minecraft:sweeping_edge',
        'minecraft:efficiency',
        'minecraft:silk_touch',
        'minecraft:unbreaking',
        'minecraft:fortune',
        'minecraft:power',
        'minecraft:punch',
        'minecraft:flame',
        'minecraft:infinity',
        'minecraft:luck_of_the_sea',
        'minecraft:lure',
        'minecraft:loyalty',
        'minecraft:impaling',
        'minecraft:riptide',
        'minecraft:channeling',
        'minecraft:multishot',
        'minecraft:quick_charge',
        'minecraft:piercing',
        'minecraft:density',
        'minecraft:breach',
        'minecraft:lunge',
    ],
)

ON_MOB_SPAWN_EQUIPMENT = Tag(values=['#minecraft:non_treasure'])

ON_RANDOM_LOOT = Tag(
    values=[
        '#minecraft:non_treasure',
        'minecraft:binding_curse',
        'minecraft:vanishing_curse',
        'minecraft:frost_walker',
        'minecraft:mending',
    ],
)

ON_TRADED_EQUIPMENT = Tag(values=['#minecraft:non_treasure'])

PREVENTS_BEE_SPAWNS_WHEN_MINING = Tag(values=['minecraft:silk_touch'])

PREVENTS_DECORATED_POT_SHATTERING = Tag(values=['minecraft:silk_touch'])

PREVENTS_ICE_MELTING = Tag(values=['minecraft:silk_touch'])

PREVENTS_INFESTED_SPAWNS = Tag(values=['minecraft:silk_touch'])

SMELTS_LOOT = Tag(values=['minecraft:fire_aspect'])

TOOLTIP_ORDER = Tag(
    values=[
        'minecraft:binding_curse',
        'minecraft:vanishing_curse',
        'minecraft:riptide',
        'minecraft:channeling',
        'minecraft:wind_burst',
        'minecraft:frost_walker',
        'minecraft:lunge',
        'minecraft:sharpness',
        'minecraft:smite',
        'minecraft:bane_of_arthropods',
        'minecraft:impaling',
        'minecraft:power',
        'minecraft:density',
        'minecraft:breach',
        'minecraft:piercing',
        'minecraft:sweeping_edge',
        'minecraft:multishot',
        'minecraft:fire_aspect',
        'minecraft:flame',
        'minecraft:knockback',
        'minecraft:punch',
        'minecraft:protection',
        'minecraft:blast_protection',
        'minecraft:fire_protection',
        'minecraft:projectile_protection',
        'minecraft:feather_falling',
        'minecraft:fortune',
        'minecraft:looting',
        'minecraft:silk_touch',
        'minecraft:luck_of_the_sea',
        'minecraft:efficiency',
        'minecraft:quick_charge',
        'minecraft:lure',
        'minecraft:respiration',
        'minecraft:aqua_affinity',
        'minecraft:soul_speed',
        'minecraft:swift_sneak',
        'minecraft:depth_strider',
        'minecraft:thorns',
        'minecraft:loyalty',
        'minecraft:unbreaking',
        'minecraft:infinity',
        'minecraft:mending',
    ],
)

TRADEABLE = Tag(
    values=[
        '#minecraft:non_treasure',
        'minecraft:binding_curse',
        'minecraft:vanishing_curse',
        'minecraft:frost_walker',
        'minecraft:mending',
    ],
)

TREASURE = Tag(
    values=[
        'minecraft:binding_curse',
        'minecraft:vanishing_curse',
        'minecraft:swift_sneak',
        'minecraft:soul_speed',
        'minecraft:frost_walker',
        'minecraft:mending',
        'minecraft:wind_burst',
    ],
)
