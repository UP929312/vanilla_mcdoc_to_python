"""
Generated from symbols.json for ::java::data::enchantment::effect_component::EnchantmentEffectComponentMap
Local link to file: generated_symbols/data/enchantment/effect_component/EnchantmentEffectComponentMap.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.AttributeEffect import AttributeEffect
    from generated_symbols.data.enchantment.effect.ValueEffect import ValueEffect
    from generated_symbols.data.enchantment.effect_component.AmmoUseEnchantmentEffect import AmmoUseEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.ArmorEffectivenessEnchantmentEffect import ArmorEffectivenessEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.BlockExperienceEnchantmentEffect import BlockExperienceEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.CrossbowChargeSoundsEnchantmentEffect import CrossbowChargeSoundsEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.DamageEnchantmentEffect import DamageEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.DamageImmunityEnchantmentEffect import DamageImmunityEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.DamageProtectionEnchantmentEffect import DamageProtectionEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.EquipmentDropsEnchantmentEffect import EquipmentDropsEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.FishingLuckBonusEnchantmentEffect import FishingLuckBonusEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.FishingTimeReductionEnchantmentEffect import FishingTimeReductionEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.HitBlockEnchantmentEffect import HitBlockEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.ItemDamageEnchantmentEffect import ItemDamageEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.KnockbackEnchantmentEffect import KnockbackEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.LocationChangedEnchantmentEffect import LocationChangedEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.MobExperienceEnchantmentEffect import MobExperienceEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.PostAttackEnchantmentEffect import PostAttackEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.PostPiercingAttackEnchantmentEffect import PostPiercingAttackEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.ProjectileCountEnchantmentEffect import ProjectileCountEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.ProjectilePiercingEnchantmentEffect import ProjectilePiercingEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.ProjectileSpawnedEnchantmentEffect import ProjectileSpawnedEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.ProjectileSpreadEnchantmentEffect import ProjectileSpreadEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.RepairWithXpEnchantmentEffect import RepairWithXpEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.SmashDamagePerBlockFallenEnchantmentEffect import SmashDamagePerBlockFallenEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.TickEnchantmentEffect import TickEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.TridentReturnAccelerationEnchantmentEffect import TridentReturnAccelerationEnchantmentEffect
    from generated_symbols.data.util.SoundEventRef import SoundEventRef


@dataclass(kw_only=True)
class EnchantmentEffectComponentMapValueStructEffectComponentPreventArmorChange:
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

