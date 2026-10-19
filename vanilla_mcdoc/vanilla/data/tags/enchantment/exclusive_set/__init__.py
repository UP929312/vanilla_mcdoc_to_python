"""Vanilla's data/tags/enchantment/exclusive_set/ files"""
from vanilla_mcdoc.data.tag.Tag import Tag

ARMOR = Tag(
    values=[
        'minecraft:protection',
        'minecraft:blast_protection',
        'minecraft:fire_protection',
        'minecraft:projectile_protection',
    ],
)

BOOTS = Tag(values=['minecraft:frost_walker', 'minecraft:depth_strider'])

BOW = Tag(values=['minecraft:infinity', 'minecraft:mending'])

CROSSBOW = Tag(values=['minecraft:multishot', 'minecraft:piercing'])

DAMAGE = Tag(
    values=[
        'minecraft:sharpness',
        'minecraft:smite',
        'minecraft:bane_of_arthropods',
        'minecraft:impaling',
        'minecraft:density',
        'minecraft:breach',
    ],
)

MINING = Tag(values=['minecraft:fortune', 'minecraft:silk_touch'])

RIPTIDE = Tag(values=['minecraft:loyalty', 'minecraft:channeling'])
