"""Vanilla's data/tags/entity_type/ files"""
from vanilla_mcdoc.data.tag.Tag import Tag

ACCEPTS_IRON_GOLEM_GIFT = Tag(values=['minecraft:copper_golem'])

AQUATIC = Tag(
    values=[
        'minecraft:turtle',
        'minecraft:axolotl',
        'minecraft:guardian',
        'minecraft:elder_guardian',
        'minecraft:cod',
        'minecraft:pufferfish',
        'minecraft:salmon',
        'minecraft:tropical_fish',
        'minecraft:dolphin',
        'minecraft:squid',
        'minecraft:glow_squid',
        'minecraft:tadpole',
        'minecraft:nautilus',
        'minecraft:zombie_nautilus',
    ],
)

ARROWS = Tag(values=['minecraft:arrow', 'minecraft:spectral_arrow'])

ARTHROPOD = Tag(
    values=['minecraft:bee', 'minecraft:endermite', 'minecraft:silverfish', 'minecraft:spider', 'minecraft:cave_spider'],
)

AXOLOTL_ALWAYS_HOSTILES = Tag(values=['minecraft:drowned', 'minecraft:guardian', 'minecraft:elder_guardian'])

AXOLOTL_HUNT_TARGETS = Tag(
    values=[
        'minecraft:tropical_fish',
        'minecraft:pufferfish',
        'minecraft:salmon',
        'minecraft:cod',
        'minecraft:squid',
        'minecraft:glow_squid',
        'minecraft:tadpole',
    ],
)

BEEHIVE_INHABITORS = Tag(values=['minecraft:bee'])

BOAT = Tag(
    values=[
        'minecraft:oak_boat',
        'minecraft:spruce_boat',
        'minecraft:birch_boat',
        'minecraft:jungle_boat',
        'minecraft:acacia_boat',
        'minecraft:cherry_boat',
        'minecraft:dark_oak_boat',
        'minecraft:pale_oak_boat',
        'minecraft:mangrove_boat',
        'minecraft:bamboo_raft',
        'minecraft:poplar_boat',
    ],
)

BURN_IN_DAYLIGHT = Tag(
    values=[
        'minecraft:skeleton',
        'minecraft:stray',
        'minecraft:wither_skeleton',
        'minecraft:bogged',
        'minecraft:zombie',
        'minecraft:zombie_horse',
        'minecraft:zombie_villager',
        'minecraft:drowned',
        'minecraft:zombie_nautilus',
        'minecraft:frostbite',
        'minecraft:phantom',
    ],
)

CANDIDATE_FOR_IRON_GOLEM_GIFT = Tag(values=['minecraft:villager', '#minecraft:accepts_iron_golem_gift'])

CANNOT_BE_AGE_LOCKED = Tag(values=['minecraft:zombie_horse', 'minecraft:skeleton_horse', 'minecraft:villager'])

CANNOT_BE_DISMOUNTED_BY_ITEM_USAGE = Tag(values=['minecraft:interaction'])

CANNOT_BE_PUSHED_ONTO_BOATS = Tag(
    values=[
        'minecraft:player',
        'minecraft:elder_guardian',
        'minecraft:cod',
        'minecraft:pufferfish',
        'minecraft:salmon',
        'minecraft:tropical_fish',
        'minecraft:dolphin',
        'minecraft:squid',
        'minecraft:glow_squid',
        'minecraft:tadpole',
        'minecraft:creaking',
        'minecraft:nautilus',
        'minecraft:zombie_nautilus',
        'minecraft:sulfur_cube',
    ],
)

CAN_BREATHE_UNDER_WATER = Tag(
    values=[
        '#minecraft:undead',
        'minecraft:axolotl',
        'minecraft:frog',
        'minecraft:guardian',
        'minecraft:elder_guardian',
        'minecraft:turtle',
        'minecraft:glow_squid',
        'minecraft:cod',
        'minecraft:pufferfish',
        'minecraft:salmon',
        'minecraft:squid',
        'minecraft:tropical_fish',
        'minecraft:tadpole',
        'minecraft:armor_stand',
        'minecraft:copper_golem',
        'minecraft:nautilus',
    ],
)

CAN_EQUIP_HARNESS = Tag(values=['minecraft:happy_ghast'])

CAN_EQUIP_SADDLE = Tag(
    values=[
        'minecraft:horse',
        'minecraft:skeleton_horse',
        'minecraft:zombie_horse',
        'minecraft:donkey',
        'minecraft:mule',
        'minecraft:pig',
        'minecraft:strider',
        'minecraft:camel',
        'minecraft:camel_husk',
        'minecraft:nautilus',
        'minecraft:zombie_nautilus',
    ],
)

CAN_FLOAT_WHILE_RIDDEN = Tag(
    values=[
        'minecraft:horse',
        'minecraft:zombie_horse',
        'minecraft:mule',
        'minecraft:donkey',
        'minecraft:camel',
        'minecraft:camel_husk',
    ],
)

CAN_TURN_IN_BOATS = Tag(values=['minecraft:breeze'])

CAN_WEAR_HORSE_ARMOR = Tag(values=['minecraft:horse', 'minecraft:zombie_horse'])

CAN_WEAR_NAUTILUS_ARMOR = Tag(values=['minecraft:nautilus', 'minecraft:zombie_nautilus'])

DEFLECTS_PROJECTILES = Tag(values=['minecraft:breeze'])

DISMOUNTS_UNDERWATER = Tag(
    values=[
        'minecraft:camel',
        'minecraft:chicken',
        'minecraft:donkey',
        'minecraft:happy_ghast',
        'minecraft:horse',
        'minecraft:llama',
        'minecraft:mule',
        'minecraft:pig',
        'minecraft:ravager',
        'minecraft:spider',
        'minecraft:strider',
        'minecraft:trader_llama',
        'minecraft:zombie_horse',
    ],
)

DOES_NOT_BREAK_BRITTLE_ICE = Tag(values=['minecraft:frostbite'])

FALL_DAMAGE_IMMUNE = Tag(
    values=[
        'minecraft:copper_golem',
        'minecraft:iron_golem',
        'minecraft:snow_golem',
        'minecraft:shulker',
        'minecraft:allay',
        'minecraft:bat',
        'minecraft:bee',
        'minecraft:blaze',
        'minecraft:cat',
        'minecraft:chicken',
        'minecraft:ghast',
        'minecraft:happy_ghast',
        'minecraft:phantom',
        'minecraft:magma_cube',
        'minecraft:ocelot',
        'minecraft:parrot',
        'minecraft:wither',
        'minecraft:breeze',
    ],
)

FOLLOWABLE_FRIENDLY_MOBS = Tag(
    values=[
        'minecraft:armadillo',
        'minecraft:bee',
        'minecraft:camel',
        'minecraft:cat',
        'minecraft:chicken',
        'minecraft:cow',
        'minecraft:donkey',
        'minecraft:fox',
        'minecraft:goat',
        'minecraft:happy_ghast',
        'minecraft:horse',
        'minecraft:skeleton_horse',
        'minecraft:llama',
        'minecraft:mule',
        'minecraft:ocelot',
        'minecraft:panda',
        'minecraft:parrot',
        'minecraft:pig',
        'minecraft:polar_bear',
        'minecraft:rabbit',
        'minecraft:sheep',
        'minecraft:sniffer',
        'minecraft:strider',
        'minecraft:villager',
        'minecraft:wolf',
    ],
)

FREEZE_HURTS_EXTRA_TYPES = Tag(values=['minecraft:strider', 'minecraft:blaze', 'minecraft:magma_cube'])

FREEZE_IMMUNE_ENTITY_TYPES = Tag(
    values=[
        'minecraft:stray',
        'minecraft:polar_bear',
        'minecraft:snow_golem',
        'minecraft:wither',
        'minecraft:frostbite',
        'minecraft:zombie',
        'minecraft:drowned',
        'minecraft:husk',
    ],
)

FROG_FOOD = Tag(values=['minecraft:slime', 'minecraft:magma_cube'])

IGNORES_POISON_AND_REGEN = Tag(values=['#minecraft:undead'])

ILLAGER = Tag(values=['minecraft:evoker', 'minecraft:illusioner', 'minecraft:pillager', 'minecraft:vindicator'])

ILLAGER_FRIENDS = Tag(values=['#minecraft:illager'])

IMMUNE_TO_INFESTED = Tag(values=['minecraft:silverfish'])

IMMUNE_TO_OOZING = Tag(values=['minecraft:slime'])

IMPACT_PROJECTILES = Tag(
    values=[
        '#minecraft:arrows',
        'minecraft:firework_rocket',
        'minecraft:ice_ball',
        'minecraft:snowball',
        'minecraft:fireball',
        'minecraft:small_fireball',
        'minecraft:egg',
        'minecraft:trident',
        'minecraft:dragon_fireball',
        'minecraft:wither_skull',
        'minecraft:wind_charge',
        'minecraft:breeze_wind_charge',
    ],
)

INVERTED_HEALING_AND_HARM = Tag(values=['#minecraft:undead'])

NAUTILUS_HOSTILES = Tag(values=['minecraft:pufferfish'])

NON_CONTROLLING_RIDER = Tag(values=['minecraft:slime', 'minecraft:magma_cube', 'minecraft:sulfur_cube'])

NOT_AFFECTED_BY_GEYSERS = Tag(values=['minecraft:ender_dragon'])

NOT_SCARY_FOR_PUFFERFISH = Tag(
    values=[
        'minecraft:turtle',
        'minecraft:guardian',
        'minecraft:elder_guardian',
        'minecraft:cod',
        'minecraft:pufferfish',
        'minecraft:salmon',
        'minecraft:tropical_fish',
        'minecraft:dolphin',
        'minecraft:squid',
        'minecraft:glow_squid',
        'minecraft:tadpole',
        'minecraft:nautilus',
        'minecraft:zombie_nautilus',
        'minecraft:sulfur_cube',
    ],
)

NO_ANGER_FROM_WIND_CHARGE = Tag(
    values=[
        'minecraft:breeze',
        'minecraft:skeleton',
        'minecraft:bogged',
        'minecraft:stray',
        'minecraft:zombie',
        'minecraft:husk',
        'minecraft:spider',
        'minecraft:cave_spider',
        'minecraft:slime',
        'minecraft:frostbite',
    ],
)

POWDER_SNOW_WALKABLE_MOBS = Tag(values=['minecraft:rabbit', 'minecraft:endermite', 'minecraft:silverfish', 'minecraft:fox', 'minecraft:frostbite'])

RAIDERS = Tag(
    values=[
        'minecraft:evoker',
        'minecraft:pillager',
        'minecraft:ravager',
        'minecraft:vindicator',
        'minecraft:illusioner',
        'minecraft:witch',
    ],
)

REDIRECTABLE_PROJECTILE = Tag(values=['minecraft:fireball', 'minecraft:wind_charge', 'minecraft:breeze_wind_charge'])

SENSITIVE_TO_BANE_OF_ARTHROPODS = Tag(values=['#minecraft:arthropod'])

SENSITIVE_TO_IMPALING = Tag(values=['#minecraft:aquatic'])

SENSITIVE_TO_SMITE = Tag(values=['#minecraft:undead'])

SKELETONS = Tag(
    values=[
        'minecraft:skeleton',
        'minecraft:stray',
        'minecraft:wither_skeleton',
        'minecraft:skeleton_horse',
        'minecraft:bogged',
        'minecraft:parched',
    ],
)

UNDEAD = Tag(values=['#minecraft:skeletons', '#minecraft:zombies', 'minecraft:wither', 'minecraft:phantom'])

WITHER_FRIENDS = Tag(values=['#minecraft:undead'])

ZOMBIES = Tag(
    values=[
        'minecraft:zombie_horse',
        'minecraft:camel_husk',
        'minecraft:zombie',
        'minecraft:zombie_villager',
        'minecraft:zombified_piglin',
        'minecraft:zoglin',
        'minecraft:drowned',
        'minecraft:husk',
        'minecraft:zombie_nautilus',
        'minecraft:frostbite',
    ],
)
