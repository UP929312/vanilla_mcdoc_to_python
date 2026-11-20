"""
Generated from symbols.json for ::java::data::dispense_behavior::DispenseBehavior
Local link to file: vanilla_mcdoc/data/dispense_behavior/DispenseBehavior.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.dispense_behavior.ShootProjectile import ShootProjectile
from vanilla_mcdoc.data.dispense_behavior.TransformBlock import TransformBlock


class DispenseBehaviorShootProjectile(ShootProjectile):
    type: Literal['minecraft:shoot_projectile', 'shoot_projectile'] = 'minecraft:shoot_projectile'


class DispenseBehaviorTransformBlock(TransformBlock):
    type: Literal['minecraft:transform_block', 'transform_block'] = 'minecraft:transform_block'


class DispenseBehaviorBrushArmadillo(GeneratedModel):
    type: Literal['minecraft:brush_armadillo', 'brush_armadillo'] = 'minecraft:brush_armadillo'


class DispenseBehaviorChargeRespawnAnchor(GeneratedModel):
    type: Literal['minecraft:charge_respawn_anchor', 'charge_respawn_anchor'] = 'minecraft:charge_respawn_anchor'


class DispenseBehaviorConvertToMud(GeneratedModel):
    type: Literal['minecraft:convert_to_mud', 'convert_to_mud'] = 'minecraft:convert_to_mud'


class DispenseBehaviorDropItem(GeneratedModel):
    type: Literal['minecraft:drop_item', 'drop_item'] = 'minecraft:drop_item'


class DispenseBehaviorEmptyBucket(GeneratedModel):
    type: Literal['minecraft:empty_bucket', 'empty_bucket'] = 'minecraft:empty_bucket'


class DispenseBehaviorEquip(GeneratedModel):
    type: Literal['minecraft:equip', 'equip'] = 'minecraft:equip'


class DispenseBehaviorEquipChest(GeneratedModel):
    type: Literal['minecraft:equip_chest', 'equip_chest'] = 'minecraft:equip_chest'


class DispenseBehaviorEquipSulfurCube(GeneratedModel):
    type: Literal['minecraft:equip_sulfur_cube', 'equip_sulfur_cube'] = 'minecraft:equip_sulfur_cube'


class DispenseBehaviorFillBottle(GeneratedModel):
    type: Literal['minecraft:fill_bottle', 'fill_bottle'] = 'minecraft:fill_bottle'


class DispenseBehaviorFillBucket(GeneratedModel):
    type: Literal['minecraft:fill_bucket', 'fill_bucket'] = 'minecraft:fill_bucket'


class DispenseBehaviorGrowPlant(GeneratedModel):
    type: Literal['minecraft:grow_plant', 'grow_plant'] = 'minecraft:grow_plant'


class DispenseBehaviorIgnite(GeneratedModel):
    type: Literal['minecraft:ignite', 'ignite'] = 'minecraft:ignite'


class DispenseBehaviorInsertIntoContainer(GeneratedModel):
    type: Literal['minecraft:insert_into_container', 'insert_into_container'] = 'minecraft:insert_into_container'


class DispenseBehaviorPlaceArmorStand(GeneratedModel):
    type: Literal['minecraft:place_armor_stand', 'place_armor_stand'] = 'minecraft:place_armor_stand'


class DispenseBehaviorPlaceBlock(GeneratedModel):
    type: Literal['minecraft:place_block', 'place_block'] = 'minecraft:place_block'


class DispenseBehaviorPlaceBoat(GeneratedModel):
    type: Literal['minecraft:place_boat', 'place_boat'] = 'minecraft:place_boat'


class DispenseBehaviorPlaceMinecart(GeneratedModel):
    type: Literal['minecraft:place_minecart', 'place_minecart'] = 'minecraft:place_minecart'


class DispenseBehaviorShear(GeneratedModel):
    type: Literal['minecraft:shear', 'shear'] = 'minecraft:shear'


class DispenseBehaviorSpawnGolemFromCarvedPumpkin(GeneratedModel):
    type: Literal['minecraft:spawn_golem_from_carved_pumpkin', 'spawn_golem_from_carved_pumpkin'] = 'minecraft:spawn_golem_from_carved_pumpkin'


class DispenseBehaviorSpawnMob(GeneratedModel):
    type: Literal['minecraft:spawn_mob', 'spawn_mob'] = 'minecraft:spawn_mob'


class DispenseBehaviorSpawnTnt(GeneratedModel):
    type: Literal['minecraft:spawn_tnt', 'spawn_tnt'] = 'minecraft:spawn_tnt'


class DispenseBehaviorSpawnWitherFromWitherSkeletonSkull(GeneratedModel):
    type: Literal['minecraft:spawn_wither_from_wither_skeleton_skull', 'spawn_wither_from_wither_skeleton_skull'] = 'minecraft:spawn_wither_from_wither_skeleton_skull'


type DispenseBehavior = Annotated[
    Annotated[DispenseBehaviorShootProjectile, Tag('minecraft:shoot_projectile')]
    | Annotated[DispenseBehaviorTransformBlock, Tag('minecraft:transform_block')]
    | Annotated[DispenseBehaviorBrushArmadillo, Tag('minecraft:brush_armadillo')]
    | Annotated[DispenseBehaviorChargeRespawnAnchor, Tag('minecraft:charge_respawn_anchor')]
    | Annotated[DispenseBehaviorConvertToMud, Tag('minecraft:convert_to_mud')]
    | Annotated[DispenseBehaviorDropItem, Tag('minecraft:drop_item')]
    | Annotated[DispenseBehaviorEmptyBucket, Tag('minecraft:empty_bucket')]
    | Annotated[DispenseBehaviorEquip, Tag('minecraft:equip')]
    | Annotated[DispenseBehaviorEquipChest, Tag('minecraft:equip_chest')]
    | Annotated[DispenseBehaviorEquipSulfurCube, Tag('minecraft:equip_sulfur_cube')]
    | Annotated[DispenseBehaviorFillBottle, Tag('minecraft:fill_bottle')]
    | Annotated[DispenseBehaviorFillBucket, Tag('minecraft:fill_bucket')]
    | Annotated[DispenseBehaviorGrowPlant, Tag('minecraft:grow_plant')]
    | Annotated[DispenseBehaviorIgnite, Tag('minecraft:ignite')]
    | Annotated[DispenseBehaviorInsertIntoContainer, Tag('minecraft:insert_into_container')]
    | Annotated[DispenseBehaviorPlaceArmorStand, Tag('minecraft:place_armor_stand')]
    | Annotated[DispenseBehaviorPlaceBlock, Tag('minecraft:place_block')]
    | Annotated[DispenseBehaviorPlaceBoat, Tag('minecraft:place_boat')]
    | Annotated[DispenseBehaviorPlaceMinecart, Tag('minecraft:place_minecart')]
    | Annotated[DispenseBehaviorShear, Tag('minecraft:shear')]
    | Annotated[DispenseBehaviorSpawnGolemFromCarvedPumpkin, Tag('minecraft:spawn_golem_from_carved_pumpkin')]
    | Annotated[DispenseBehaviorSpawnMob, Tag('minecraft:spawn_mob')]
    | Annotated[DispenseBehaviorSpawnTnt, Tag('minecraft:spawn_tnt')]
    | Annotated[DispenseBehaviorSpawnWitherFromWitherSkeletonSkull, Tag('minecraft:spawn_wither_from_wither_skeleton_skull')],
    Discriminator(tag_of('type')),
]
