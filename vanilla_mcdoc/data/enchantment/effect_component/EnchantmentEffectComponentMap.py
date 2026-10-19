"""
Generated from symbols.json for ::java::data::enchantment::effect_component::EnchantmentEffectComponentMap
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/EnchantmentEffectComponentMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.AttributeEffect import AttributeEffect
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect
    from vanilla_mcdoc.data.enchantment.effect_component.AmmoUseEnchantmentEffect import AmmoUseEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.ArmorEffectivenessEnchantmentEffect import ArmorEffectivenessEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.BlockExperienceEnchantmentEffect import BlockExperienceEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.CrossbowChargeSoundsEnchantmentEffect import CrossbowChargeSoundsEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.DamageEnchantmentEffect import DamageEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.DamageImmunityEnchantmentEffect import DamageImmunityEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.DamageProtectionEnchantmentEffect import DamageProtectionEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.EquipmentDropsEnchantmentEffect import EquipmentDropsEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.FishingLuckBonusEnchantmentEffect import FishingLuckBonusEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.FishingTimeReductionEnchantmentEffect import FishingTimeReductionEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.HitBlockEnchantmentEffect import HitBlockEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.ItemDamageEnchantmentEffect import ItemDamageEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.KnockbackEnchantmentEffect import KnockbackEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.LocationChangedEnchantmentEffect import LocationChangedEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.MobExperienceEnchantmentEffect import MobExperienceEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.PostAttackEnchantmentEffect import PostAttackEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.PostPiercingAttackEnchantmentEffect import PostPiercingAttackEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.ProjectileCountEnchantmentEffect import ProjectileCountEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.ProjectilePiercingEnchantmentEffect import ProjectilePiercingEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.ProjectileSpawnedEnchantmentEffect import ProjectileSpawnedEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.ProjectileSpreadEnchantmentEffect import ProjectileSpreadEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.RepairWithXpEnchantmentEffect import RepairWithXpEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.SmashDamagePerBlockFallenEnchantmentEffect import SmashDamagePerBlockFallenEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.TickEnchantmentEffect import TickEnchantmentEffect
    from vanilla_mcdoc.data.enchantment.effect_component.TridentReturnAccelerationEnchantmentEffect import TridentReturnAccelerationEnchantmentEffect
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class PreventArmorChangeStruct(GeneratedModel):
    pass


class PreventEquipmentDropStruct(GeneratedModel):
    pass


class EnchantmentEffectComponentMap(GeneratedModel):
    ammo_use: list[AmmoUseEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:ammo_use', serialization_alias='minecraft:ammo_use')
    armor_effectiveness: list[ArmorEffectivenessEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:armor_effectiveness', serialization_alias='minecraft:armor_effectiveness')
    attributes: list[AttributeEffect] | None = Field(default=None, validation_alias='minecraft:attributes', serialization_alias='minecraft:attributes')
    block_experience: list[BlockExperienceEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:block_experience', serialization_alias='minecraft:block_experience')
    crossbow_charge_time: ValueEffect | None = Field(default=None, validation_alias='minecraft:crossbow_charge_time', serialization_alias='minecraft:crossbow_charge_time')
    crossbow_charging_sounds: list[CrossbowChargeSoundsEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:crossbow_charging_sounds', serialization_alias='minecraft:crossbow_charging_sounds')
    damage: list[DamageEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:damage', serialization_alias='minecraft:damage')
    damage_immunity: list[DamageImmunityEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:damage_immunity', serialization_alias='minecraft:damage_immunity')
    damage_protection: list[DamageProtectionEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:damage_protection', serialization_alias='minecraft:damage_protection')
    equipment_drops: list[EquipmentDropsEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:equipment_drops', serialization_alias='minecraft:equipment_drops')
    fishing_luck_bonus: list[FishingLuckBonusEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:fishing_luck_bonus', serialization_alias='minecraft:fishing_luck_bonus')
    fishing_time_reduction: list[FishingTimeReductionEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:fishing_time_reduction', serialization_alias='minecraft:fishing_time_reduction')
    hit_block: list[HitBlockEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:hit_block', serialization_alias='minecraft:hit_block')
    item_damage: list[ItemDamageEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:item_damage', serialization_alias='minecraft:item_damage')
    knockback: list[KnockbackEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:knockback', serialization_alias='minecraft:knockback')
    location_changed: list[LocationChangedEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:location_changed', serialization_alias='minecraft:location_changed')
    mob_experience: list[MobExperienceEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:mob_experience', serialization_alias='minecraft:mob_experience')
    post_attack: list[PostAttackEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:post_attack', serialization_alias='minecraft:post_attack')
    post_piercing_attack: list[PostPiercingAttackEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:post_piercing_attack', serialization_alias='minecraft:post_piercing_attack')
    prevent_armor_change: PreventArmorChangeStruct | None = Field(default=None, validation_alias='minecraft:prevent_armor_change', serialization_alias='minecraft:prevent_armor_change')
    prevent_equipment_drop: PreventEquipmentDropStruct | None = Field(default=None, validation_alias='minecraft:prevent_equipment_drop', serialization_alias='minecraft:prevent_equipment_drop')
    projectile_count: list[ProjectileCountEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:projectile_count', serialization_alias='minecraft:projectile_count')
    projectile_piercing: list[ProjectilePiercingEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:projectile_piercing', serialization_alias='minecraft:projectile_piercing')
    projectile_spawned: list[ProjectileSpawnedEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:projectile_spawned', serialization_alias='minecraft:projectile_spawned')
    projectile_spread: list[ProjectileSpreadEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:projectile_spread', serialization_alias='minecraft:projectile_spread')
    repair_with_xp: list[RepairWithXpEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:repair_with_xp', serialization_alias='minecraft:repair_with_xp')
    smash_damage_per_block_fallen: list[SmashDamagePerBlockFallenEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:smash_damage_per_block_fallen', serialization_alias='minecraft:smash_damage_per_block_fallen')
    tick: list[TickEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:tick', serialization_alias='minecraft:tick')
    trident_return_acceleration: list[TridentReturnAccelerationEnchantmentEffect] | None = Field(default=None, validation_alias='minecraft:trident_return_acceleration', serialization_alias='minecraft:trident_return_acceleration')
    trident_sound: list[SoundEventRef] | None = Field(default=None, validation_alias='minecraft:trident_sound', serialization_alias='minecraft:trident_sound')
    trident_spin_attack_strength: ValueEffect | None = Field(default=None, validation_alias='minecraft:trident_spin_attack_strength', serialization_alias='minecraft:trident_spin_attack_strength')
