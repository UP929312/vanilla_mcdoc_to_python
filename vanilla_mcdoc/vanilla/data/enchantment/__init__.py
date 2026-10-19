"""Vanilla's data/enchantment/ files"""
from typing import Any
from vanilla_mcdoc.data.advancement.predicate.BlockPredicate import BlockPredicate
from vanilla_mcdoc.data.advancement.predicate.DamageSourcePredicate import DamageSourcePredicate
from vanilla_mcdoc.data.advancement.predicate.DamageTagPredicate import DamageTagPredicate
from vanilla_mcdoc.data.advancement.predicate.EntityFlagsPredicate import EntityFlagsPredicate
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.advancement.predicate.GameMode import GameMode
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate
from vanilla_mcdoc.data.advancement.predicate.MovementPredicate import MovementPredicate
from vanilla_mcdoc.data.advancement.predicate.PlayerPredicate import FoodStruct, PlayerPredicate
from vanilla_mcdoc.data.enchantment.Enchantment import Enchantment
from vanilla_mcdoc.data.enchantment.EnchantmentCost import EnchantmentCost
from vanilla_mcdoc.data.enchantment.effect.AttributeEffect import AttributeEffect
from vanilla_mcdoc.data.enchantment.effect.BlockInteraction import BlockInteraction
from vanilla_mcdoc.data.enchantment.effect.EntityEffect import EntityEffectAllOf, EntityEffectApplyExhaustion, EntityEffectApplyImpulse, EntityEffectApplyMobEffect, EntityEffectChangeItemDamage, EntityEffectDamageEntity, EntityEffectExplode, EntityEffectIgnite, EntityEffectPlaySound, EntityEffectSpawnParticles, EntityEffectSummonEntity
from vanilla_mcdoc.data.enchantment.effect.LocationBasedEffect import LocationBasedEffectAllOf, LocationBasedEffectAttribute, LocationBasedEffectChangeItemDamage, LocationBasedEffectReplaceDisk
from vanilla_mcdoc.data.enchantment.effect.ParticlePosition import ParticlePosition
from vanilla_mcdoc.data.enchantment.effect.ParticleVelocity import ParticleVelocity
from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffectAdd, ValueEffectMultiply, ValueEffectRemoveBinomial, ValueEffectSet
from vanilla_mcdoc.data.enchantment.effect_component.AmmoUseEnchantmentEffect import AmmoUseEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.ArmorEffectivenessEnchantmentEffect import ArmorEffectivenessEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.AttackTarget import AttackTarget
from vanilla_mcdoc.data.enchantment.effect_component.BlockExperienceEnchantmentEffect import BlockExperienceEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.CrossbowChargeSoundsEnchantmentEffect import CrossbowChargeSoundsEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.DamageEnchantmentEffect import DamageEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.DamageImmunityEnchantmentEffect import DamageImmunityEnchantmentEffect, EffectStruct
from vanilla_mcdoc.data.enchantment.effect_component.DamageProtectionEnchantmentEffect import DamageProtectionEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.EnchantmentEffectComponentMap import EnchantmentEffectComponentMap, PreventArmorChangeStruct, PreventEquipmentDropStruct
from vanilla_mcdoc.data.enchantment.effect_component.EquipmentDropsEnchantmentEffect import EquipmentDropsEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.FishingLuckBonusEnchantmentEffect import FishingLuckBonusEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.FishingTimeReductionEnchantmentEffect import FishingTimeReductionEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.HitBlockEnchantmentEffect import HitBlockEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.ItemDamageEnchantmentEffect import ItemDamageEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.KnockbackEnchantmentEffect import KnockbackEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.LocationChangedEnchantmentEffect import LocationChangedEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.PostAttackEnchantmentEffect import PostAttackEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.PostPiercingAttackEnchantmentEffect import PostPiercingAttackEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.ProjectileCountEnchantmentEffect import ProjectileCountEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.ProjectilePiercingEnchantmentEffect import ProjectilePiercingEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.ProjectileSpawnedEnchantmentEffect import ProjectileSpawnedEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.ProjectileSpreadEnchantmentEffect import ProjectileSpreadEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.RepairWithXpEnchantmentEffect import RepairWithXpEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.TickEnchantmentEffect import TickEnchantmentEffect
from vanilla_mcdoc.data.enchantment.effect_component.TridentReturnAccelerationEnchantmentEffect import TridentReturnAccelerationEnchantmentEffect
from vanilla_mcdoc.data.enchantment.level_based_value.LevelBasedValueMap import LevelBasedValueMapClamped, LevelBasedValueMapFraction, LevelBasedValueMapLevelsSquared, LevelBasedValueMapLinear, LevelBasedValueMapLookup
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionAllOf, LootConditionAnyOf, LootConditionDamageSourceProperties, LootConditionEnchantmentActiveCheck, LootConditionEntityProperties, LootConditionInverted, LootConditionLocationCheck, LootConditionMatchTool, LootConditionRandomChance, LootConditionWeatherCheck
from vanilla_mcdoc.data.number_provider.context_float.ContextFloatProvider import ContextFloatProviderStructEnchantmentLevel
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
from vanilla_mcdoc.data.worldgen.FloatProvider import FloatProvider
from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicateAllOf, BlockPredicateMatchingBlockTag, BlockPredicateMatchingBlocks, BlockPredicateMatchingFluids, BlockPredicateUnobstructed
from vanilla_mcdoc.util.attribute.AttributeOperation import AttributeOperation
from vanilla_mcdoc.util.block_state.FullBlockState import FullBlockState
from vanilla_mcdoc.util.particle.Particle import ParticleDefault
from vanilla_mcdoc.util.slot.EquipmentSlotGroup import EquipmentSlotGroup
from vanilla_mcdoc.util.text.TextObject import TextObjectStruct2

AQUA_AFFINITY = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.aqua_affinity'),
    supported_items='#minecraft:enchantable/head_armor',
    weight=2,
    max_level=1,
    min_cost=EnchantmentCost(base=1, per_level_above_first=0),
    max_cost=EnchantmentCost(base=41, per_level_above_first=0),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.HEAD],
    effects=EnchantmentEffectComponentMap(
        attributes=[
            AttributeEffect(
                attribute='minecraft:submerged_mining_speed',
                id='minecraft:enchantment.aqua_affinity',
                amount=LevelBasedValueMapLinear(base=4.0, per_level_above_first=4.0, type='minecraft:linear'),
                operation=AttributeOperation.ADDMULTIPLIEDTOTAL,
            ),
        ],
    ),
)

BANE_OF_ARTHROPODS = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.bane_of_arthropods'),
    exclusive_set='#minecraft:exclusive_set/damage',
    supported_items='#minecraft:enchantable/weapon',
    primary_items='#minecraft:enchantable/melee_weapon',
    weight=5,
    max_level=5,
    min_cost=EnchantmentCost(base=5, per_level_above_first=8),
    max_cost=EnchantmentCost(base=25, per_level_above_first=8),
    anvil_cost=2,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        damage=[
            DamageEnchantmentEffect(
                requirements=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='#minecraft:sensitive_to_bane_of_arthropods'),
                    type='minecraft:entity_properties',
                ),
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=2.5, per_level_above_first=2.5, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
        post_attack=[
            PostAttackEnchantmentEffect(
                requirements=LootConditionAllOf(
                    terms=[
                        LootConditionEntityProperties(
                            entity=EntityTarget.THIS,
                            predicate=EntitySubPredicateMap(entity_type='#minecraft:sensitive_to_bane_of_arthropods'),
                            type='minecraft:entity_properties',
                        ),
                        LootConditionDamageSourceProperties(
                            predicate=DamageSourcePredicate(is_direct=True),
                            type='minecraft:damage_source_properties',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
                effect=EntityEffectApplyMobEffect(
                    to_apply='minecraft:slowness',
                    min_duration=1.5,
                    max_duration=LevelBasedValueMapLinear(base=1.5, per_level_above_first=0.5, type='minecraft:linear'),
                    min_amplifier=3.0,
                    max_amplifier=3.0,
                    type='minecraft:apply_mob_effect',
                ),
                enchanted=AttackTarget.ATTACKER,
                affected=AttackTarget.VICTIM,
            ),
        ],
    ),
)

BINDING_CURSE = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.binding_curse'),
    supported_items='#minecraft:enchantable/equippable',
    weight=1,
    max_level=1,
    min_cost=EnchantmentCost(base=25, per_level_above_first=0),
    max_cost=EnchantmentCost(base=50, per_level_above_first=0),
    anvil_cost=8,
    slots=[EquipmentSlotGroup.ARMOR],
    effects=EnchantmentEffectComponentMap(prevent_armor_change=PreventArmorChangeStruct()),
)

BLAST_PROTECTION = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.blast_protection'),
    exclusive_set='#minecraft:exclusive_set/armor',
    supported_items='#minecraft:enchantable/armor',
    weight=2,
    max_level=4,
    min_cost=EnchantmentCost(base=5, per_level_above_first=8),
    max_cost=EnchantmentCost(base=13, per_level_above_first=8),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.ARMOR],
    effects=EnchantmentEffectComponentMap(
        attributes=[
            AttributeEffect(
                attribute='minecraft:explosion_knockback_resistance',
                id='minecraft:enchantment.blast_protection',
                amount=LevelBasedValueMapLinear(base=0.15, per_level_above_first=0.15, type='minecraft:linear'),
                operation=AttributeOperation.ADDVALUE,
            ),
        ],
        damage_protection=[
            DamageProtectionEnchantmentEffect(
                requirements=LootConditionDamageSourceProperties(
                    predicate=DamageSourcePredicate(
                        tags=[
                            DamageTagPredicate(id='#minecraft:is_explosion', expected=True),
                            DamageTagPredicate(id='#minecraft:bypasses_invulnerability', expected=False),
                        ],
                    ),
                    type='minecraft:damage_source_properties',
                ),
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=2.0, per_level_above_first=2.0, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

BREACH = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.breach'),
    exclusive_set='#minecraft:exclusive_set/damage',
    supported_items='#minecraft:enchantable/mace',
    weight=2,
    max_level=4,
    min_cost=EnchantmentCost(base=15, per_level_above_first=9),
    max_cost=EnchantmentCost(base=65, per_level_above_first=9),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        armor_effectiveness=[
            ArmorEffectivenessEnchantmentEffect(
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=-0.15, per_level_above_first=-0.15, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

CHANNELING = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.channeling'),
    supported_items='#minecraft:enchantable/trident',
    weight=1,
    max_level=1,
    min_cost=EnchantmentCost(base=25, per_level_above_first=0),
    max_cost=EnchantmentCost(base=50, per_level_above_first=0),
    anvil_cost=8,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        hit_block=[
            HitBlockEnchantmentEffect(
                requirements=LootConditionAllOf(
                    terms=[
                        LootConditionWeatherCheck(thundering=True, type='minecraft:weather_check'),
                        LootConditionEntityProperties(
                            entity=EntityTarget.THIS,
                            predicate=EntitySubPredicateMap(entity_type='minecraft:trident'),
                            type='minecraft:entity_properties',
                        ),
                        LootConditionLocationCheck(
                            predicate=LocationPredicate(
                                block=BlockPredicate(blocks='#minecraft:lightning_rods'),
                                can_see_sky=True,
                            ),
                            type='minecraft:location_check',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
                effect=EntityEffectAllOf(
                    effects=[
                        EntityEffectSummonEntity(entity='minecraft:lightning_bolt', type='minecraft:summon_entity'),
                        EntityEffectPlaySound(
                            sound='minecraft:item.trident.thunder',
                            volume=5.0,
                            pitch=1.0,
                            type='minecraft:play_sound',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
            ),
        ],
        post_attack=[
            PostAttackEnchantmentEffect(
                requirements=LootConditionAllOf(
                    terms=[
                        LootConditionWeatherCheck(thundering=True, type='minecraft:weather_check'),
                        LootConditionEntityProperties(
                            entity=EntityTarget.THIS,
                            predicate=EntitySubPredicateMap(location=LocationPredicate(can_see_sky=True)),
                            type='minecraft:entity_properties',
                        ),
                        LootConditionEntityProperties(
                            entity=EntityTarget.DIRECTATTACKER,
                            predicate=EntitySubPredicateMap(entity_type='minecraft:trident'),
                            type='minecraft:entity_properties',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
                effect=EntityEffectAllOf(
                    effects=[
                        EntityEffectSummonEntity(entity='minecraft:lightning_bolt', type='minecraft:summon_entity'),
                        EntityEffectPlaySound(
                            sound='minecraft:item.trident.thunder',
                            volume=5.0,
                            pitch=1.0,
                            type='minecraft:play_sound',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
                enchanted=AttackTarget.ATTACKER,
                affected=AttackTarget.VICTIM,
            ),
        ],
    ),
)

DENSITY = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.density'),
    exclusive_set='#minecraft:exclusive_set/damage',
    supported_items='#minecraft:enchantable/mace',
    weight=5,
    max_level=5,
    min_cost=EnchantmentCost(base=5, per_level_above_first=8),
    max_cost=EnchantmentCost(base=25, per_level_above_first=8),
    anvil_cost=2,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        **dict[str, Any]({
            'minecraft:smash_damage_per_fallen_block': [
                {
                    'effect': {
                        'type': 'minecraft:add',
                        'value': {'type': 'minecraft:linear', 'base': 0.5, 'per_level_above_first': 0.5},
                    },
                },
            ],
        }),
    ),
)

DEPTH_STRIDER = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.depth_strider'),
    exclusive_set='#minecraft:exclusive_set/boots',
    supported_items='#minecraft:enchantable/foot_armor',
    weight=2,
    max_level=3,
    min_cost=EnchantmentCost(base=10, per_level_above_first=10),
    max_cost=EnchantmentCost(base=25, per_level_above_first=10),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.FEET],
    effects=EnchantmentEffectComponentMap(
        attributes=[
            AttributeEffect(
                attribute='minecraft:water_movement_efficiency',
                id='minecraft:enchantment.depth_strider',
                amount=LevelBasedValueMapLinear(base=0.33333334, per_level_above_first=0.33333334, type='minecraft:linear'),
                operation=AttributeOperation.ADDVALUE,
            ),
        ],
    ),
)

EFFICIENCY = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.efficiency'),
    supported_items='#minecraft:enchantable/mining',
    weight=10,
    max_level=5,
    min_cost=EnchantmentCost(base=1, per_level_above_first=10),
    max_cost=EnchantmentCost(base=51, per_level_above_first=10),
    anvil_cost=1,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        attributes=[
            AttributeEffect(
                attribute='minecraft:mining_efficiency',
                id='minecraft:enchantment.efficiency',
                amount=LevelBasedValueMapLevelsSquared(added=1.0, type='minecraft:levels_squared'),
                operation=AttributeOperation.ADDVALUE,
            ),
        ],
    ),
)

FEATHER_FALLING = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.feather_falling'),
    supported_items='#minecraft:enchantable/foot_armor',
    weight=5,
    max_level=4,
    min_cost=EnchantmentCost(base=5, per_level_above_first=6),
    max_cost=EnchantmentCost(base=11, per_level_above_first=6),
    anvil_cost=2,
    slots=[EquipmentSlotGroup.ARMOR],
    effects=EnchantmentEffectComponentMap(
        damage_protection=[
            DamageProtectionEnchantmentEffect(
                requirements=LootConditionDamageSourceProperties(
                    predicate=DamageSourcePredicate(
                        tags=[
                            DamageTagPredicate(id='#minecraft:is_fall', expected=True),
                            DamageTagPredicate(id='#minecraft:bypasses_invulnerability', expected=False),
                        ],
                    ),
                    type='minecraft:damage_source_properties',
                ),
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=3.0, per_level_above_first=3.0, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

FIRE_ASPECT = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.fire_aspect'),
    supported_items='#minecraft:enchantable/fire_aspect',
    primary_items='#minecraft:enchantable/melee_weapon',
    weight=2,
    max_level=2,
    min_cost=EnchantmentCost(base=10, per_level_above_first=20),
    max_cost=EnchantmentCost(base=60, per_level_above_first=20),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        post_attack=[
            PostAttackEnchantmentEffect(
                requirements=LootConditionDamageSourceProperties(
                    predicate=DamageSourcePredicate(is_direct=True),
                    type='minecraft:damage_source_properties',
                ),
                effect=EntityEffectIgnite(
                    duration=LevelBasedValueMapLinear(base=4.0, per_level_above_first=4.0, type='minecraft:linear'),
                    type='minecraft:ignite',
                ),
                enchanted=AttackTarget.ATTACKER,
                affected=AttackTarget.VICTIM,
            ),
        ],
    ),
)

FIRE_PROTECTION = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.fire_protection'),
    exclusive_set='#minecraft:exclusive_set/armor',
    supported_items='#minecraft:enchantable/armor',
    weight=5,
    max_level=4,
    min_cost=EnchantmentCost(base=10, per_level_above_first=8),
    max_cost=EnchantmentCost(base=18, per_level_above_first=8),
    anvil_cost=2,
    slots=[EquipmentSlotGroup.ARMOR],
    effects=EnchantmentEffectComponentMap(
        attributes=[
            AttributeEffect(
                attribute='minecraft:burning_time',
                id='minecraft:enchantment.fire_protection',
                amount=LevelBasedValueMapLinear(base=-0.15, per_level_above_first=-0.15, type='minecraft:linear'),
                operation=AttributeOperation.ADDMULTIPLIEDBASE,
            ),
        ],
        damage_protection=[
            DamageProtectionEnchantmentEffect(
                requirements=LootConditionDamageSourceProperties(
                    predicate=DamageSourcePredicate(
                        tags=[
                            DamageTagPredicate(id='#minecraft:is_fire', expected=True),
                            DamageTagPredicate(id='#minecraft:bypasses_invulnerability', expected=False),
                        ],
                    ),
                    type='minecraft:damage_source_properties',
                ),
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=2.0, per_level_above_first=2.0, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

FLAME = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.flame'),
    supported_items='#minecraft:enchantable/bow',
    weight=2,
    max_level=1,
    min_cost=EnchantmentCost(base=20, per_level_above_first=0),
    max_cost=EnchantmentCost(base=50, per_level_above_first=0),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        projectile_spawned=[ProjectileSpawnedEnchantmentEffect(effect=EntityEffectIgnite(duration=100.0, type='minecraft:ignite'))],
    ),
)

FORTUNE = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.fortune'),
    exclusive_set='#minecraft:exclusive_set/mining',
    supported_items='#minecraft:enchantable/mining_loot',
    weight=2,
    max_level=3,
    min_cost=EnchantmentCost(base=15, per_level_above_first=9),
    max_cost=EnchantmentCost(base=65, per_level_above_first=9),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.MAINHAND],
)

FROST_WALKER = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.frost_walker'),
    exclusive_set='#minecraft:exclusive_set/boots',
    supported_items='#minecraft:enchantable/foot_armor',
    weight=2,
    max_level=2,
    min_cost=EnchantmentCost(base=10, per_level_above_first=10),
    max_cost=EnchantmentCost(base=25, per_level_above_first=10),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.FEET],
    effects=EnchantmentEffectComponentMap(
        damage_immunity=[
            DamageImmunityEnchantmentEffect(
                requirements=LootConditionDamageSourceProperties(
                    predicate=DamageSourcePredicate(
                        tags=[
                            DamageTagPredicate(id='#minecraft:burn_from_stepping', expected=True),
                            DamageTagPredicate(id='#minecraft:bypasses_invulnerability', expected=False),
                        ],
                    ),
                    type='minecraft:damage_source_properties',
                ),
                effect=EffectStruct(),
            ),
        ],
        location_changed=[
            LocationChangedEnchantmentEffect(
                requirements=LootConditionAllOf(
                    terms=[
                        LootConditionEntityProperties(
                            entity=EntityTarget.THIS,
                            predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_ground=True)),
                            type='minecraft:entity_properties',
                        ),
                        LootConditionInverted(
                            term=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(vehicle=EntitySubPredicateMap()),
                                type='minecraft:entity_properties',
                            ),
                            type='minecraft:inverted',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
                effect=LocationBasedEffectReplaceDisk(
                    block_state=FullBlockState(id='minecraft:frosted_ice', properties={'age': '0'}),
                    offset=(0, -1, 0),
                    predicate=BlockPredicateAllOf(
                        predicates=[
                            BlockPredicateMatchingBlockTag(
                                offset=(0, 1, 0),
                                tag='minecraft:air',
                                type='minecraft:matching_block_tag',
                            ),
                            BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
                            BlockPredicateMatchingFluids(
                                fluids='minecraft:water',
                                state={'source': 'true'},
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateUnobstructed(type='minecraft:unobstructed'),
                        ],
                        type='minecraft:all_of',
                    ),
                    trigger_game_event='minecraft:block_place',
                    radius=LevelBasedValueMapClamped(
                        value=LevelBasedValueMapLinear(base=3.0, per_level_above_first=1.0, type='minecraft:linear'),
                        min=0.0,
                        max=16.0,
                        type='minecraft:clamped',
                    ),
                    height=1.0,
                    type='minecraft:replace_disk',
                ),
            ),
        ],
    ),
)

IMPALING = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.impaling'),
    exclusive_set='#minecraft:exclusive_set/damage',
    supported_items='#minecraft:enchantable/trident',
    weight=2,
    max_level=5,
    min_cost=EnchantmentCost(base=1, per_level_above_first=8),
    max_cost=EnchantmentCost(base=21, per_level_above_first=8),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        damage=[
            DamageEnchantmentEffect(
                requirements=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='#minecraft:sensitive_to_impaling'),
                    type='minecraft:entity_properties',
                ),
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=2.5, per_level_above_first=2.5, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

INFINITY = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.infinity'),
    exclusive_set='#minecraft:exclusive_set/bow',
    supported_items='#minecraft:enchantable/bow',
    weight=1,
    max_level=1,
    min_cost=EnchantmentCost(base=20, per_level_above_first=0),
    max_cost=EnchantmentCost(base=50, per_level_above_first=0),
    anvil_cost=8,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        ammo_use=[
            AmmoUseEnchantmentEffect(
                requirements=LootConditionMatchTool(predicate=ItemPredicate(items='minecraft:arrow'), type='minecraft:match_tool'),
                effect=ValueEffectSet(value=0.0, type='minecraft:set'),
            ),
        ],
    ),
)

KNOCKBACK = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.knockback'),
    supported_items='#minecraft:enchantable/melee_weapon',
    weight=5,
    max_level=2,
    min_cost=EnchantmentCost(base=5, per_level_above_first=20),
    max_cost=EnchantmentCost(base=55, per_level_above_first=20),
    anvil_cost=2,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        knockback=[
            KnockbackEnchantmentEffect(
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=1.0, per_level_above_first=1.0, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

LOOTING = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.looting'),
    supported_items='#minecraft:enchantable/melee_weapon',
    weight=2,
    max_level=3,
    min_cost=EnchantmentCost(base=15, per_level_above_first=9),
    max_cost=EnchantmentCost(base=65, per_level_above_first=9),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        equipment_drops=[
            EquipmentDropsEnchantmentEffect(
                requirements=LootConditionEntityProperties(
                    entity=EntityTarget.ATTACKER,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:player'),
                    type='minecraft:entity_properties',
                ),
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=0.01, per_level_above_first=0.01, type='minecraft:linear'),
                    type='minecraft:add',
                ),
                enchanted='attacker',
            ),
        ],
    ),
)

LOYALTY = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.loyalty'),
    supported_items='#minecraft:enchantable/trident',
    weight=5,
    max_level=3,
    min_cost=EnchantmentCost(base=12, per_level_above_first=7),
    max_cost=EnchantmentCost(base=50, per_level_above_first=0),
    anvil_cost=2,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        trident_return_acceleration=[
            TridentReturnAccelerationEnchantmentEffect(
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=1.0, per_level_above_first=1.0, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

LUCK_OF_THE_SEA = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.luck_of_the_sea'),
    supported_items='#minecraft:enchantable/fishing',
    weight=2,
    max_level=3,
    min_cost=EnchantmentCost(base=15, per_level_above_first=9),
    max_cost=EnchantmentCost(base=65, per_level_above_first=9),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        fishing_luck_bonus=[
            FishingLuckBonusEnchantmentEffect(
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=1.0, per_level_above_first=1.0, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

LUNGE = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.lunge'),
    supported_items='#minecraft:enchantable/lunge',
    weight=5,
    max_level=3,
    min_cost=EnchantmentCost(base=5, per_level_above_first=8),
    max_cost=EnchantmentCost(base=25, per_level_above_first=8),
    anvil_cost=2,
    slots=[EquipmentSlotGroup.HAND],
    effects=EnchantmentEffectComponentMap(
        post_piercing_attack=[
            PostPiercingAttackEnchantmentEffect(
                requirements=LootConditionAllOf(
                    terms=[
                        LootConditionInverted(
                            term=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(vehicle=EntitySubPredicateMap()),
                                type='minecraft:entity_properties',
                            ),
                            type='minecraft:inverted',
                        ),
                        LootConditionEntityProperties(
                            entity=EntityTarget.THIS,
                            predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_fall_flying=False)),
                            type='minecraft:entity_properties',
                        ),
                        LootConditionEntityProperties(
                            entity=EntityTarget.THIS,
                            predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_in_water=False)),
                            type='minecraft:entity_properties',
                        ),
                        LootConditionAnyOf(
                            terms=[
                                LootConditionInverted(
                                    term=LootConditionEntityProperties(
                                        entity=EntityTarget.THIS,
                                        predicate=EntitySubPredicateMap(type_specific_player=PlayerPredicate()),
                                        type='minecraft:entity_properties',
                                    ),
                                    type='minecraft:inverted',
                                ),
                                LootConditionEntityProperties(
                                    entity=EntityTarget.THIS,
                                    predicate=EntitySubPredicateMap(
                                        type_specific_player=PlayerPredicate(gamemode=[GameMode.CREATIVE]),
                                    ),
                                    type='minecraft:entity_properties',
                                ),
                                LootConditionEntityProperties(
                                    entity=EntityTarget.THIS,
                                    predicate=EntitySubPredicateMap(
                                        type_specific_player=PlayerPredicate(food=FoodStruct(level=MinMaxBounds(min=7))),
                                    ),
                                    type='minecraft:entity_properties',
                                ),
                            ],
                            type='minecraft:any_of',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
                effect=EntityEffectAllOf(
                    effects=[
                        EntityEffectChangeItemDamage(amount=1.0, type='minecraft:change_item_damage'),
                        EntityEffectApplyExhaustion(
                            amount=LevelBasedValueMapLinear(base=4.0, per_level_above_first=4.0, type='minecraft:linear'),
                            type='minecraft:apply_exhaustion',
                        ),
                        EntityEffectApplyImpulse(
                            direction=(0.0, 0.0, 1.0),
                            coordinate_scale=(1.0, 0.0, 1.0),
                            magnitude=LevelBasedValueMapLinear(base=0.458, per_level_above_first=0.458, type='minecraft:linear'),
                            type='minecraft:apply_impulse',
                        ),
                        EntityEffectPlaySound(
                            sound=[
                                'minecraft:item.spear.lunge_1',
                                'minecraft:item.spear.lunge_2',
                                'minecraft:item.spear.lunge_3',
                            ],
                            volume=1.0,
                            pitch=1.0,
                            type='minecraft:play_sound',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
            ),
        ],
    ),
)

LURE = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.lure'),
    supported_items='#minecraft:enchantable/fishing',
    weight=2,
    max_level=3,
    min_cost=EnchantmentCost(base=15, per_level_above_first=9),
    max_cost=EnchantmentCost(base=65, per_level_above_first=9),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        fishing_time_reduction=[
            FishingTimeReductionEnchantmentEffect(
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=5.0, per_level_above_first=5.0, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

MENDING = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.mending'),
    supported_items='#minecraft:enchantable/durability',
    weight=2,
    max_level=1,
    min_cost=EnchantmentCost(base=25, per_level_above_first=25),
    max_cost=EnchantmentCost(base=75, per_level_above_first=25),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.ANY],
    effects=EnchantmentEffectComponentMap(
        repair_with_xp=[RepairWithXpEnchantmentEffect(effect=ValueEffectMultiply(factor=2.0, type='minecraft:multiply'))],
    ),
)

MULTISHOT = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.multishot'),
    exclusive_set='#minecraft:exclusive_set/crossbow',
    supported_items='#minecraft:enchantable/crossbow',
    weight=2,
    max_level=1,
    min_cost=EnchantmentCost(base=20, per_level_above_first=0),
    max_cost=EnchantmentCost(base=50, per_level_above_first=0),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        projectile_count=[
            ProjectileCountEnchantmentEffect(
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=2.0, per_level_above_first=2.0, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
        projectile_spread=[
            ProjectileSpreadEnchantmentEffect(
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=10.0, per_level_above_first=10.0, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

PIERCING = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.piercing'),
    exclusive_set='#minecraft:exclusive_set/crossbow',
    supported_items='#minecraft:enchantable/crossbow',
    weight=10,
    max_level=4,
    min_cost=EnchantmentCost(base=1, per_level_above_first=10),
    max_cost=EnchantmentCost(base=50, per_level_above_first=0),
    anvil_cost=1,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        projectile_piercing=[
            ProjectilePiercingEnchantmentEffect(
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=1.0, per_level_above_first=1.0, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

POWER = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.power'),
    supported_items='#minecraft:enchantable/bow',
    weight=10,
    max_level=5,
    min_cost=EnchantmentCost(base=1, per_level_above_first=10),
    max_cost=EnchantmentCost(base=16, per_level_above_first=10),
    anvil_cost=1,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        damage=[
            DamageEnchantmentEffect(
                requirements=LootConditionEntityProperties(
                    entity=EntityTarget.DIRECTATTACKER,
                    predicate=EntitySubPredicateMap(entity_type='#minecraft:arrows'),
                    type='minecraft:entity_properties',
                ),
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=1.0, per_level_above_first=0.5, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

PROJECTILE_PROTECTION = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.projectile_protection'),
    exclusive_set='#minecraft:exclusive_set/armor',
    supported_items='#minecraft:enchantable/armor',
    weight=5,
    max_level=4,
    min_cost=EnchantmentCost(base=3, per_level_above_first=6),
    max_cost=EnchantmentCost(base=9, per_level_above_first=6),
    anvil_cost=2,
    slots=[EquipmentSlotGroup.ARMOR],
    effects=EnchantmentEffectComponentMap(
        damage_protection=[
            DamageProtectionEnchantmentEffect(
                requirements=LootConditionDamageSourceProperties(
                    predicate=DamageSourcePredicate(
                        tags=[
                            DamageTagPredicate(id='#minecraft:is_projectile', expected=True),
                            DamageTagPredicate(id='#minecraft:bypasses_invulnerability', expected=False),
                        ],
                    ),
                    type='minecraft:damage_source_properties',
                ),
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=2.0, per_level_above_first=2.0, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

PROTECTION = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.protection'),
    exclusive_set='#minecraft:exclusive_set/armor',
    supported_items='#minecraft:enchantable/armor',
    weight=10,
    max_level=4,
    min_cost=EnchantmentCost(base=1, per_level_above_first=11),
    max_cost=EnchantmentCost(base=12, per_level_above_first=11),
    anvil_cost=1,
    slots=[EquipmentSlotGroup.ARMOR],
    effects=EnchantmentEffectComponentMap(
        damage_protection=[
            DamageProtectionEnchantmentEffect(
                requirements=LootConditionDamageSourceProperties(
                    predicate=DamageSourcePredicate(
                        tags=[DamageTagPredicate(id='#minecraft:bypasses_invulnerability', expected=False)],
                    ),
                    type='minecraft:damage_source_properties',
                ),
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=1.0, per_level_above_first=1.0, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

PUNCH = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.punch'),
    supported_items='#minecraft:enchantable/bow',
    weight=2,
    max_level=2,
    min_cost=EnchantmentCost(base=12, per_level_above_first=20),
    max_cost=EnchantmentCost(base=37, per_level_above_first=20),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        knockback=[
            KnockbackEnchantmentEffect(
                requirements=LootConditionEntityProperties(
                    entity=EntityTarget.DIRECTATTACKER,
                    predicate=EntitySubPredicateMap(entity_type='#minecraft:arrows'),
                    type='minecraft:entity_properties',
                ),
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=1.0, per_level_above_first=1.0, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

QUICK_CHARGE = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.quick_charge'),
    supported_items='#minecraft:enchantable/crossbow',
    weight=5,
    max_level=3,
    min_cost=EnchantmentCost(base=12, per_level_above_first=20),
    max_cost=EnchantmentCost(base=50, per_level_above_first=0),
    anvil_cost=2,
    slots=[EquipmentSlotGroup.MAINHAND, EquipmentSlotGroup.OFFHAND],
    effects=EnchantmentEffectComponentMap(
        crossbow_charge_time=ValueEffectAdd(
            value=LevelBasedValueMapLinear(base=-0.25, per_level_above_first=-0.25, type='minecraft:linear'),
            type='minecraft:add',
        ),
        crossbow_charging_sounds=[
            CrossbowChargeSoundsEnchantmentEffect(
                start='minecraft:item.crossbow.quick_charge_1',
                end='minecraft:item.crossbow.loading_end',
            ),
            CrossbowChargeSoundsEnchantmentEffect(
                start='minecraft:item.crossbow.quick_charge_2',
                end='minecraft:item.crossbow.loading_end',
            ),
            CrossbowChargeSoundsEnchantmentEffect(
                start='minecraft:item.crossbow.quick_charge_3',
                end='minecraft:item.crossbow.loading_end',
            ),
        ],
    ),
)

RESPIRATION = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.respiration'),
    supported_items='#minecraft:enchantable/head_armor',
    weight=2,
    max_level=3,
    min_cost=EnchantmentCost(base=10, per_level_above_first=10),
    max_cost=EnchantmentCost(base=40, per_level_above_first=10),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.HEAD],
    effects=EnchantmentEffectComponentMap(
        attributes=[
            AttributeEffect(
                attribute='minecraft:oxygen_bonus',
                id='minecraft:enchantment.respiration',
                amount=LevelBasedValueMapLinear(base=1.0, per_level_above_first=1.0, type='minecraft:linear'),
                operation=AttributeOperation.ADDVALUE,
            ),
        ],
    ),
)

RIPTIDE = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.riptide'),
    exclusive_set='#minecraft:exclusive_set/riptide',
    supported_items='#minecraft:enchantable/trident',
    weight=2,
    max_level=3,
    min_cost=EnchantmentCost(base=17, per_level_above_first=7),
    max_cost=EnchantmentCost(base=50, per_level_above_first=0),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.HAND],
    effects=EnchantmentEffectComponentMap(
        trident_sound=['minecraft:item.trident.riptide_1', 'minecraft:item.trident.riptide_2', 'minecraft:item.trident.riptide_3'],
        trident_spin_attack_strength=ValueEffectAdd(
            value=LevelBasedValueMapLinear(base=1.5, per_level_above_first=0.75, type='minecraft:linear'),
            type='minecraft:add',
        ),
    ),
)

SHARPNESS = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.sharpness'),
    exclusive_set='#minecraft:exclusive_set/damage',
    supported_items='#minecraft:enchantable/sharp_weapon',
    primary_items='#minecraft:enchantable/melee_weapon',
    weight=10,
    max_level=5,
    min_cost=EnchantmentCost(base=1, per_level_above_first=11),
    max_cost=EnchantmentCost(base=21, per_level_above_first=11),
    anvil_cost=1,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        damage=[
            DamageEnchantmentEffect(
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=1.0, per_level_above_first=0.5, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

SILK_TOUCH = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.silk_touch'),
    exclusive_set='#minecraft:exclusive_set/mining',
    supported_items='#minecraft:enchantable/mining_loot',
    weight=1,
    max_level=1,
    min_cost=EnchantmentCost(base=15, per_level_above_first=0),
    max_cost=EnchantmentCost(base=65, per_level_above_first=0),
    anvil_cost=8,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        block_experience=[BlockExperienceEnchantmentEffect(effect=ValueEffectSet(value=0.0, type='minecraft:set'))],
    ),
)

SMITE = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.smite'),
    exclusive_set='#minecraft:exclusive_set/damage',
    supported_items='#minecraft:enchantable/weapon',
    primary_items='#minecraft:enchantable/melee_weapon',
    weight=5,
    max_level=5,
    min_cost=EnchantmentCost(base=5, per_level_above_first=8),
    max_cost=EnchantmentCost(base=25, per_level_above_first=8),
    anvil_cost=2,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        damage=[
            DamageEnchantmentEffect(
                requirements=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='#minecraft:sensitive_to_smite'),
                    type='minecraft:entity_properties',
                ),
                effect=ValueEffectAdd(
                    value=LevelBasedValueMapLinear(base=2.5, per_level_above_first=2.5, type='minecraft:linear'),
                    type='minecraft:add',
                ),
            ),
        ],
    ),
)

SOUL_SPEED = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.soul_speed'),
    supported_items='#minecraft:enchantable/foot_armor',
    weight=1,
    max_level=3,
    min_cost=EnchantmentCost(base=10, per_level_above_first=10),
    max_cost=EnchantmentCost(base=25, per_level_above_first=10),
    anvil_cost=8,
    slots=[EquipmentSlotGroup.FEET],
    effects=EnchantmentEffectComponentMap(
        location_changed=[
            LocationChangedEnchantmentEffect(
                requirements=LootConditionAllOf(
                    terms=[
                        LootConditionInverted(
                            term=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(vehicle=EntitySubPredicateMap()),
                                type='minecraft:entity_properties',
                            ),
                            type='minecraft:inverted',
                        ),
                        LootConditionAnyOf(
                            terms=[
                                LootConditionAllOf(
                                    terms=[
                                        LootConditionEnchantmentActiveCheck(
                                            active=True,
                                            type='minecraft:enchantment_active_check',
                                        ),
                                        LootConditionEntityProperties(
                                            entity=EntityTarget.THIS,
                                            predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_flying=False)),
                                            type='minecraft:entity_properties',
                                        ),
                                        LootConditionAnyOf(
                                            terms=[
                                                LootConditionEntityProperties(
                                                    entity=EntityTarget.THIS,
                                                    predicate=EntitySubPredicateMap(
                                                        movement_affected_by=LocationPredicate(
                                                            block=BlockPredicate(blocks='#minecraft:soul_speed_blocks'),
                                                        ),
                                                    ),
                                                    type='minecraft:entity_properties',
                                                ),
                                                LootConditionEntityProperties(
                                                    entity=EntityTarget.THIS,
                                                    predicate=EntitySubPredicateMap(
                                                        flags=EntityFlagsPredicate(is_on_ground=False),
                                                    ),
                                                    type='minecraft:entity_properties',
                                                ),
                                            ],
                                            type='minecraft:any_of',
                                        ),
                                    ],
                                    type='minecraft:all_of',
                                ),
                                LootConditionAllOf(
                                    terms=[
                                        LootConditionEnchantmentActiveCheck(
                                            active=False,
                                            type='minecraft:enchantment_active_check',
                                        ),
                                        LootConditionEntityProperties(
                                            entity=EntityTarget.THIS,
                                            predicate=EntitySubPredicateMap(
                                                flags=EntityFlagsPredicate(is_flying=False),
                                                movement_affected_by=LocationPredicate(
                                                    block=BlockPredicate(blocks='#minecraft:soul_speed_blocks'),
                                                ),
                                            ),
                                            type='minecraft:entity_properties',
                                        ),
                                    ],
                                    type='minecraft:all_of',
                                ),
                            ],
                            type='minecraft:any_of',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
                effect=LocationBasedEffectAllOf(
                    effects=[
                        LocationBasedEffectAttribute(
                            type='minecraft:attribute',
                            **dict[str, Any]({
                                'amount': {'type': 'minecraft:linear', 'base': 0.0405, 'per_level_above_first': 0.0105},
                                'attribute': 'minecraft:movement_speed',
                                'id': 'minecraft:enchantment.soul_speed',
                                'operation': 'add_value',
                            }),
                        ),
                        LocationBasedEffectAttribute(
                            type='minecraft:attribute',
                            **dict[str, Any]({
                                'amount': 1.0,
                                'attribute': 'minecraft:movement_efficiency',
                                'id': 'minecraft:enchantment.soul_speed',
                                'operation': 'add_value',
                            }),
                        ),
                    ],
                    type='minecraft:all_of',
                ),
            ),
            LocationChangedEnchantmentEffect(
                requirements=LootConditionAllOf(
                    terms=[
                        LootConditionRandomChance(
                            chance=ContextFloatProviderStructEnchantmentLevel(amount=0.04, type='minecraft:enchantment_level'),
                            type='minecraft:random_chance',
                        ),
                        LootConditionEntityProperties(
                            entity=EntityTarget.THIS,
                            predicate=EntitySubPredicateMap(
                                flags=EntityFlagsPredicate(is_on_ground=True),
                                movement_affected_by=LocationPredicate(block=BlockPredicate(blocks='#minecraft:soul_speed_blocks')),
                            ),
                            type='minecraft:entity_properties',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
                effect=LocationBasedEffectChangeItemDamage(amount=1.0, type='minecraft:change_item_damage'),
            ),
        ],
        tick=[
            TickEnchantmentEffect(
                requirements=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        flags=EntityFlagsPredicate(is_on_ground=True, is_flying=False),
                        movement=MovementPredicate(horizontal_speed=MinMaxBounds(min=9.999999747378752e-06)),
                        movement_affected_by=LocationPredicate(block=BlockPredicate(blocks='#minecraft:soul_speed_blocks')),
                        periodic_tick=5,
                    ),
                    type='minecraft:entity_properties',
                ),
                effect=EntityEffectSpawnParticles(
                    particle=ParticleDefault(type='minecraft:soul'),
                    horizontal_position=ParticlePosition(type='in_bounding_box'),
                    vertical_position=ParticlePosition(type='entity_position', offset=0.1),
                    horizontal_velocity=ParticleVelocity(movement_scale=-0.2),
                    vertical_velocity=ParticleVelocity(base=0.1),
                    speed=1.0,
                    type='minecraft:spawn_particles',
                ),
            ),
            TickEnchantmentEffect(
                requirements=LootConditionAllOf(
                    terms=[
                        LootConditionRandomChance(chance=0.35, type='minecraft:random_chance'),
                        LootConditionEntityProperties(
                            entity=EntityTarget.THIS,
                            predicate=EntitySubPredicateMap(
                                flags=EntityFlagsPredicate(is_on_ground=True, is_flying=False),
                                movement=MovementPredicate(horizontal_speed=MinMaxBounds(min=9.999999747378752e-06)),
                                movement_affected_by=LocationPredicate(block=BlockPredicate(blocks='#minecraft:soul_speed_blocks')),
                                periodic_tick=5,
                            ),
                            type='minecraft:entity_properties',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
                effect=EntityEffectPlaySound(
                    sound='minecraft:particle.soul_escape',
                    volume=0.6,
                    pitch=FloatProvider(
                        type='minecraft:uniform',
                        **dict[str, Any]({'max_exclusive': 1.0, 'min_inclusive': 0.6}),
                    ),
                    type='minecraft:play_sound',
                ),
            ),
        ],
    ),
)

SWEEPING_EDGE = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.sweeping_edge'),
    supported_items='#minecraft:enchantable/sweeping',
    weight=2,
    max_level=3,
    min_cost=EnchantmentCost(base=5, per_level_above_first=9),
    max_cost=EnchantmentCost(base=20, per_level_above_first=9),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        attributes=[
            AttributeEffect(
                attribute='minecraft:sweeping_damage_ratio',
                id='minecraft:enchantment.sweeping_edge',
                amount=LevelBasedValueMapFraction(
                    numerator=LevelBasedValueMapLinear(base=1.0, per_level_above_first=1.0, type='minecraft:linear'),
                    denominator=LevelBasedValueMapLinear(base=2.0, per_level_above_first=1.0, type='minecraft:linear'),
                    type='minecraft:fraction',
                ),
                operation=AttributeOperation.ADDVALUE,
            ),
        ],
    ),
)

SWIFT_SNEAK = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.swift_sneak'),
    supported_items='#minecraft:enchantable/leg_armor',
    weight=1,
    max_level=3,
    min_cost=EnchantmentCost(base=25, per_level_above_first=25),
    max_cost=EnchantmentCost(base=75, per_level_above_first=25),
    anvil_cost=8,
    slots=[EquipmentSlotGroup.LEGS],
    effects=EnchantmentEffectComponentMap(
        attributes=[
            AttributeEffect(
                attribute='minecraft:sneaking_speed',
                id='minecraft:enchantment.swift_sneak',
                amount=LevelBasedValueMapLinear(base=0.15, per_level_above_first=0.15, type='minecraft:linear'),
                operation=AttributeOperation.ADDVALUE,
            ),
        ],
    ),
)

THORNS = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.thorns'),
    supported_items='#minecraft:enchantable/armor',
    primary_items='#minecraft:enchantable/chest_armor',
    weight=1,
    max_level=3,
    min_cost=EnchantmentCost(base=10, per_level_above_first=20),
    max_cost=EnchantmentCost(base=60, per_level_above_first=20),
    anvil_cost=8,
    slots=[EquipmentSlotGroup.ANY],
    effects=EnchantmentEffectComponentMap(
        post_attack=[
            PostAttackEnchantmentEffect(
                requirements=LootConditionRandomChance(
                    chance=ContextFloatProviderStructEnchantmentLevel(
                        amount=LevelBasedValueMapLinear(base=0.15, per_level_above_first=0.15, type='minecraft:linear'),
                        type='minecraft:enchantment_level',
                    ),
                    type='minecraft:random_chance',
                ),
                effect=EntityEffectAllOf(
                    effects=[
                        EntityEffectDamageEntity(
                            damage_type='minecraft:thorns',
                            min_damage=1.0,
                            max_damage=5.0,
                            type='minecraft:damage_entity',
                        ),
                        EntityEffectChangeItemDamage(amount=2.0, type='minecraft:change_item_damage'),
                    ],
                    type='minecraft:all_of',
                ),
                enchanted=AttackTarget.VICTIM,
                affected=AttackTarget.ATTACKER,
            ),
        ],
    ),
)

UNBREAKING = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.unbreaking'),
    supported_items='#minecraft:enchantable/durability',
    weight=5,
    max_level=3,
    min_cost=EnchantmentCost(base=5, per_level_above_first=8),
    max_cost=EnchantmentCost(base=55, per_level_above_first=8),
    anvil_cost=2,
    slots=[EquipmentSlotGroup.ANY],
    effects=EnchantmentEffectComponentMap(
        item_damage=[
            ItemDamageEnchantmentEffect(
                requirements=LootConditionMatchTool(
                    predicate=ItemPredicate(items='#minecraft:enchantable/armor'),
                    type='minecraft:match_tool',
                ),
                effect=ValueEffectRemoveBinomial(
                    chance=LevelBasedValueMapFraction(
                        numerator=LevelBasedValueMapLinear(base=2.0, per_level_above_first=2.0, type='minecraft:linear'),
                        denominator=LevelBasedValueMapLinear(base=10.0, per_level_above_first=5.0, type='minecraft:linear'),
                        type='minecraft:fraction',
                    ),
                    type='minecraft:remove_binomial',
                ),
            ),
            ItemDamageEnchantmentEffect(
                requirements=LootConditionInverted(
                    term=LootConditionMatchTool(
                        predicate=ItemPredicate(items='#minecraft:enchantable/armor'),
                        type='minecraft:match_tool',
                    ),
                    type='minecraft:inverted',
                ),
                effect=ValueEffectRemoveBinomial(
                    chance=LevelBasedValueMapFraction(
                        numerator=LevelBasedValueMapLinear(base=1.0, per_level_above_first=1.0, type='minecraft:linear'),
                        denominator=LevelBasedValueMapLinear(base=2.0, per_level_above_first=1.0, type='minecraft:linear'),
                        type='minecraft:fraction',
                    ),
                    type='minecraft:remove_binomial',
                ),
            ),
        ],
    ),
)

VANISHING_CURSE = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.vanishing_curse'),
    supported_items='#minecraft:enchantable/vanishing',
    weight=1,
    max_level=1,
    min_cost=EnchantmentCost(base=25, per_level_above_first=0),
    max_cost=EnchantmentCost(base=50, per_level_above_first=0),
    anvil_cost=8,
    slots=[EquipmentSlotGroup.ANY],
    effects=EnchantmentEffectComponentMap(prevent_equipment_drop=PreventEquipmentDropStruct()),
)

WIND_BURST = Enchantment(
    description=TextObjectStruct2(translate='enchantment.minecraft.wind_burst'),
    supported_items='#minecraft:enchantable/mace',
    weight=2,
    max_level=3,
    min_cost=EnchantmentCost(base=15, per_level_above_first=9),
    max_cost=EnchantmentCost(base=65, per_level_above_first=9),
    anvil_cost=4,
    slots=[EquipmentSlotGroup.MAINHAND],
    effects=EnchantmentEffectComponentMap(
        post_attack=[
            PostAttackEnchantmentEffect(
                requirements=LootConditionEntityProperties(
                    entity=EntityTarget.DIRECTATTACKER,
                    predicate=EntitySubPredicateMap(
                        flags=EntityFlagsPredicate(is_flying=False),
                        movement=MovementPredicate(fall_distance=MinMaxBounds(min=1.5)),
                    ),
                    type='minecraft:entity_properties',
                ),
                effect=EntityEffectExplode(
                    immune_blocks='#minecraft:blocks_wind_charge_explosions',
                    knockback_multiplier=LevelBasedValueMapLookup(
                        values=[1.2, 1.75, 2.2],
                        fallback=LevelBasedValueMapLinear(base=1.5, per_level_above_first=0.35, type='minecraft:linear'),
                        type='minecraft:lookup',
                    ),
                    radius=3.5,
                    block_interaction=BlockInteraction.TRIGGER,
                    sound='minecraft:entity.wind_charge.wind_burst',
                    small_particle=ParticleDefault(type='minecraft:gust_emitter_small'),
                    large_particle=ParticleDefault(type='minecraft:gust_emitter_large'),
                    type='minecraft:explode',
                ),
                enchanted=AttackTarget.ATTACKER,
                affected=AttackTarget.ATTACKER,
            ),
        ],
    ),
)
