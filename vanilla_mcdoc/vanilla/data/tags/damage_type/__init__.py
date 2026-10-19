"""Vanilla's data/tags/damage_type/ files"""
from vanilla_mcdoc.data.tag.Tag import Tag

ALWAYS_HURTS_ENDER_DRAGONS = Tag(values=['#minecraft:is_explosion'])

ALWAYS_KILLS_ARMOR_STANDS = Tag(
    values=['minecraft:arrow', 'minecraft:trident', 'minecraft:fireball', 'minecraft:wither_skull', 'minecraft:wind_charge'],
)

ALWAYS_MOST_SIGNIFICANT_FALL = Tag(values=['minecraft:out_of_world'])

ALWAYS_TRIGGERS_SILVERFISH = Tag(values=['minecraft:magic'])

AVOIDS_GUARDIAN_THORNS = Tag(values=['minecraft:magic', 'minecraft:thorns', '#minecraft:is_explosion'])

BURNS_ARMOR_STANDS = Tag(values=['minecraft:on_fire'])

BURN_FROM_STEPPING = Tag(values=['minecraft:campfire', 'minecraft:hot_floor', 'minecraft:sulfur_cube_hot'])

BYPASSES_ARMOR = Tag(
    values=[
        'minecraft:on_fire',
        'minecraft:in_wall',
        'minecraft:cramming',
        'minecraft:drown',
        'minecraft:fly_into_wall',
        'minecraft:generic',
        'minecraft:wither',
        'minecraft:dragon_breath',
        'minecraft:starve',
        'minecraft:fall',
        'minecraft:ender_pearl',
        'minecraft:freeze',
        'minecraft:stalagmite',
        'minecraft:magic',
        'minecraft:indirect_magic',
        'minecraft:out_of_world',
        'minecraft:generic_kill',
        'minecraft:sonic_boom',
        'minecraft:outside_border',
    ],
)

BYPASSES_COOLDOWN = Tag(values=[])

BYPASSES_EFFECTS = Tag(values=['minecraft:starve'])

BYPASSES_ENCHANTMENTS = Tag(values=['minecraft:sonic_boom'])

BYPASSES_INVULNERABILITY = Tag(values=['minecraft:out_of_world', 'minecraft:generic_kill'])

BYPASSES_RESISTANCE = Tag(values=['minecraft:out_of_world', 'minecraft:generic_kill'])

BYPASSES_SHIELD = Tag(
    values=[
        '#minecraft:bypasses_armor',
        'minecraft:cactus',
        'minecraft:campfire',
        'minecraft:dry_out',
        'minecraft:falling_anvil',
        'minecraft:falling_stalactite',
        'minecraft:hot_floor',
        'minecraft:sulfur_cube_hot',
        'minecraft:in_fire',
        'minecraft:lava',
        'minecraft:lightning_bolt',
        'minecraft:sweet_berry_bush',
    ],
)

BYPASSES_WOLF_ARMOR = Tag(
    values=[
        '#minecraft:bypasses_invulnerability',
        'minecraft:cramming',
        'minecraft:drown',
        'minecraft:dry_out',
        'minecraft:freeze',
        'minecraft:in_wall',
        'minecraft:indirect_magic',
        'minecraft:magic',
        'minecraft:outside_border',
        'minecraft:starve',
        'minecraft:thorns',
        'minecraft:wither',
    ],
)

CAN_BREAK_ARMOR_STAND = Tag(values=['minecraft:player_explosion', '#minecraft:is_player_attack'])

DAMAGES_HELMET = Tag(values=['minecraft:falling_anvil', 'minecraft:falling_block', 'minecraft:falling_stalactite'])

IGNITES_ARMOR_STANDS = Tag(values=['minecraft:in_fire', 'minecraft:campfire'])

IS_DROWNING = Tag(values=['minecraft:drown'])

IS_EXPLOSION = Tag(values=['minecraft:fireworks', 'minecraft:explosion', 'minecraft:player_explosion', 'minecraft:bad_respawn_point'])

IS_FALL = Tag(values=['minecraft:fall', 'minecraft:ender_pearl', 'minecraft:stalagmite'])

IS_FIRE = Tag(
    values=[
        'minecraft:in_fire',
        'minecraft:campfire',
        'minecraft:on_fire',
        'minecraft:lava',
        'minecraft:hot_floor',
        'minecraft:sulfur_cube_hot',
        'minecraft:unattributed_fireball',
        'minecraft:fireball',
    ],
)

IS_FREEZING = Tag(values=['minecraft:freeze'])

IS_LIGHTNING = Tag(values=['minecraft:lightning_bolt'])

IS_PLAYER_ATTACK = Tag(values=['minecraft:player_attack', 'minecraft:spear', 'minecraft:mace_smash'])

IS_PROJECTILE = Tag(
    values=[
        'minecraft:arrow',
        'minecraft:trident',
        'minecraft:mob_projectile',
        'minecraft:unattributed_fireball',
        'minecraft:fireball',
        'minecraft:wither_skull',
        'minecraft:thrown',
        'minecraft:wind_charge',
    ],
)

MACE_SMASH = Tag(values=['minecraft:mace_smash'])

NO_ANGER = Tag(values=['minecraft:mob_attack_no_aggro'])

NO_HURT_SOUND = Tag(values=[])

NO_IMPACT = Tag(values=['minecraft:drown'])

NO_KNOCKBACK = Tag(
    values=[
        'minecraft:explosion',
        'minecraft:player_explosion',
        'minecraft:bad_respawn_point',
        'minecraft:in_fire',
        'minecraft:lightning_bolt',
        'minecraft:on_fire',
        'minecraft:lava',
        'minecraft:hot_floor',
        'minecraft:sulfur_cube_hot',
        'minecraft:in_wall',
        'minecraft:cramming',
        'minecraft:drown',
        'minecraft:starve',
        'minecraft:cactus',
        'minecraft:fall',
        'minecraft:ender_pearl',
        'minecraft:fly_into_wall',
        'minecraft:out_of_world',
        'minecraft:generic',
        'minecraft:magic',
        'minecraft:wither',
        'minecraft:dragon_breath',
        'minecraft:dry_out',
        'minecraft:sweet_berry_bush',
        'minecraft:freeze',
        'minecraft:stalagmite',
        'minecraft:outside_border',
        'minecraft:generic_kill',
        'minecraft:campfire',
        'minecraft:spear',
    ],
)

NO_WOLF_RETALIATION = Tag(values=['minecraft:sulfur_cube_hot'])

PANIC_CAUSES = Tag(
    values=[
        '#minecraft:panic_environmental_causes',
        'minecraft:arrow',
        'minecraft:dragon_breath',
        'minecraft:explosion',
        'minecraft:fireball',
        'minecraft:fireworks',
        'minecraft:indirect_magic',
        'minecraft:magic',
        'minecraft:mob_attack',
        'minecraft:mob_projectile',
        'minecraft:player_explosion',
        'minecraft:sonic_boom',
        'minecraft:sting',
        'minecraft:thrown',
        'minecraft:trident',
        'minecraft:unattributed_fireball',
        'minecraft:wind_charge',
        'minecraft:wither',
        'minecraft:wither_skull',
        '#minecraft:is_player_attack',
    ],
)

PANIC_ENVIRONMENTAL_CAUSES = Tag(
    values=[
        'minecraft:cactus',
        'minecraft:freeze',
        'minecraft:hot_floor',
        'minecraft:sulfur_cube_hot',
        'minecraft:in_fire',
        'minecraft:lava',
        'minecraft:lightning_bolt',
        'minecraft:on_fire',
    ],
)

SULFUR_CUBE_WITH_BLOCK_IMMUNE_TO = Tag(
    values=[
        'minecraft:arrow',
        'minecraft:cactus',
        'minecraft:dry_out',
        'minecraft:fall',
        'minecraft:falling_anvil',
        'minecraft:falling_block',
        'minecraft:falling_stalactite',
        'minecraft:freeze',
        'minecraft:mace_smash',
        'minecraft:hot_floor',
        'minecraft:mob_attack',
        'minecraft:mob_attack_no_aggro',
        'minecraft:mob_projectile',
        'minecraft:player_attack',
        'minecraft:spear',
        'minecraft:spit',
        'minecraft:stalagmite',
        'minecraft:sting',
        'minecraft:sulfur_cube_hot',
        'minecraft:sweet_berry_bush',
        'minecraft:thrown',
        'minecraft:trident',
        'minecraft:wind_charge',
        '#minecraft:is_explosion',
    ],
)

WITCH_RESISTANT_TO = Tag(values=['minecraft:magic', 'minecraft:indirect_magic', 'minecraft:sonic_boom', 'minecraft:thorns'])

WITHER_IMMUNE_TO = Tag(values=['minecraft:drown'])
