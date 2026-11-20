"""Vanilla's data/dispense_behavior/ files"""
from typing import Any
from vanilla_mcdoc.data.dispense_behavior.DispenseBehavior import DispenseBehaviorBrushArmadillo, DispenseBehaviorChargeRespawnAnchor, DispenseBehaviorConvertToMud, DispenseBehaviorDropItem, DispenseBehaviorEmptyBucket, DispenseBehaviorEquip, DispenseBehaviorEquipChest, DispenseBehaviorEquipSulfurCube, DispenseBehaviorFillBottle, DispenseBehaviorFillBucket, DispenseBehaviorGrowPlant, DispenseBehaviorIgnite, DispenseBehaviorInsertIntoContainer, DispenseBehaviorPlaceArmorStand, DispenseBehaviorPlaceBlock, DispenseBehaviorPlaceBoat, DispenseBehaviorPlaceMinecart, DispenseBehaviorShear, DispenseBehaviorShootProjectile, DispenseBehaviorSpawnGolemFromCarvedPumpkin, DispenseBehaviorSpawnMob, DispenseBehaviorSpawnTnt, DispenseBehaviorSpawnWitherFromWitherSkeletonSkull, DispenseBehaviorTransformBlock
from vanilla_mcdoc.data.dispense_behavior.ShootProjectile import SoundStruct
from vanilla_mcdoc.data.worldgen.FloatProvider import FloatProvider

ARMOR_STAND = [DispenseBehaviorPlaceArmorStand(type='minecraft:place_armor_stand')]

BOAT = [DispenseBehaviorPlaceBoat(type='minecraft:place_boat'), DispenseBehaviorDropItem(type='minecraft:drop_item')]

BONE_MEAL = [DispenseBehaviorGrowPlant(type='minecraft:grow_plant')]

BRUSH = [DispenseBehaviorBrushArmadillo(type='minecraft:brush_armadillo')]

CARVED_PUMPKIN = [
    DispenseBehaviorSpawnGolemFromCarvedPumpkin(type='minecraft:spawn_golem_from_carved_pumpkin'),
    DispenseBehaviorEquip(type='minecraft:equip'),
]

CHEST = [DispenseBehaviorEquipChest(type='minecraft:equip_chest'), DispenseBehaviorDropItem(type='minecraft:drop_item')]

DEFAULT = [
    DispenseBehaviorEquipSulfurCube(type='minecraft:equip_sulfur_cube'),
    DispenseBehaviorDropItem(type='minecraft:drop_item'),
]

DEFAULT_PROJECTILE = [
    DispenseBehaviorShootProjectile(
        scale=0.699999988079071,
        offset=(0.0, 0.1, 0.0),
        uncertainty=6.0,
        power=1.1,
        type='minecraft:shoot_projectile',
    ),
]

DROPPER = [
    DispenseBehaviorInsertIntoContainer(type='minecraft:insert_into_container'),
    DispenseBehaviorDropItem(type='minecraft:drop_item'),
]

EMPTY_BUCKET = [DispenseBehaviorFillBucket(type='minecraft:fill_bucket'), DispenseBehaviorDropItem(type='minecraft:drop_item')]

EQUIPMENT = [DispenseBehaviorEquip(type='minecraft:equip'), DispenseBehaviorDropItem(type='minecraft:drop_item')]

FILLED_BUCKET = [DispenseBehaviorEmptyBucket(type='minecraft:empty_bucket'), DispenseBehaviorDropItem(type='minecraft:drop_item')]

FIREWORK_ROCKET = [
    DispenseBehaviorShootProjectile(
        scale=0.5000099999997474,
        offset=(0.0, 0.0, 0.0),
        uncertainty=1.0,
        power=0.5,
        sound=SoundStruct(sound='minecraft:entity.firework_rocket.shoot', volume=1.0, pitch=1.2),
        type='minecraft:shoot_projectile',
    ),
]

FIRE_CHARGE = [
    DispenseBehaviorShootProjectile(
        scale=1.0,
        offset=(0.0, 0.0, 0.0),
        uncertainty=6.6666665,
        power=1.0,
        sound=SoundStruct(
            sound='minecraft:entity.blaze.shoot',
            volume=2.0,
            pitch=FloatProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 1.2, 'min': 0.8, 'plateau': 0.0})),
        ),
        type='minecraft:shoot_projectile',
    ),
]

FLINT_AND_STEEL = [DispenseBehaviorIgnite(type='minecraft:ignite')]

GLASS_BOTTLE = [DispenseBehaviorFillBottle(type='minecraft:fill_bottle'), DispenseBehaviorDropItem(type='minecraft:drop_item')]

GLOWSTONE = [
    DispenseBehaviorChargeRespawnAnchor(type='minecraft:charge_respawn_anchor'),
    DispenseBehaviorDropItem(type='minecraft:drop_item'),
]

HONEYCOMB = [
    DispenseBehaviorTransformBlock(transformer='minecraft:honeycomb', type='minecraft:transform_block'),
    DispenseBehaviorDropItem(type='minecraft:drop_item'),
]

MINECART = [DispenseBehaviorPlaceMinecart(type='minecraft:place_minecart'), DispenseBehaviorDropItem(type='minecraft:drop_item')]

POTION = [DispenseBehaviorConvertToMud(type='minecraft:convert_to_mud'), DispenseBehaviorDropItem(type='minecraft:drop_item')]

SHEARS = [DispenseBehaviorShear(type='minecraft:shear')]

SHULKER_BOX = [DispenseBehaviorPlaceBlock(type='minecraft:place_block')]

SPAWN_EGG = [DispenseBehaviorSpawnMob(type='minecraft:spawn_mob')]

THROWN_POTION = [
    DispenseBehaviorShootProjectile(
        scale=0.699999988079071,
        offset=(0.0, 0.1, 0.0),
        uncertainty=3.0,
        power=1.375,
        type='minecraft:shoot_projectile',
    ),
]

TNT = [
    DispenseBehaviorEquipSulfurCube(type='minecraft:equip_sulfur_cube'),
    DispenseBehaviorSpawnTnt(type='minecraft:spawn_tnt'),
]

WIND_CHARGE = [
    DispenseBehaviorShootProjectile(
        scale=1.0,
        offset=(0.0, 0.0, 0.0),
        uncertainty=6.6666665,
        power=1.0,
        sound=SoundStruct(
            sound='minecraft:entity.wind_charge.throw',
            volume=0.5,
            pitch=FloatProvider(
                type='minecraft:uniform',
                **dict[str, Any]({'max_exclusive': 0.5, 'min_inclusive': 0.33333334}),
            ),
        ),
        type='minecraft:shoot_projectile',
    ),
]

WITHER_SKELETON_SKULL = [
    DispenseBehaviorSpawnWitherFromWitherSkeletonSkull(type='minecraft:spawn_wither_from_wither_skeleton_skull'),
    DispenseBehaviorEquip(type='minecraft:equip'),
]
