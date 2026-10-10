"""
Generated from symbols.json for ::java::data::enchantment::effect_component::EnchantmentEffectComponentMap
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/EnchantmentEffectComponentMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

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


class EnchantmentEffectComponentMapValueStructEffectComponentPreventArmorChange(GeneratedModel):
    pass


type EnchantmentEffectComponentMap = dict[Annotated[str, IdSpec(registry='enchantment_effect_component_type')], list[AmmoUseEnchantmentEffect] | list[ArmorEffectivenessEnchantmentEffect] | list[AttributeEffect] | list[BlockExperienceEnchantmentEffect] | ValueEffect | list[CrossbowChargeSoundsEnchantmentEffect] | list[DamageEnchantmentEffect] | list[DamageImmunityEnchantmentEffect] | list[DamageProtectionEnchantmentEffect] | list[EquipmentDropsEnchantmentEffect] | list[FishingLuckBonusEnchantmentEffect] | list[FishingTimeReductionEnchantmentEffect] | list[HitBlockEnchantmentEffect] | list[ItemDamageEnchantmentEffect] | list[KnockbackEnchantmentEffect] | list[LocationChangedEnchantmentEffect] | list[MobExperienceEnchantmentEffect] | list[PostAttackEnchantmentEffect] | list[PostPiercingAttackEnchantmentEffect] | EnchantmentEffectComponentMapValueStructEffectComponentPreventArmorChange | list[ProjectileCountEnchantmentEffect] | list[ProjectilePiercingEnchantmentEffect] | list[ProjectileSpawnedEnchantmentEffect] | list[ProjectileSpreadEnchantmentEffect] | list[RepairWithXpEnchantmentEffect] | list[SmashDamagePerBlockFallenEnchantmentEffect] | list[TickEnchantmentEffect] | list[TridentReturnAccelerationEnchantmentEffect] | list[SoundEventRef]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::EnchantmentEffectComponentMap": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "enchantment_effect_component_type"
                                }
                            }
                        }
                    ]
                },
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                {
                                    "keyword": "key"
                                }
                            ]
                        }
                    ],
                    "registry": "minecraft:effect_component"
                },
                "optional": True
            }
        ]
    }
}
