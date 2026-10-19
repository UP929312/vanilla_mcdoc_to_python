"""Vanilla's data/tags/item/enchantable/ files"""
from vanilla_mcdoc.data.tag.Tag import Tag

ARMOR = Tag(
    values=[
        '#minecraft:enchantable/foot_armor',
        '#minecraft:enchantable/leg_armor',
        '#minecraft:enchantable/chest_armor',
        '#minecraft:enchantable/head_armor',
    ],
)

BOW = Tag(values=['minecraft:bow'])

CHEST_ARMOR = Tag(values=['#minecraft:chest_armor'])

CROSSBOW = Tag(values=['minecraft:crossbow'])

DURABILITY = Tag(
    values=[
        '#minecraft:foot_armor',
        '#minecraft:leg_armor',
        '#minecraft:chest_armor',
        '#minecraft:head_armor',
        'minecraft:elytra',
        'minecraft:shield',
        '#minecraft:swords',
        '#minecraft:axes',
        '#minecraft:pickaxes',
        '#minecraft:shovels',
        '#minecraft:hoes',
        'minecraft:bow',
        'minecraft:crossbow',
        'minecraft:trident',
        'minecraft:flint_and_steel',
        'minecraft:shears',
        'minecraft:brush',
        'minecraft:fishing_rod',
        'minecraft:carrot_on_a_stick',
        'minecraft:warped_fungus_on_a_stick',
        'minecraft:mace',
        '#minecraft:spears',
    ],
)

EQUIPPABLE = Tag(
    values=[
        '#minecraft:foot_armor',
        '#minecraft:leg_armor',
        '#minecraft:chest_armor',
        '#minecraft:head_armor',
        'minecraft:elytra',
        '#minecraft:skulls',
        'minecraft:carved_pumpkin',
    ],
)

FIRE_ASPECT = Tag(values=['#minecraft:enchantable/melee_weapon', 'minecraft:mace'])

FISHING = Tag(values=['minecraft:fishing_rod'])

FOOT_ARMOR = Tag(values=['#minecraft:foot_armor'])

HEAD_ARMOR = Tag(values=['#minecraft:head_armor'])

LEG_ARMOR = Tag(values=['#minecraft:leg_armor'])

LUNGE = Tag(values=['#minecraft:spears'])

MACE = Tag(values=['minecraft:mace'])

MELEE_WEAPON = Tag(values=['#minecraft:swords', '#minecraft:spears'])

MINING = Tag(values=['#minecraft:axes', '#minecraft:pickaxes', '#minecraft:shovels', '#minecraft:hoes', 'minecraft:shears'])

MINING_LOOT = Tag(values=['#minecraft:axes', '#minecraft:pickaxes', '#minecraft:shovels', '#minecraft:hoes'])

SHARP_WEAPON = Tag(values=['#minecraft:enchantable/melee_weapon', '#minecraft:axes'])

SWEEPING = Tag(values=['#minecraft:swords'])

TRIDENT = Tag(values=['minecraft:trident'])

VANISHING = Tag(values=['#minecraft:enchantable/durability', 'minecraft:compass', 'minecraft:carved_pumpkin', '#minecraft:skulls'])

WEAPON = Tag(values=['#minecraft:enchantable/sharp_weapon', 'minecraft:mace'])
