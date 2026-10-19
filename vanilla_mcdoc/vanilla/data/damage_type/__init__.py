"""Vanilla's data/damage_type/ files"""
from vanilla_mcdoc.data.damage_type.DamageEffects import DamageEffects
from vanilla_mcdoc.data.damage_type.DamageScaling import DamageScaling
from vanilla_mcdoc.data.damage_type.DamageType import DamageType
from vanilla_mcdoc.data.damage_type.DeathMessageType import DeathMessageType

ARROW = DamageType(message_id='arrow', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

BAD_RESPAWN_POINT = DamageType(
    message_id='badRespawnPoint',
    exhaustion=0.1,
    scaling=DamageScaling.ALWAYS,
    death_message_type=DeathMessageType.INTENTIONALGAMEDESIGN,
)

CACTUS = DamageType(message_id='cactus', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

CAMPFIRE = DamageType(message_id='inFire', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER, effects=DamageEffects.BURNING)

CRAMMING = DamageType(message_id='cramming', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER)

DRAGON_BREATH = DamageType(message_id='dragonBreath', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER)

DROWN = DamageType(message_id='drown', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER, effects=DamageEffects.DROWNING)

DRY_OUT = DamageType(message_id='dryout', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

ENDER_PEARL = DamageType(
    message_id='fall',
    exhaustion=0.0,
    scaling=DamageScaling.LIVINGNONPLAYER,
    death_message_type=DeathMessageType.FALLVARIANTS,
)

EXPLOSION = DamageType(message_id='explosion', exhaustion=0.1, scaling=DamageScaling.ALWAYS)

FALL = DamageType(
    message_id='fall',
    exhaustion=0.0,
    scaling=DamageScaling.LIVINGNONPLAYER,
    death_message_type=DeathMessageType.FALLVARIANTS,
)

FALLING_ANVIL = DamageType(message_id='anvil', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

FALLING_BLOCK = DamageType(message_id='fallingBlock', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

FALLING_STALACTITE = DamageType(message_id='fallingStalactite', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

FIREBALL = DamageType(message_id='fireball', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER, effects=DamageEffects.BURNING)

FIREWORKS = DamageType(message_id='fireworks', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

FLY_INTO_WALL = DamageType(message_id='flyIntoWall', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER)

FREEZE = DamageType(message_id='freeze', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER, effects=DamageEffects.FREEZING)

GENERIC = DamageType(message_id='generic', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER)

GENERIC_KILL = DamageType(message_id='genericKill', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER)

HOT_FLOOR = DamageType(message_id='hotFloor', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER, effects=DamageEffects.BURNING)

INDIRECT_MAGIC = DamageType(message_id='indirectMagic', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER)

IN_FIRE = DamageType(message_id='inFire', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER, effects=DamageEffects.BURNING)

IN_WALL = DamageType(message_id='inWall', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER)

LAVA = DamageType(message_id='lava', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER, effects=DamageEffects.BURNING)

LIGHTNING_BOLT = DamageType(message_id='lightningBolt', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

MACE_SMASH = DamageType(message_id='mace_smash', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

MAGIC = DamageType(message_id='magic', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER)

MOB_ATTACK = DamageType(message_id='mob', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

MOB_ATTACK_NO_AGGRO = DamageType(message_id='mob', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

MOB_PROJECTILE = DamageType(message_id='mob', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

ON_FIRE = DamageType(message_id='onFire', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER, effects=DamageEffects.BURNING)

OUTSIDE_BORDER = DamageType(message_id='outsideBorder', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER)

OUT_OF_WORLD = DamageType(message_id='outOfWorld', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER)

PLAYER_ATTACK = DamageType(message_id='player', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

PLAYER_EXPLOSION = DamageType(message_id='explosion.player', exhaustion=0.1, scaling=DamageScaling.ALWAYS)

SONIC_BOOM = DamageType(message_id='sonic_boom', exhaustion=0.0, scaling=DamageScaling.ALWAYS)

SPEAR = DamageType(message_id='spear', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

SPIT = DamageType(message_id='mob', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

STALAGMITE = DamageType(message_id='stalagmite', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER)

STARVE = DamageType(message_id='starve', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER)

STING = DamageType(message_id='sting', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

SULFUR_CUBE_HOT = DamageType(
    message_id='sulfurCubeHot',
    exhaustion=0.1,
    scaling=DamageScaling.LIVINGNONPLAYER,
    effects=DamageEffects.BURNING,
)

SWEET_BERRY_BUSH = DamageType(
    message_id='sweetBerryBush',
    exhaustion=0.1,
    scaling=DamageScaling.LIVINGNONPLAYER,
    effects=DamageEffects.POKING,
)

THORNS = DamageType(message_id='thorns', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER, effects=DamageEffects.THORNS)

THROWN = DamageType(message_id='thrown', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

TRIDENT = DamageType(message_id='trident', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

UNATTRIBUTED_FIREBALL = DamageType(message_id='onFire', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER, effects=DamageEffects.BURNING)

WIND_CHARGE = DamageType(message_id='mob', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)

WITHER = DamageType(message_id='wither', exhaustion=0.0, scaling=DamageScaling.LIVINGNONPLAYER)

WITHER_SKULL = DamageType(message_id='witherSkull', exhaustion=0.1, scaling=DamageScaling.LIVINGNONPLAYER)
