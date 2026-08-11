"""Lazy top-level exports for generated data and asset symbols."""

from importlib import import_module
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.ARGBColorAttribute import ARGBColorAttribute
    from generated_symbols.data.worldgen.feature.tree.AboveRootPlacement import AboveRootPlacement
    from generated_symbols.assets.item_definition.ActuallyTranslucentRGB import ActuallyTranslucentRGB
    from generated_symbols.data.enchantment.effect.AddEffectValue import AddEffectValue
    from generated_symbols.data.advancement.Advancement import Advancement
    from generated_symbols.data.advancement.AdvancementCriteriaMap import AdvancementCriteriaMap
    from generated_symbols.data.advancement.AdvancementCriterion import AdvancementCriterion
    from generated_symbols.data.advancement.AdvancementDisplay import AdvancementDisplay
    from generated_symbols.data.advancement.AdvancementFrame import AdvancementFrame
    from generated_symbols.data.advancement.AdvancementIcon import AdvancementIcon
    from generated_symbols.data.advancement.trigger.AdvancementPredicateRef import AdvancementPredicateRef
    from generated_symbols.data.advancement.AdvancementRewards import AdvancementRewards
    from generated_symbols.data.dialog.AfterAction import AfterAction
    from generated_symbols.data.loot.condition.AllOf import AllOf
    from generated_symbols.data.enchantment.effect.AllOfEffectValue import AllOfEffectValue
    from generated_symbols.data.enchantment.effect.AllOfEntityEffect import AllOfEntityEffect
    from generated_symbols.data.enchantment.effect.AllOfLocationBasedEffect import AllOfLocationBasedEffect
    from generated_symbols.data.gametest.test_environment.AllOffTestEnvironment import AllOffTestEnvironment
    from generated_symbols.data.advancement.trigger.AllayDropItemOnBlock import AllayDropItemOnBlock
    from generated_symbols.data.worldgen.feature.tree.AlterGroundTreeDecorator import AlterGroundTreeDecorator
    from generated_symbols.data.loot.condition.Alternative import Alternative
    from generated_symbols.data.worldgen.attribute.AmbientParticle import AmbientParticle
    from generated_symbols.data.worldgen.attribute.AmbientSounds import AmbientSounds
    from generated_symbols.data.enchantment.effect_component.AmmoUseEnchantmentEffect import AmmoUseEnchantmentEffect
    from generated_symbols.data.advancement.trigger.AnyBlockUse import AnyBlockUse
    from generated_symbols.data.loot.condition.AnyOf import AnyOf
    from generated_symbols.data.worldgen.processor_list.AppendLoot import AppendLoot
    from generated_symbols.data.worldgen.processor_list.AppendStatic import AppendStatic
    from generated_symbols.data.loot.function.ApplyBonus import ApplyBonus
    from generated_symbols.data.loot.function.ApplyBonusFormula import ApplyBonusFormula
    from generated_symbols.data.enchantment.effect.ApplyExhaustionEntityEffect import ApplyExhaustionEntityEffect
    from generated_symbols.data.enchantment.effect.ApplyImpulseEntityEffect import ApplyImpulseEntityEffect
    from generated_symbols.data.enchantment.effect.ApplyMobEffectEntityEffect import ApplyMobEffectEntityEffect
    from generated_symbols.data.worldgen.noise_settings.Aquifer import Aquifer
    from generated_symbols.data.enchantment.effect_component.ArmorEffectivenessEnchantmentEffect import ArmorEffectivenessEnchantmentEffect
    from generated_symbols.data.trim.ArmorMaterial import ArmorMaterial
    from generated_symbols.assets.atlas.Atlas import Atlas
    from generated_symbols.data.worldgen.feature.tree.AttachedToLeavesTreeDecorator import AttachedToLeavesTreeDecorator
    from generated_symbols.data.worldgen.feature.tree.AttachedToLogsTreeDecorator import AttachedToLogsTreeDecorator
    from generated_symbols.data.enchantment.effect_component.AttackTarget import AttackTarget
    from generated_symbols.data.enchantment.effect.AttributeEffect import AttributeEffect
    from generated_symbols.data.sulfur_cube_archetype.AttributeEntry import AttributeEntry
    from generated_symbols.data.loot.function.AttributeModifier import AttributeModifier
    from generated_symbols.data.timeline.AttributeTrackBase import AttributeTrackBase
    from generated_symbols.assets.shader.post.AuxTarget import AuxTarget
    from generated_symbols.data.worldgen.processor_list.AxisAlignedLinearPos import AxisAlignedLinearPos
    from generated_symbols.data.advancement.predicate.AxolotlPredicate import AxolotlPredicate
    from generated_symbols.data.worldgen.attribute.BackgroundMusic import BackgroundMusic
    from generated_symbols.assets.item_definition.Banner import Banner
    from generated_symbols.assets.item_definition.BannerAttachment import BannerAttachment
    from generated_symbols.data.loot.function.BannerPatternLayer import BannerPatternLayer
    from generated_symbols.data.worldgen.feature.block_state_provider.BaseNoiseProvider import BaseNoiseProvider
    from generated_symbols.assets.item_definition.Bed import Bed
    from generated_symbols.assets.item_definition.BedPart import BedPart
    from generated_symbols.data.worldgen.attribute.BedRule import BedRule
    from generated_symbols.data.worldgen.attribute.BedRuleType import BedRuleType
    from generated_symbols.data.advancement.trigger.BeeNestDestroyed import BeeNestDestroyed
    from generated_symbols.data.worldgen.feature.tree.BeehiveTreeDecorator import BeehiveTreeDecorator
    from generated_symbols.data.worldgen.feature.tree.BendingTrunkPlacer import BendingTrunkPlacer
    from generated_symbols.data.util.BinomialIntGenerator import BinomialIntGenerator
    from generated_symbols.data.number_provider.BinomialNumberProvider import BinomialNumberProvider
    from generated_symbols.data.loot.function.BinomialWithBonusCountFormula import BinomialWithBonusCountFormula
    from generated_symbols.data.worldgen.biome.Biome import Biome
    from generated_symbols.data.worldgen.biome.BiomeCategory import BiomeCategory
    from generated_symbols.data.variants.BiomeCheck import BiomeCheck
    from generated_symbols.data.worldgen.material_condition.BiomeCondition import BiomeCondition
    from generated_symbols.data.worldgen.biome.BiomeEffects import BiomeEffects
    from generated_symbols.data.worldgen.biome.BiomeMusic import BiomeMusic
    from generated_symbols.data.worldgen.dimension.biome_source.BiomeNoiseEntry import BiomeNoiseEntry
    from generated_symbols.data.worldgen.biome.BiomeParticle import BiomeParticle
    from generated_symbols.data.worldgen.biome.BiomeSoundAdditions import BiomeSoundAdditions
    from generated_symbols.data.worldgen.dimension.biome_source.BiomeSource import BiomeSource
    from generated_symbols.data.worldgen.structure.BiomeTemperature import BiomeTemperature
    from generated_symbols.assets.font.BitmapProvider import BitmapProvider
    from generated_symbols.assets.shader.program.BlendFactor import BlendFactor
    from generated_symbols.assets.shader.program.BlendFunc import BlendFunc
    from generated_symbols.assets.shader.program.BlendMode import BlendMode
    from generated_symbols.data.worldgen.attribute.modifier.BlendToGray import BlendToGray
    from generated_symbols.data.worldgen.processor_list.BlockAge import BlockAge
    from generated_symbols.data.gametest.BlockBasedTestInstance import BlockBasedTestInstance
    from generated_symbols.data.worldgen.feature.BlockBlobConfig import BlockBlobConfig
    from generated_symbols.data.worldgen.feature.BlockColumnConfig import BlockColumnConfig
    from generated_symbols.data.worldgen.feature.BlockColumnLayer import BlockColumnLayer
    from generated_symbols.data.worldgen.processor_list.BlockEntityModifier import BlockEntityModifier
    from generated_symbols.data.loot.BlockEntityTarget import BlockEntityTarget
    from generated_symbols.data.enchantment.effect_component.BlockExperienceEnchantmentEffect import BlockExperienceEnchantmentEffect
    from generated_symbols.data.worldgen.processor_list.BlockIgnore import BlockIgnore
    from generated_symbols.data.enchantment.effect.BlockInteraction import BlockInteraction
    from generated_symbols.data.worldgen.processor_list.BlockMatch import BlockMatch
    from generated_symbols.data.structure.BlockPalette import BlockPalette
    from generated_symbols.data.worldgen.feature.BlockPileConfig import BlockPileConfig
    from generated_symbols.data.worldgen.feature.BlockPlacer import BlockPlacer
    from generated_symbols.data.worldgen.feature.placement.BlockPredicateFilter import BlockPredicateFilter
    from generated_symbols.data.advancement.predicate.BlockPredicateState import BlockPredicateState
    from generated_symbols.data.worldgen.processor_list.BlockRot import BlockRot
    from generated_symbols.data.worldgen.material_rule.BlockRule import BlockRule
    from generated_symbols.assets.item_definition.BlockState import BlockState
    from generated_symbols.assets.block_state_definition.BlockStateDefinition import BlockStateDefinition
    from generated_symbols.assets.block_state_definition.BlockStateDefinitionMultipart import BlockStateDefinitionMultipart
    from generated_symbols.assets.block_state_definition.BlockStateDefinitionMultipartEntry import BlockStateDefinitionMultipartEntry
    from generated_symbols.assets.block_state_definition.BlockStateDefinitionVariant import BlockStateDefinitionVariant
    from generated_symbols.assets.block_state_definition.BlockStateDefinitionVariantMap import BlockStateDefinitionVariantMap
    from generated_symbols.data.worldgen.processor_list.BlockStateMatch import BlockStateMatch
    from generated_symbols.data.loot.condition.BlockStateProperty import BlockStateProperty
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider
    from generated_symbols.data.worldgen.feature.BlockStateRuleProviderEntry import BlockStateRuleProviderEntry
    from generated_symbols.data.advancement.predicate.BoatPredicate import BoatPredicate
    from generated_symbols.assets.item_definition.Book import Book
    from generated_symbols.data.gametest.test_environment.BoolGameRule import BoolGameRule
    from generated_symbols.data.worldgen.attribute.BooleanAttribute import BooleanAttribute
    from generated_symbols.data.worldgen.attribute.modifier.BooleanAttributeModifier import BooleanAttributeModifier
    from generated_symbols.data.dialog.input.BooleanInput import BooleanInput
    from generated_symbols.data.worldgen.attribute.modifier.BooleanModifierType import BooleanModifierType
    from generated_symbols.data.worldgen.BottomBiasHeightProvider import BottomBiasHeightProvider
    from generated_symbols.data.worldgen.structure.BoundingBox import BoundingBox
    from generated_symbols.data.advancement.trigger.BredAnimals import BredAnimals
    from generated_symbols.data.advancement.trigger.BrewedPotion import BrewedPotion
    from generated_symbols.data.recipe.Brewing import Brewing
    from generated_symbols.data.worldgen.structure.BuriedTreasure import BuriedTreasure
    from generated_symbols.data.dialog.Button import Button
    from generated_symbols.data.dialog.ButtonListDialogBase import ButtonListDialogBase
    from generated_symbols.data.enchantment.provider.ByCostEnchantmentProvider import ByCostEnchantmentProvider
    from generated_symbols.data.enchantment.provider.ByCostWithDifficultyEnchantmentProvider import ByCostWithDifficultyEnchantmentProvider
    from generated_symbols.data.worldgen.carver.CanyonConfig import CanyonConfig
    from generated_symbols.data.worldgen.carver.CanyonShape import CanyonShape
    from generated_symbols.data.worldgen.processor_list.Capped import Capped
    from generated_symbols.data.worldgen.dimension.CardinalLightType import CardinalLightType
    from generated_symbols.data.worldgen.CarveStep import CarveStep
    from generated_symbols.data.worldgen.carver.CarverConfigBase import CarverConfigBase
    from generated_symbols.data.worldgen.carver.CarverDebugSettings import CarverDebugSettings
    from generated_symbols.data.worldgen.carver.CarverListRef import CarverListRef
    from generated_symbols.data.worldgen.carver.CarverRef import CarverRef
    from generated_symbols.data.worldgen.biome.CarversPerStep import CarversPerStep
    from generated_symbols.data.worldgen.feature.decorator.CarvingMaskConfig import CarvingMaskConfig
    from generated_symbols.data.worldgen.feature.placement.CarvingMaskModifier import CarvingMaskModifier
    from generated_symbols.data.advancement.predicate.CatPredicate import CatPredicate
    from generated_symbols.data.variants.cat.CatSounds import CatSounds
    from generated_symbols.data.variants.cat.CatVariant import CatVariant
    from generated_symbols.data.worldgen.carver.CaveConfig import CaveConfig
    from generated_symbols.data.worldgen.feature.decorator.ChanceConfig import ChanceConfig
    from generated_symbols.data.enchantment.effect.ChangeItemDamageEffect import ChangeItemDamageEffect
    from generated_symbols.data.advancement.trigger.ChangedDimension import ChangedDimension
    from generated_symbols.data.advancement.trigger.ChanneledLightning import ChanneledLightning
    from generated_symbols.assets.item_definition.ChargeType import ChargeType
    from generated_symbols.data.chat_type.ChatDecoration import ChatDecoration
    from generated_symbols.data.chat_type.ChatDecorationParameter import ChatDecorationParameter
    from generated_symbols.data.chat_type.ChatType import ChatType
    from generated_symbols.data.worldgen.dimension.biome_source.Checkerboard import Checkerboard
    from generated_symbols.data.worldgen.feature.tree.CherryFoliagePlacer import CherryFoliagePlacer
    from generated_symbols.data.worldgen.feature.tree.CherryTrunkPlacer import CherryTrunkPlacer
    from generated_symbols.assets.item_definition.Chest import Chest
    from generated_symbols.assets.item_definition.ChestType import ChestType
    from generated_symbols.data.variants.chicken.ChickenModelType import ChickenModelType
    from generated_symbols.data.variants.chicken.ChickenSounds import ChickenSounds
    from generated_symbols.data.variants.chicken.ChickenVariant import ChickenVariant
    from generated_symbols.data.worldgen.dimension.chunk_generator.ChunkGenerator import ChunkGenerator
    from generated_symbols.data.worldgen.density_function.Clamp import Clamp
    from generated_symbols.data.worldgen.ClampedIntProvider import ClampedIntProvider
    from generated_symbols.data.enchantment.level_based_value.ClampedLevelValue import ClampedLevelValue
    from generated_symbols.data.worldgen.ClampedNormalIntProvider import ClampedNormalIntProvider
    from generated_symbols.data.dialog.action.ClickAction import ClickAction
    from generated_symbols.data.worldgen.dimension.biome_source.ClimateParameter import ClimateParameter
    from generated_symbols.data.worldgen.dimension.biome_source.ClimateParameters import ClimateParameters
    from generated_symbols.data.gametest.test_environment.ClockTimeTestEnvironment import ClockTimeTestEnvironment
    from generated_symbols.data.worldgen.feature.tree.CocoaTreeDecorator import CocoaTreeDecorator
    from generated_symbols.assets.regional_compliancies.Code import Code
    from generated_symbols.data.worldgen.attribute.modifier.ColorAttributeModifier import ColorAttributeModifier
    from generated_symbols.data.worldgen.attribute.modifier.ColorModifierType import ColorModifierType
    from generated_symbols.assets.texture_meta.ColormapTextureMeta import ColormapTextureMeta
    from generated_symbols.data.worldgen.feature.ColumnPlacer import ColumnPlacer
    from generated_symbols.data.worldgen.feature.ColumnsConfig import ColumnsConfig
    from generated_symbols.data.worldgen.feature.block_predicate.CombiningPredicate import CombiningPredicate
    from generated_symbols.assets.item_definition.Compass import Compass
    from generated_symbols.assets.item_definition.CompassTarget import CompassTarget
    from generated_symbols.assets.item_definition.ComponentFlags import ComponentFlags
    from generated_symbols.assets.item_definition.ComponentStrings import ComponentStrings
    from generated_symbols.assets.item_definition.Composite import Composite
    from generated_symbols.data.advancement.trigger.CompositeEntity import CompositeEntity
    from generated_symbols.data.worldgen.processor_list.CompositeMatch import CompositeMatch
    from generated_symbols.data.loot.CompositePoolEntry import CompositePoolEntry
    from generated_symbols.data.worldgen.structure_set.ConcentricRingsPlacement import ConcentricRingsPlacement
    from generated_symbols.assets.item_definition.Condition import Condition
    from generated_symbols.data.worldgen.material_rule.ConditionRule import ConditionRule
    from generated_symbols.data.number_provider.ConditionalNumberProvider import ConditionalNumberProvider
    from generated_symbols.assets.item_definition.ConditionalPropertyType import ConditionalPropertyType
    from generated_symbols.data.worldgen.surface_builder.Config import Config
    from generated_symbols.data.worldgen.carver.ConfiguredCarver import ConfiguredCarver
    from generated_symbols.data.worldgen.feature.decorator.ConfiguredDecorator import ConfiguredDecorator
    from generated_symbols.data.worldgen.feature.ConfiguredFeature import ConfiguredFeature
    from generated_symbols.data.worldgen.feature.ConfiguredFeatureRef import ConfiguredFeatureRef
    from generated_symbols.data.worldgen.surface_builder.ConfiguredSurfaceBuilder import ConfiguredSurfaceBuilder
    from generated_symbols.data.worldgen.surface_builder.ConfiguredSurfaceBuilderRef import ConfiguredSurfaceBuilderRef
    from generated_symbols.data.dialog.ConfirmationDialog import ConfirmationDialog
    from generated_symbols.data.worldgen.density_function.Constant import Constant
    from generated_symbols.data.worldgen.ConstantHeightProvider import ConstantHeightProvider
    from generated_symbols.data.util.ConstantIntGenerator import ConstantIntGenerator
    from generated_symbols.data.worldgen.ConstantIntProvider import ConstantIntProvider
    from generated_symbols.data.number_provider.ConstantNumberProvider import ConstantNumberProvider
    from generated_symbols.assets.item_definition.ConstantTint import ConstantTint
    from generated_symbols.data.advancement.trigger.ConstructBeacon import ConstructBeacon
    from generated_symbols.data.advancement.trigger.ConsumeItem import ConsumeItem
    from generated_symbols.data.sulfur_cube_archetype.ContactDamage import ContactDamage
    from generated_symbols.data.loot.function.ContainerComponents import ContainerComponents
    from generated_symbols.data.slot_source.ContentsSlotSource import ContentsSlotSource
    from generated_symbols.assets.item_definition.ContextDimension import ContextDimension
    from generated_symbols.assets.item_definition.ContextEntityType import ContextEntityType
    from generated_symbols.data.util.ContextNbtProvider import ContextNbtProvider
    from generated_symbols.data.util.ContextScoreProvider import ContextScoreProvider
    from generated_symbols.data.recipe.CookingBookCategory import CookingBookCategory
    from generated_symbols.data.recipe.CookingBookInfo import CookingBookInfo
    from generated_symbols.assets.item_definition.CopperGolemStatue import CopperGolemStatue
    from generated_symbols.assets.item_definition.CopperGolemStatuePose import CopperGolemStatuePose
    from generated_symbols.data.loot.function.CopyComponents import CopyComponents
    from generated_symbols.data.loot.function.CopyName import CopyName
    from generated_symbols.data.loot.function.CopyNameSource import CopyNameSource
    from generated_symbols.data.loot.function.CopyNbt import CopyNbt
    from generated_symbols.data.loot.function.CopyNbtOperation import CopyNbtOperation
    from generated_symbols.data.loot.function.CopyNbtStrategy import CopyNbtStrategy
    from generated_symbols.data.worldgen.feature.block_state_provider.CopyPropertiesProvider import CopyPropertiesProvider
    from generated_symbols.data.loot.function.CopyState import CopyState
    from generated_symbols.data.worldgen.feature.CoralConfig import CoralConfig
    from generated_symbols.assets.item_definition.Count import Count
    from generated_symbols.data.worldgen.feature.decorator.CountConfig import CountConfig
    from generated_symbols.data.worldgen.feature.decorator.CountExtraConfig import CountExtraConfig
    from generated_symbols.data.worldgen.feature.placement.CountModifier import CountModifier
    from generated_symbols.data.worldgen.feature.decorator.CountNoiseBiasedConfig import CountNoiseBiasedConfig
    from generated_symbols.data.worldgen.feature.decorator.CountNoiseConfig import CountNoiseConfig
    from generated_symbols.data.worldgen.feature.placement.CountOnEveryLayerModifier import CountOnEveryLayerModifier
    from generated_symbols.data.variants.cow.CowModelType import CowModelType
    from generated_symbols.data.variants.cow.CowSounds import CowSounds
    from generated_symbols.data.variants.cow.CowVariant import CowVariant
    from generated_symbols.data.recipe.CraftingBookCategory import CraftingBookCategory
    from generated_symbols.data.recipe.CraftingBookInfo import CraftingBookInfo
    from generated_symbols.data.recipe.CraftingDecoratedPot import CraftingDecoratedPot
    from generated_symbols.data.recipe.CraftingDye import CraftingDye
    from generated_symbols.data.recipe.CraftingImbue import CraftingImbue
    from generated_symbols.data.recipe.CraftingIngredients import CraftingIngredients
    from generated_symbols.data.recipe.CraftingShaped import CraftingShaped
    from generated_symbols.data.recipe.CraftingShapeless import CraftingShapeless
    from generated_symbols.data.recipe.CraftingSpecialBannerDuplicate import CraftingSpecialBannerDuplicate
    from generated_symbols.data.recipe.CraftingSpecialBookCloning import CraftingSpecialBookCloning
    from generated_symbols.data.recipe.CraftingSpecialFireworkRocket import CraftingSpecialFireworkRocket
    from generated_symbols.data.recipe.CraftingSpecialFireworkStar import CraftingSpecialFireworkStar
    from generated_symbols.data.recipe.CraftingSpecialFireworkStarFade import CraftingSpecialFireworkStarFade
    from generated_symbols.data.recipe.CraftingSpecialMapExtending import CraftingSpecialMapExtending
    from generated_symbols.data.recipe.CraftingSpecialShieldDecoration import CraftingSpecialShieldDecoration
    from generated_symbols.data.recipe.CraftingTransmute import CraftingTransmute
    from generated_symbols.data.worldgen.feature.tree.CreakingHeartTreeDecorator import CreakingHeartTreeDecorator
    from generated_symbols.assets.credits.Credits import Credits
    from generated_symbols.assets.credits.CreditsCompanySegment import CreditsCompanySegment
    from generated_symbols.assets.credits.CreditsDiscipline import CreditsDiscipline
    from generated_symbols.assets.credits.CreditsJobTitle import CreditsJobTitle
    from generated_symbols.data.enchantment.effect_component.CrossbowChargeSoundsEnchantmentEffect import CrossbowChargeSoundsEnchantmentEffect
    from generated_symbols.assets.item_definition.CrossbowChargeType import CrossbowChargeType
    from generated_symbols.data.timeline.CubicBezierEase import CubicBezierEase
    from generated_symbols.data.worldgen.density_function.CubicSpline import CubicSpline
    from generated_symbols.data.worldgen.feature.placement.CuboidModifier import CuboidModifier
    from generated_symbols.data.advancement.trigger.CuredZombieVillager import CuredZombieVillager
    from generated_symbols.data.loot.function.CustomModelDataColors import CustomModelDataColors
    from generated_symbols.assets.item_definition.CustomModelDataTint import CustomModelDataTint
    from generated_symbols.assets.model.CustomizableItemDisplayContext import CustomizableItemDisplayContext
    from generated_symbols.assets.item_definition.Damage import Damage
    from generated_symbols.data.damage_type.DamageEffects import DamageEffects
    from generated_symbols.data.enchantment.effect_component.DamageEnchantmentEffect import DamageEnchantmentEffect
    from generated_symbols.data.enchantment.effect.DamageEntityEffect import DamageEntityEffect
    from generated_symbols.data.enchantment.effect_component.DamageImmunityEnchantmentEffect import DamageImmunityEnchantmentEffect
    from generated_symbols.data.enchantment.effect.DamageItemEffect import DamageItemEffect
    from generated_symbols.data.advancement.predicate.DamagePredicate import DamagePredicate
    from generated_symbols.data.enchantment.effect_component.DamageProtectionEnchantmentEffect import DamageProtectionEnchantmentEffect
    from generated_symbols.data.damage_type.DamageScaling import DamageScaling
    from generated_symbols.data.advancement.predicate.DamageSourceFlags import DamageSourceFlags
    from generated_symbols.data.advancement.predicate.DamageSourcePredicate import DamageSourcePredicate
    from generated_symbols.data.loot.condition.DamageSourceProperties import DamageSourceProperties
    from generated_symbols.data.advancement.predicate.DamageTagPredicate import DamageTagPredicate
    from generated_symbols.data.damage_type.DamageType import DamageType
    from generated_symbols.data.damage_type.DeathMessageType import DeathMessageType
    from generated_symbols.data.decorated_pot_pattern.DecoratedPotPattern import DecoratedPotPattern
    from generated_symbols.data.worldgen.DecorationStep import DecorationStep
    from generated_symbols.data.advancement.trigger.DefaultBlockUse import DefaultBlockUse
    from generated_symbols.assets.shader.program.Defines import Defines
    from generated_symbols.assets.shader.program.DefinesValues import DefinesValues
    from generated_symbols.data.worldgen.feature.DeltaConfig import DeltaConfig
    from generated_symbols.data.worldgen.density_function.DensityFunction import DensityFunction
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from generated_symbols.data.worldgen.feature.decorator.DepthAverageConfig import DepthAverageConfig
    from generated_symbols.data.dialog.Dialog import Dialog
    from generated_symbols.data.dialog.DialogBase import DialogBase
    from generated_symbols.data.dialog.body.DialogBody import DialogBody
    from generated_symbols.data.dialog.DialogListRef import DialogListRef
    from generated_symbols.data.gametest.test_environment.Difficulty import Difficulty
    from generated_symbols.data.gametest.test_environment.DifficultyTestEnvironment import DifficultyTestEnvironment
    from generated_symbols.data.worldgen.dimension.Dimension import Dimension
    from generated_symbols.data.worldgen.structure.DimensionPaddingConfig import DimensionPaddingConfig
    from generated_symbols.data.worldgen.dimension.DimensionType import DimensionType
    from generated_symbols.data.worldgen.dimension.DimensionTypeEffects import DimensionTypeEffects
    from generated_symbols.data.worldgen.dimension.DimensionTypeRef import DimensionTypeRef
    from generated_symbols.data.worldgen.dimension.biome_source.DirectMultiNoise import DirectMultiNoise
    from generated_symbols.data.worldgen.structure.DirectPoolAlias import DirectPoolAlias
    from generated_symbols.assets.atlas.Directory import Directory
    from generated_symbols.data.worldgen.attribute.DiscreteAttribute import DiscreteAttribute
    from generated_symbols.data.worldgen.feature.DiskConfig import DiskConfig
    from generated_symbols.assets.item_definition.DisplayContext import DisplayContext
    from generated_symbols.data.worldgen.density_function.DistanceMetric import DistanceMetric
    from generated_symbols.data.advancement.predicate.DistancePredicate import DistancePredicate
    from generated_symbols.data.worldgen.density_function.DistanceToPoint import DistanceToPoint
    from generated_symbols.data.worldgen.feature.block_state_provider.DualNoiseProvider import DualNoiseProvider
    from generated_symbols.assets.item_definition.DyeTint import DyeTint
    from generated_symbols.assets.equipment.Dyeable import Dyeable
    from generated_symbols.data.dialog.action.DynamicCustomAction import DynamicCustomAction
    from generated_symbols.data.loot.DynamicDrops import DynamicDrops
    from generated_symbols.data.loot.DynamicPoolEntry import DynamicPoolEntry
    from generated_symbols.data.dialog.action.DynamicRunCommand import DynamicRunCommand
    from generated_symbols.data.timeline.EasingType import EasingType
    from generated_symbols.data.advancement.trigger.EffectsChanged import EffectsChanged
    from generated_symbols.data.worldgen.template_pool.Element import Element
    from generated_symbols.data.worldgen.template_pool.ElementBase import ElementBase
    from generated_symbols.data.worldgen.feature.EmeraldOreConfig import EmeraldOreConfig
    from generated_symbols.data.loot.function.EnchantRandomly import EnchantRandomly
    from generated_symbols.data.loot.function.EnchantWithLevels import EnchantWithLevels
    from generated_symbols.data.loot.function.EnchantedCountBase import EnchantedCountBase
    from generated_symbols.data.loot.function.EnchantedCountIncrease import EnchantedCountIncrease
    from generated_symbols.data.advancement.trigger.EnchantedItem import EnchantedItem
    from generated_symbols.data.enchantment.Enchantment import Enchantment
    from generated_symbols.data.loot.condition.EnchantmentActiveCheck import EnchantmentActiveCheck
    from generated_symbols.data.enchantment.EnchantmentCost import EnchantmentCost
    from generated_symbols.data.enchantment.effect_component.EnchantmentEffectComponentMap import EnchantmentEffectComponentMap
    from generated_symbols.data.number_provider.EnchantmentLevelProvider import EnchantmentLevelProvider
    from generated_symbols.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
    from generated_symbols.data.enchantment.provider.EnchantmentProvider import EnchantmentProvider
    from generated_symbols.data.enchantment.provider.EnchantmentsType import EnchantmentsType
    from generated_symbols.assets.item_definition.EndCube import EndCube
    from generated_symbols.assets.item_definition.EndCubeEffectType import EndCubeEffectType
    from generated_symbols.data.worldgen.feature.EndGatewayConfig import EndGatewayConfig
    from generated_symbols.data.worldgen.feature.EndPodiumConfig import EndPodiumConfig
    from generated_symbols.data.worldgen.feature.EndSpike import EndSpike
    from generated_symbols.data.worldgen.feature.EndSpikeConfig import EndSpikeConfig
    from generated_symbols.data.advancement.trigger.EnterBlock import EnterBlock
    from generated_symbols.data.enchantment.effect.EntityEffect import EntityEffect
    from generated_symbols.data.advancement.predicate.EntityEffectsPredicate import EntityEffectsPredicate
    from generated_symbols.data.advancement.predicate.EntityEquipmentPredicate import EntityEquipmentPredicate
    from generated_symbols.data.advancement.predicate.EntityFlagsPredicate import EntityFlagsPredicate
    from generated_symbols.data.advancement.trigger.EntityHurtPlayer import EntityHurtPlayer
    from generated_symbols.data.advancement.trigger.EntityKilledPlayer import EntityKilledPlayer
    from generated_symbols.data.advancement.predicate.EntityPredicate import EntityPredicate
    from generated_symbols.data.loot.condition.EntityProperties import EntityProperties
    from generated_symbols.data.loot.condition.EntityScores import EntityScores
    from generated_symbols.data.advancement.predicate.EntitySlotsPredicate import EntitySlotsPredicate
    from generated_symbols.data.advancement.predicate.EntitySubPredicate import EntitySubPredicate
    from generated_symbols.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
    from generated_symbols.data.advancement.predicate.EntityTagPredicate import EntityTagPredicate
    from generated_symbols.data.loot.EntityTarget import EntityTarget
    from generated_symbols.data.advancement.predicate.EntityTypePredicate import EntityTypePredicate
    from generated_symbols.data.loot.condition.EnvironmentAttributeCheck import EnvironmentAttributeCheck
    from generated_symbols.data.worldgen.attribute.EnvironmentAttributeMap import EnvironmentAttributeMap
    from generated_symbols.data.number_provider.EnvironmentAttributeNumberProvider import EnvironmentAttributeNumberProvider
    from generated_symbols.data.timeline.EnvironmentAttributeTrackMap import EnvironmentAttributeTrackMap
    from generated_symbols.data.worldgen.feature.placement.EnvironmentScanModifier import EnvironmentScanModifier
    from generated_symbols.assets.equipment.Equipment import Equipment
    from generated_symbols.data.enchantment.effect_component.EquipmentDropsEnchantmentEffect import EquipmentDropsEnchantmentEffect
    from generated_symbols.data.worldgen.structure_set.ExclusionZone import ExclusionZone
    from generated_symbols.data.tag.ExplicitTagEntry import ExplicitTagEntry
    from generated_symbols.data.enchantment.effect.ExplodeEntityEffect import ExplodeEntityEffect
    from generated_symbols.data.loot.function.ExplorationMap import ExplorationMap
    from generated_symbols.data.sulfur_cube_archetype.ExplosionData import ExplosionData
    from generated_symbols.data.enchantment.effect.ExplosionParticleInfo import ExplosionParticleInfo
    from generated_symbols.data.enchantment.level_based_value.ExponentLevelValue import ExponentLevelValue
    from generated_symbols.data.enchantment.effect.ExponentialEffectValue import ExponentialEffectValue
    from generated_symbols.data.advancement.trigger.FallAfterExplosion import FallAfterExplosion
    from generated_symbols.data.advancement.trigger.FallFromHeight import FallFromHeight
    from generated_symbols.data.worldgen.feature.tree.FallenTreeConfig import FallenTreeConfig
    from generated_symbols.data.worldgen.template_pool.FeatureElement import FeatureElement
    from generated_symbols.data.worldgen.feature.FeatureRef import FeatureRef
    from generated_symbols.data.worldgen.feature.tree.FeatureSize import FeatureSize
    from generated_symbols.data.worldgen.feature.FillLayerConfig import FillLayerConfig
    from generated_symbols.data.loot.function.FillPlayerHead import FillPlayerHead
    from generated_symbols.data.advancement.trigger.FilledBucket import FilledBucket
    from generated_symbols.assets.atlas.Filter import Filter
    from generated_symbols.assets.atlas.FilterPattern import FilterPattern
    from generated_symbols.data.slot_source.FilterSlotSource import FilterSlotSource
    from generated_symbols.data.loot.function.Filtered import Filtered
    from generated_symbols.data.worldgen.density_function.FindTopSurface import FindTopSurface
    from generated_symbols.data.loot.function.FireworkExplosions import FireworkExplosions
    from generated_symbols.data.recipe.FireworkShapeIngredients import FireworkShapeIngredients
    from generated_symbols.assets.item_definition.FireworkTint import FireworkTint
    from generated_symbols.data.advancement.predicate.FishingHookPredicate import FishingHookPredicate
    from generated_symbols.data.enchantment.effect_component.FishingLuckBonusEnchantmentEffect import FishingLuckBonusEnchantmentEffect
    from generated_symbols.data.advancement.trigger.FishingRodHooked import FishingRodHooked
    from generated_symbols.data.enchantment.effect_component.FishingTimeReductionEnchantmentEffect import FishingTimeReductionEnchantmentEffect
    from generated_symbols.data.worldgen.dimension.biome_source.Fixed import Fixed
    from generated_symbols.data.worldgen.feature.placement.FixedPlacementModifier import FixedPlacementModifier
    from generated_symbols.data.util.FixedScoreProvider import FixedScoreProvider
    from generated_symbols.assets.shader.post.FixedSizedTarget import FixedSizedTarget
    from generated_symbols.data.worldgen.dimension.chunk_generator.Flat import Flat
    from generated_symbols.data.worldgen.dimension.chunk_generator.FlatGeneratorLayer import FlatGeneratorLayer
    from generated_symbols.data.worldgen.world_preset.FlatGeneratorPreset import FlatGeneratorPreset
    from generated_symbols.data.worldgen.dimension.chunk_generator.FlatGeneratorSettings import FlatGeneratorSettings
    from generated_symbols.data.worldgen.attribute.FloatAttribute import FloatAttribute
    from generated_symbols.data.worldgen.attribute.modifier.FloatAttributeModifier import FloatAttributeModifier
    from generated_symbols.data.worldgen.attribute.modifier.FloatModifierType import FloatModifierType
    from generated_symbols.data.worldgen.FloatProvider import FloatProvider
    from generated_symbols.data.worldgen.attribute.modifier.FloatWithAlpha import FloatWithAlpha
    from generated_symbols.data.advancement.predicate.FluidPredicate import FluidPredicate
    from generated_symbols.data.advancement.predicate.FluidPredicateState import FluidPredicateState
    from generated_symbols.data.worldgen.feature.tree.FoliagePlacer import FoliagePlacer
    from generated_symbols.assets.font.Font import Font
    from generated_symbols.assets.font.FontOption import FontOption
    from generated_symbols.data.advancement.predicate.FoodPredicate import FoodPredicate
    from generated_symbols.data.worldgen.feature.ForestRockConfig import ForestRockConfig
    from generated_symbols.data.worldgen.feature.FossilConfig import FossilConfig
    from generated_symbols.data.advancement.predicate.FoxPredicate import FoxPredicate
    from generated_symbols.data.enchantment.level_based_value.FractionLevelValue import FractionLevelValue
    from generated_symbols.data.worldgen.structure_set.FrequencyReductionMethod import FrequencyReductionMethod
    from generated_symbols.data.advancement.predicate.FrogPredicate import FrogPredicate
    from generated_symbols.data.variants.frog.FrogVariant import FrogVariant
    from generated_symbols.assets.shader.post.FullScreenTarget import FullScreenTarget
    from generated_symbols.data.gametest.test_environment.FunctionTestEnvironment import FunctionTestEnvironment
    from generated_symbols.data.gametest.FunctionTestInstance import FunctionTestInstance
    from generated_symbols.data.advancement.predicate.GameMode import GameMode
    from generated_symbols.data.gametest.test_environment.GameRuleMap import GameRuleMap
    from generated_symbols.data.gametest.test_environment.GameRulesTestEnvironment import GameRulesTestEnvironment
    from generated_symbols.data.worldgen.feature.GeodeBlockSettings import GeodeBlockSettings
    from generated_symbols.data.worldgen.feature.GeodeConfig import GeodeConfig
    from generated_symbols.data.worldgen.feature.GeodeCrackSettings import GeodeCrackSettings
    from generated_symbols.data.worldgen.feature.GeodeLayerSettings import GeodeLayerSettings
    from generated_symbols.data.worldgen.attribute.GlobalEnvironmentAttributeMap import GlobalEnvironmentAttributeMap
    from generated_symbols.assets.font.GlyphProvider import GlyphProvider
    from generated_symbols.assets.font.GlyphProviderType import GlyphProviderType
    from generated_symbols.assets.gpu_warnlist.GpuWarnlist import GpuWarnlist
    from generated_symbols.data.worldgen.density_function.Gradient import Gradient
    from generated_symbols.data.worldgen.biome.GrassColorModifier import GrassColorModifier
    from generated_symbols.assets.item_definition.GrassTint import GrassTint
    from generated_symbols.data.worldgen.processor_list.Gravity import Gravity
    from generated_symbols.data.slot_source.GroupSlotSource import GroupSlotSource
    from generated_symbols.data.worldgen.feature.GrowingPlantConfig import GrowingPlantConfig
    from generated_symbols.data.worldgen.feature.GrowingPlantHeight import GrowingPlantHeight
    from generated_symbols.assets.texture_meta.GuiMeta import GuiMeta
    from generated_symbols.assets.texture_meta.GuiSpriteScaling import GuiSpriteScaling
    from generated_symbols.assets.texture_meta.GuiSpriteScalingType import GuiSpriteScalingType
    from generated_symbols.assets.item_definition.HangingSign import HangingSign
    from generated_symbols.assets.item_definition.HangingSignAttachment import HangingSignAttachment
    from generated_symbols.assets.item_definition.HasComponent import HasComponent
    from generated_symbols.data.worldgen.feature.block_predicate.HasSturdyFacePredicate import HasSturdyFacePredicate
    from generated_symbols.assets.item_definition.Head import Head
    from generated_symbols.assets.item_definition.HeadType import HeadType
    from generated_symbols.data.worldgen.feature.tree.HeightFoliagePlacer import HeightFoliagePlacer
    from generated_symbols.data.worldgen.processor_list.HeightMatch import HeightMatch
    from generated_symbols.data.worldgen.HeightProvider import HeightProvider
    from generated_symbols.data.worldgen.feature.placement.HeightRangeModifier import HeightRangeModifier
    from generated_symbols.data.worldgen.feature.block_predicate.HeightRangePredicate import HeightRangePredicate
    from generated_symbols.data.worldgen.feature.decorator.HeightmapConfig import HeightmapConfig
    from generated_symbols.data.worldgen.feature.placement.HeightmapModifier import HeightmapModifier
    from generated_symbols.data.worldgen.HeightmapType import HeightmapType
    from generated_symbols.data.enchantment.effect_component.HitBlockEnchantmentEffect import HitBlockEnchantmentEffect
    from generated_symbols.data.advancement.trigger.HoneyHarvestedBlock import HoneyHarvestedBlock
    from generated_symbols.data.advancement.predicate.HorsePredicate import HorsePredicate
    from generated_symbols.data.worldgen.feature.HugeFungusConfig import HugeFungusConfig
    from generated_symbols.data.worldgen.feature.HugeMushroomConfig import HugeMushroomConfig
    from generated_symbols.data.worldgen.feature.IcebergConfig import IcebergConfig
    from generated_symbols.data.enchantment.effect.IgniteEntityEffect import IgniteEntityEffect
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.data.recipe.IngredientItem import IngredientItem
    from generated_symbols.data.recipe.IngredientTag import IngredientTag
    from generated_symbols.data.recipe.IngredientValue import IngredientValue
    from generated_symbols.data.dialog.input.InputControl import InputControl
    from generated_symbols.data.advancement.predicate.InputPredicate import InputPredicate
    from generated_symbols.data.loot.function.InsertListOperation import InsertListOperation
    from generated_symbols.data.worldgen.feature.block_predicate.InsideWorldBoundsPredicate import InsideWorldBoundsPredicate
    from generated_symbols.data.variants.instrument.Instrument import Instrument
    from generated_symbols.data.gametest.test_environment.IntGameRule import IntGameRule
    from generated_symbols.data.util.IntLimiter import IntLimiter
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.util.IntRange import IntRange
    from generated_symbols.assets.shader.post.InternalTarget import InternalTarget
    from generated_symbols.data.advancement.trigger.InventoryChanged import InventoryChanged
    from generated_symbols.data.advancement.trigger.InventoryChangedSlots import InventoryChangedSlots
    from generated_symbols.data.loot.condition.Inverted import Inverted
    from generated_symbols.data.worldgen.processor_list.InvertedMatch import InvertedMatch
    from generated_symbols.data.worldgen.density_function.InvervalSelect import InvervalSelect
    from generated_symbols.data.dialog.body.ItemBody import ItemBody
    from generated_symbols.data.enchantment.effect_component.ItemDamageEnchantmentEffect import ItemDamageEnchantmentEffect
    from generated_symbols.assets.item_definition.ItemDefinition import ItemDefinition
    from generated_symbols.assets.model.ItemDisplayContext import ItemDisplayContext
    from generated_symbols.data.advancement.trigger.ItemDurabilityChanged import ItemDurabilityChanged
    from generated_symbols.assets.item_definition.ItemModel import ItemModel
    from generated_symbols.assets.item_definition.ItemModeltype import ItemModeltype
    from generated_symbols.data.item_modifier.ItemModifier import ItemModifier
    from generated_symbols.data.loot.ItemPoolEntry import ItemPoolEntry
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.data.recipe.ItemResult import ItemResult
    from generated_symbols.data.loot.ItemStackTarget import ItemStackTarget
    from generated_symbols.assets.model.ItemTransform import ItemTransform
    from generated_symbols.data.advancement.trigger.ItemUsedOnBlock import ItemUsedOnBlock
    from generated_symbols.data.worldgen.structure.Jigsaw import Jigsaw
    from generated_symbols.data.worldgen.structure.JigsawDistanceLimits import JigsawDistanceLimits
    from generated_symbols.data.variants.jukebox_song.JukeboxSong import JukeboxSong
    from generated_symbols.assets.item_definition.KeybindDown import KeybindDown
    from generated_symbols.data.advancement.trigger.KillMobNearSculkCatalyst import KillMobNearSculkCatalyst
    from generated_symbols.data.advancement.trigger.KilledByArrow import KilledByArrow
    from generated_symbols.data.advancement.trigger.KilledByCrossbow import KilledByCrossbow
    from generated_symbols.data.loot.condition.KilledByPlayer import KilledByPlayer
    from generated_symbols.data.enchantment.effect_component.KnockbackEnchantmentEffect import KnockbackEnchantmentEffect
    from generated_symbols.data.sulfur_cube_archetype.KnockbackModifiers import KnockbackModifiers
    from generated_symbols.data.worldgen.feature.LakeConfig import LakeConfig
    from generated_symbols.assets.lang.Lang import Lang
    from generated_symbols.assets.lang.LangDeprecated import LangDeprecated
    from generated_symbols.data.worldgen.feature.LargeDripstoneConfig import LargeDripstoneConfig
    from generated_symbols.assets.equipment.Layer import Layer
    from generated_symbols.assets.equipment.Layers import Layers
    from generated_symbols.data.worldgen.feature.tree.LeaveVineTreeDecorator import LeaveVineTreeDecorator
    from generated_symbols.data.loot.function.LegacyExplorationMapDestination import LegacyExplorationMapDestination
    from generated_symbols.assets.font.LegacyUnicodeProvider import LegacyUnicodeProvider
    from generated_symbols.data.worldgen.density_function.Lerp import Lerp
    from generated_symbols.data.enchantment.level_based_value.LevelBasedValueMap import LevelBasedValueMap
    from generated_symbols.data.advancement.trigger.Levitation import Levitation
    from generated_symbols.data.advancement.predicate.LightningBoltPredicate import LightningBoltPredicate
    from generated_symbols.data.advancement.trigger.LightningStrike import LightningStrike
    from generated_symbols.data.loot.function.LimitCount import LimitCount
    from generated_symbols.data.slot_source.LimitCountSlotSource import LimitCountSlotSource
    from generated_symbols.data.enchantment.level_based_value.LinearLevelValue import LinearLevelValue
    from generated_symbols.data.worldgen.processor_list.LinearPos import LinearPos
    from generated_symbols.data.worldgen.structure.LiquidSettings import LiquidSettings
    from generated_symbols.data.worldgen.attribute.ListAttribute import ListAttribute
    from generated_symbols.data.dialog.ListDialogBase import ListDialogBase
    from generated_symbols.data.worldgen.template_pool.ListElement import ListElement
    from generated_symbols.data.worldgen.attribute.modifier.ListModifier import ListModifier
    from generated_symbols.data.worldgen.attribute.modifier.ListModifierType import ListModifierType
    from generated_symbols.data.loot.function.ListOperation import ListOperation
    from generated_symbols.data.loot.function.ListOperationMode import ListOperationMode
    from generated_symbols.data.advancement.predicate.LlamaPredicate import LlamaPredicate
    from generated_symbols.assets.item_definition.LocalTime import LocalTime
    from generated_symbols.data.enchantment.effect.LocationBasedEffect import LocationBasedEffect
    from generated_symbols.data.enchantment.effect_component.LocationChangedEnchantmentEffect import LocationChangedEnchantmentEffect
    from generated_symbols.data.loot.condition.LocationCheck import LocationCheck
    from generated_symbols.data.advancement.predicate.LocationPredicate import LocationPredicate
    from generated_symbols.data.advancement.predicate.LocationPredicateLight import LocationPredicateLight
    from generated_symbols.data.advancement.predicate.LocationPredicatePosition import LocationPredicatePosition
    from generated_symbols.data.enchantment.level_based_value.LookupLevelValue import LookupLevelValue
    from generated_symbols.data.loot.LootConditionType import LootConditionType
    from generated_symbols.data.loot.LootContextParamSets import LootContextParamSets
    from generated_symbols.data.loot.LootEntryType import LootEntryType
    from generated_symbols.data.loot.LootFunctionType import LootFunctionType
    from generated_symbols.data.loot.LootPool import LootPool
    from generated_symbols.data.loot.LootPoolEntry import LootPoolEntry
    from generated_symbols.data.loot.LootPoolEntryBase import LootPoolEntryBase
    from generated_symbols.data.loot.LootTable import LootTable
    from generated_symbols.data.loot.LootTableListRef import LootTableListRef
    from generated_symbols.data.loot.LootTablePoolEntry import LootTablePoolEntry
    from generated_symbols.data.loot.LootTableRef import LootTableRef
    from generated_symbols.data.loot.function.LootingEnchant import LootingEnchant
    from generated_symbols.assets.item_definition.MainHand import MainHand
    from generated_symbols.data.worldgen.feature.tree.MangroveRootPlacement import MangroveRootPlacement
    from generated_symbols.data.worldgen.feature.tree.MangroveRootPlacer import MangroveRootPlacer
    from generated_symbols.assets.item_definition.MapColorTint import MapColorTint
    from generated_symbols.data.loot.function.MapDecoration import MapDecoration
    from generated_symbols.data.loot.condition.MatchTool import MatchTool
    from generated_symbols.data.worldgen.feature.block_predicate.MatchingBiomesPredicate import MatchingBiomesPredicate
    from generated_symbols.data.worldgen.feature.block_predicate.MatchingBlockTagPredicate import MatchingBlockTagPredicate
    from generated_symbols.data.worldgen.feature.block_predicate.MatchingBlocksPredicate import MatchingBlocksPredicate
    from generated_symbols.data.worldgen.feature.block_predicate.MatchingFluidsPredicate import MatchingFluidsPredicate
    from generated_symbols.data.worldgen.material_condition.MaterialCondition import MaterialCondition
    from generated_symbols.data.worldgen.material_condition.MaterialConditionRef import MaterialConditionRef
    from generated_symbols.data.worldgen.material_rule.MaterialRule import MaterialRule
    from generated_symbols.data.worldgen.material_rule.MaterialRuleRef import MaterialRuleRef
    from generated_symbols.data.worldgen.feature.tree.MegaPineFoliagePlacer import MegaPineFoliagePlacer
    from generated_symbols.data.worldgen.attribute.MergeableAttribute import MergeableAttribute
    from generated_symbols.data.worldgen.attribute.modifier.MergeableModifier import MergeableModifier
    from generated_symbols.data.worldgen.attribute.modifier.MergeableModifierType import MergeableModifierType
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds
    from generated_symbols.data.worldgen.structure.Mineshaft import Mineshaft
    from generated_symbols.data.worldgen.structure.MineshaftType import MineshaftType
    from generated_symbols.assets.texture_meta.MipmapStrategy import MipmapStrategy
    from generated_symbols.data.worldgen.biome.MobCategory import MobCategory
    from generated_symbols.data.advancement.predicate.MobEffectPredicate import MobEffectPredicate
    from generated_symbols.data.enchantment.effect_component.MobExperienceEnchantmentEffect import MobExperienceEnchantmentEffect
    from generated_symbols.data.worldgen.biome.MobSpawnCost import MobSpawnCost
    from generated_symbols.assets.model.ModelDisplay import ModelDisplay
    from generated_symbols.assets.model.ModelElement import ModelElement
    from generated_symbols.assets.model.ModelElementFace import ModelElementFace
    from generated_symbols.assets.model.ModelElementFaceMap import ModelElementFaceMap
    from generated_symbols.assets.model.ModelElementRotation import ModelElementRotation
    from generated_symbols.assets.model.ModelElementRotationBase import ModelElementRotationBase
    from generated_symbols.assets.model.ModelOverride import ModelOverride
    from generated_symbols.assets.model.ModelOverridePredicates import ModelOverridePredicates
    from generated_symbols.assets.model.ModelRef import ModelRef
    from generated_symbols.assets.model.ModelTextures import ModelTextures
    from generated_symbols.assets.item_definition.ModelTint import ModelTint
    from generated_symbols.assets.block_state_definition.ModelVariant import ModelVariant
    from generated_symbols.assets.block_state_definition.ModelVariantBase import ModelVariantBase
    from generated_symbols.data.worldgen.feature.ModernNetherVegetationConfig import ModernNetherVegetationConfig
    from generated_symbols.data.worldgen.feature.ModernPatchConfig import ModernPatchConfig
    from generated_symbols.data.loot.function.ModifyContents import ModifyContents
    from generated_symbols.data.worldgen.biome.MoodSound import MoodSound
    from generated_symbols.data.variants.MoonBrightnessCheck import MoonBrightnessCheck
    from generated_symbols.data.util.MoonPhase import MoonPhase
    from generated_symbols.data.advancement.predicate.MooshroomPredicate import MooshroomPredicate
    from generated_symbols.data.advancement.predicate.MovementPredicate import MovementPredicate
    from generated_symbols.data.dialog.MultiActionDialog import MultiActionDialog
    from generated_symbols.data.dialog.input.MultiLine import MultiLine
    from generated_symbols.data.worldgen.dimension.biome_source.MultiNoise import MultiNoise
    from generated_symbols.data.worldgen.dimension.biome_source.MultiNoiseBase import MultiNoiseBase
    from generated_symbols.data.worldgen.dimension.biome_source.MultiNoiseBiomeSourceParameterList import MultiNoiseBiomeSourceParameterList
    from generated_symbols.data.worldgen.dimension.biome_source.MultiNoisePreset import MultiNoisePreset
    from generated_symbols.assets.block_state_definition.MultiPartAlternatives import MultiPartAlternatives
    from generated_symbols.assets.block_state_definition.MultiPartAnd import MultiPartAnd
    from generated_symbols.assets.block_state_definition.MultiPartCondition import MultiPartCondition
    from generated_symbols.data.worldgen.feature.MultifaceBlock import MultifaceBlock
    from generated_symbols.data.worldgen.feature.MultifaceGrowthConfig import MultifaceGrowthConfig
    from generated_symbols.assets.model.MultipleAxesModelElementRotation import MultipleAxesModelElementRotation
    from generated_symbols.data.enchantment.effect.MultiplyEffectValue import MultiplyEffectValue
    from generated_symbols.data.chat_type.Narration import Narration
    from generated_symbols.data.chat_type.NarrationPriority import NarrationPriority
    from generated_symbols.data.worldgen.biome.NaturalMobSpawns import NaturalMobSpawns
    from generated_symbols.data.util.NbtContextTarget import NbtContextTarget
    from generated_symbols.data.util.NbtProvider import NbtProvider
    from generated_symbols.data.util.NbtProviderSource import NbtProviderSource
    from generated_symbols.data.worldgen.feature.NetherForestVegetationConfig import NetherForestVegetationConfig
    from generated_symbols.data.worldgen.structure.NetherFossil import NetherFossil
    from generated_symbols.data.advancement.trigger.NetherTravel import NetherTravel
    from generated_symbols.data.worldgen.feature.NetherrackReplaceBlobsConfig import NetherrackReplaceBlobsConfig
    from generated_symbols.assets.texture_meta.NineSlice import NineSlice
    from generated_symbols.assets.texture_meta.NineSliceBorder import NineSliceBorder
    from generated_symbols.data.worldgen.feature.placement.NoiseBasedCountModifier import NoiseBasedCountModifier
    from generated_symbols.data.worldgen.noise_settings.NoiseGeneratorFlags import NoiseGeneratorFlags
    from generated_symbols.data.worldgen.noise_settings.NoiseGeneratorSettings import NoiseGeneratorSettings
    from generated_symbols.data.worldgen.noise_settings.NoiseGeneratorSettingsRef import NoiseGeneratorSettingsRef
    from generated_symbols.data.worldgen.dimension.biome_source.NoiseParameters import NoiseParameters
    from generated_symbols.data.worldgen.density_function.NoiseParametersRef import NoiseParametersRef
    from generated_symbols.data.worldgen.feature.block_state_provider.NoiseProvider import NoiseProvider
    from generated_symbols.data.worldgen.density_function.NoiseRange import NoiseRange
    from generated_symbols.data.worldgen.noise_settings.NoiseRouter import NoiseRouter
    from generated_symbols.data.worldgen.noise_settings.NoiseSamplingSettings import NoiseSamplingSettings
    from generated_symbols.data.worldgen.noise_settings.NoiseSettings import NoiseSettings
    from generated_symbols.data.worldgen.noise_settings.NoiseSlideSettings import NoiseSlideSettings
    from generated_symbols.data.worldgen.material_condition.NoiseThresholdCondition import NoiseThresholdCondition
    from generated_symbols.data.worldgen.feature.placement.NoiseThresholdCountModifier import NoiseThresholdCountModifier
    from generated_symbols.data.worldgen.feature.block_state_provider.NoiseThresholdProvider import NoiseThresholdProvider
    from generated_symbols.data.worldgen.material_condition.NotCondition import NotCondition
    from generated_symbols.data.worldgen.feature.block_predicate.NotPredicate import NotPredicate
    from generated_symbols.data.dialog.NoticeDialog import NoticeDialog
    from generated_symbols.assets.regional_compliancies.Notification import Notification
    from generated_symbols.data.recipe.NotificationInfo import NotificationInfo
    from generated_symbols.data.number_provider.NumberDispatcher import NumberDispatcher
    from generated_symbols.data.number_provider.NumberProvider import NumberProvider
    from generated_symbols.data.number_provider.NumberProviderListRef import NumberProviderListRef
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef
    from generated_symbols.data.dialog.input.NumberRangeInput import NumberRangeInput
    from generated_symbols.assets.item_definition.NumericPropertyType import NumericPropertyType
    from generated_symbols.data.worldgen.attribute.NumericalEnvironmentAttribute import NumericalEnvironmentAttribute
    from generated_symbols.data.worldgen.structure.OceanRuin import OceanRuin
    from generated_symbols.data.worldgen.feature.placement.OffsetModifier import OffsetModifier
    from generated_symbols.data.worldgen.density_function.OldBlendedNoise import OldBlendedNoise
    from generated_symbols.data.chat_type.OldChatType import OldChatType
    from generated_symbols.data.advancement.predicate.OldEntityPredicate import OldEntityPredicate
    from generated_symbols.data.worldgen.feature.OldPatchConfig import OldPatchConfig
    from generated_symbols.data.worldgen.feature.decorator.OldRangeConfig import OldRangeConfig
    from generated_symbols.data.worldgen.feature.OldSimpleBlockConfig import OldSimpleBlockConfig
    from generated_symbols.assets.shader.post.OldTarget import OldTarget
    from generated_symbols.data.trim.OldTrimMaterialOverrides import OldTrimMaterialOverrides
    from generated_symbols.data.worldgen.density_function.OneArgument import OneArgument
    from generated_symbols.data.dialog.input.Option import Option
    from generated_symbols.data.worldgen.feature.OptionalSimpleBlockConfig import OptionalSimpleBlockConfig
    from generated_symbols.data.recipe.OptionalSmithingIngredients import OptionalSmithingIngredients
    from generated_symbols.data.worldgen.feature.OreConfig import OreConfig
    from generated_symbols.data.worldgen.noise_settings.OreVeinifier import OreVeinifier
    from generated_symbols.data.worldgen.feature.OverlayConfig import OverlayConfig
    from generated_symbols.data.worldgen.attribute.modifier.OverrideModifier import OverrideModifier
    from generated_symbols.data.advancement.predicate.PaintingPredicate import PaintingPredicate
    from generated_symbols.data.variants.painting.PaintingVariant import PaintingVariant
    from generated_symbols.data.worldgen.feature.tree.PaleMossTreeDecorator import PaleMossTreeDecorator
    from generated_symbols.data.structure.Palette import Palette
    from generated_symbols.assets.texture_meta.PaletteMeta import PaletteMeta
    from generated_symbols.assets.atlas.PaletteRef import PaletteRef
    from generated_symbols.assets.atlas.PaletteTexture import PaletteTexture
    from generated_symbols.assets.atlas.PalettedPermutations import PalettedPermutations
    from generated_symbols.data.advancement.predicate.ParrotPredicate import ParrotPredicate
    from generated_symbols.assets.particle.Particle import Particle
    from generated_symbols.data.enchantment.effect.ParticlePosition import ParticlePosition
    from generated_symbols.data.enchantment.effect.ParticleVelocity import ParticleVelocity
    from generated_symbols.assets.shader.post.Pass import Pass
    from generated_symbols.assets.atlas.PermutationsMap import PermutationsMap
    from generated_symbols.data.variants.pig.PigModelType import PigModelType
    from generated_symbols.data.variants.pig.PigSounds import PigSounds
    from generated_symbols.data.variants.pig.PigVariant import PigVariant
    from generated_symbols.data.worldgen.feature.tree.PineFoliagePlacer import PineFoliagePlacer
    from generated_symbols.data.worldgen.feature.tree.PlaceOnGroundTreeDecorator import PlaceOnGroundTreeDecorator
    from generated_symbols.data.advancement.trigger.PlacedBlock import PlacedBlock
    from generated_symbols.data.worldgen.feature.placement.PlacedFeature import PlacedFeature
    from generated_symbols.data.worldgen.feature.placement.PlacedFeatureListRef import PlacedFeatureListRef
    from generated_symbols.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef
    from generated_symbols.data.worldgen.feature.placement.PlacementModifier import PlacementModifier
    from generated_symbols.data.dialog.body.PlainMessage import PlainMessage
    from generated_symbols.data.enchantment.effect.PlaySoundEntityEffect import PlaySoundEntityEffect
    from generated_symbols.data.advancement.predicate.PlayerAdvancementCriteria import PlayerAdvancementCriteria
    from generated_symbols.data.advancement.predicate.PlayerAdvancements import PlayerAdvancements
    from generated_symbols.data.advancement.trigger.PlayerGeneratesContainerLoot import PlayerGeneratesContainerLoot
    from generated_symbols.data.advancement.trigger.PlayerHurtEntity import PlayerHurtEntity
    from generated_symbols.data.advancement.trigger.PlayerInteract import PlayerInteract
    from generated_symbols.data.advancement.trigger.PlayerKilledEntity import PlayerKilledEntity
    from generated_symbols.data.advancement.predicate.PlayerPredicate import PlayerPredicate
    from generated_symbols.data.advancement.predicate.PlayerRecipes import PlayerRecipes
    from generated_symbols.data.advancement.trigger.PlayerTrigger import PlayerTrigger
    from generated_symbols.data.worldgen.structure.PoolAlias import PoolAlias
    from generated_symbols.data.worldgen.feature.tree.PoplarFoliagePlacer import PoplarFoliagePlacer
    from generated_symbols.data.worldgen.feature.tree.PoplarTrunkPlacer import PoplarTrunkPlacer
    from generated_symbols.data.worldgen.processor_list.PosRuleTest import PosRuleTest
    from generated_symbols.data.worldgen.attribute.PositionalEnvironmentAttribute import PositionalEnvironmentAttribute
    from generated_symbols.data.worldgen.attribute.PositionalEnvironmentAttributeMap import PositionalEnvironmentAttributeMap
    from generated_symbols.data.enchantment.effect_component.PostAttackEnchantmentEffect import PostAttackEnchantmentEffect
    from generated_symbols.data.advancement.predicate.PostComponentsItemPredicate import PostComponentsItemPredicate
    from generated_symbols.assets.shader.post.PostEffect import PostEffect
    from generated_symbols.data.enchantment.effect_component.PostPiercingAttackEnchantmentEffect import PostPiercingAttackEnchantmentEffect
    from generated_symbols.data.recipe.PotionIngredient import PotionIngredient
    from generated_symbols.assets.item_definition.PotionTint import PotionTint
    from generated_symbols.data.worldgen.density_function.Pow import Pow
    from generated_symbols.data.advancement.predicate.PreComponentsItemPredicate import PreComponentsItemPredicate
    from generated_symbols.data.worldgen.biome.Precipitation import Precipitation
    from generated_symbols.data.predicate.Predicate import Predicate
    from generated_symbols.data.predicate.PredicateListRef import PredicateListRef
    from generated_symbols.data.worldgen.feature.block_predicate.PredicateOffset import PredicateOffset
    from generated_symbols.data.predicate.PredicateRef import PredicateRef
    from generated_symbols.assets.model.Predicates import Predicates
    from generated_symbols.data.worldgen.feature.ProbabilityConfig import ProbabilityConfig
    from generated_symbols.data.worldgen.processor_list.Processor import Processor
    from generated_symbols.data.worldgen.processor_list.ProcessorList import ProcessorList
    from generated_symbols.data.worldgen.processor_list.ProcessorListObject import ProcessorListObject
    from generated_symbols.data.worldgen.processor_list.ProcessorListRef import ProcessorListRef
    from generated_symbols.data.worldgen.processor_list.ProcessorRule import ProcessorRule
    from generated_symbols.data.worldgen.feature.ProjectedSquareConfig import ProjectedSquareConfig
    from generated_symbols.data.enchantment.effect_component.ProjectileCountEnchantmentEffect import ProjectileCountEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.ProjectilePiercingEnchantmentEffect import ProjectilePiercingEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.ProjectileSpawnedEnchantmentEffect import ProjectileSpawnedEnchantmentEffect
    from generated_symbols.data.enchantment.effect_component.ProjectileSpreadEnchantmentEffect import ProjectileSpreadEnchantmentEffect
    from generated_symbols.data.worldgen.template_pool.Projection import Projection
    from generated_symbols.data.worldgen.processor_list.ProtectedBlocks import ProtectedBlocks
    from generated_symbols.data.worldgen.attribute.RGBColorAttribute import RGBColorAttribute
    from generated_symbols.data.advancement.predicate.RabbitPredicate import RabbitPredicate
    from generated_symbols.data.advancement.predicate.RaiderPredicate import RaiderPredicate
    from generated_symbols.data.worldgen.processor_list.RandomBlockMatch import RandomBlockMatch
    from generated_symbols.data.worldgen.processor_list.RandomBlockStateMatch import RandomBlockStateMatch
    from generated_symbols.data.worldgen.feature.block_state_provider.RandomBlockStateProvider import RandomBlockStateProvider
    from generated_symbols.data.worldgen.feature.RandomBooleanSelector import RandomBooleanSelector
    from generated_symbols.data.loot.condition.RandomChance import RandomChance
    from generated_symbols.data.worldgen.feature.placement.RandomChanceModifier import RandomChanceModifier
    from generated_symbols.data.loot.condition.RandomChanceWithEnchantedBonus import RandomChanceWithEnchantedBonus
    from generated_symbols.data.loot.condition.RandomChanceWithLooting import RandomChanceWithLooting
    from generated_symbols.data.worldgen.feature.RandomFeatureEntry import RandomFeatureEntry
    from generated_symbols.data.worldgen.structure.RandomGroupPoolAlias import RandomGroupPoolAlias
    from generated_symbols.data.util.RandomIntGenerator import RandomIntGenerator
    from generated_symbols.data.util.RandomIntGeneratorType import RandomIntGeneratorType
    from generated_symbols.data.worldgen.feature.RandomNeighborSpreadConfig import RandomNeighborSpreadConfig
    from generated_symbols.data.worldgen.feature.placement.RandomOffsetModifier import RandomOffsetModifier
    from generated_symbols.data.worldgen.feature.RandomPatchConfig import RandomPatchConfig
    from generated_symbols.data.worldgen.structure.RandomPoolAlias import RandomPoolAlias
    from generated_symbols.data.worldgen.feature.RandomSelector import RandomSelector
    from generated_symbols.data.worldgen.feature.tree.RandomSpreadFoliagePlacer import RandomSpreadFoliagePlacer
    from generated_symbols.data.worldgen.structure_set.RandomSpreadPlacement import RandomSpreadPlacement
    from generated_symbols.data.util.RandomValueBounds import RandomValueBounds
    from generated_symbols.data.worldgen.feature.block_state_provider.RandomizedIntStateProvider import RandomizedIntStateProvider
    from generated_symbols.data.structure.RandomizedPalette import RandomizedPalette
    from generated_symbols.data.worldgen.density_function.RangeChoice import RangeChoice
    from generated_symbols.data.worldgen.feature.decorator.RangeConfig import RangeConfig
    from generated_symbols.assets.item_definition.RangeDispatch import RangeDispatch
    from generated_symbols.assets.item_definition.RangeDispatchEntry import RangeDispatchEntry
    from generated_symbols.data.slot_source.RangeSlotSource import RangeSlotSource
    from generated_symbols.data.worldgen.feature.placement.RarityFilter import RarityFilter
    from generated_symbols.data.worldgen.density_function.RarityType import RarityType
    from generated_symbols.data.recipe.Recipe import Recipe
    from generated_symbols.data.advancement.trigger.RecipeCrafted import RecipeCrafted
    from generated_symbols.data.recipe.RecipeListRef import RecipeListRef
    from generated_symbols.data.advancement.trigger.RecipeUnlocked import RecipeUnlocked
    from generated_symbols.data.dialog.RedirectDialog import RedirectDialog
    from generated_symbols.data.enchantment.effect.ReduceBinomialEffectValue import ReduceBinomialEffectValue
    from generated_symbols.assets.font.ReferenceProvider import ReferenceProvider
    from generated_symbols.assets.regional_compliancies.RegionalCompliancies import RegionalCompliancies
    from generated_symbols.data.enchantment.effect_component.RepairWithXpEnchantmentEffect import RepairWithXpEnchantmentEffect
    from generated_symbols.data.enchantment.effect.ReplaceBlockEntityEffect import ReplaceBlockEntityEffect
    from generated_symbols.data.enchantment.effect.ReplaceDiskEntityEffect import ReplaceDiskEntityEffect
    from generated_symbols.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation
    from generated_symbols.data.worldgen.feature.ReplaceSingleBlockConfig import ReplaceSingleBlockConfig
    from generated_symbols.data.advancement.trigger.RequiredConditions import RequiredConditions
    from generated_symbols.data.recipe.RequiredSmithingIngredients import RequiredSmithingIngredients
    from generated_symbols.data.number_provider.ResolvableNumber import ResolvableNumber
    from generated_symbols.data.advancement.trigger.RideEntityInLava import RideEntityInLava
    from generated_symbols.data.worldgen.feature.tree.RootPlacer import RootPlacer
    from generated_symbols.data.worldgen.feature.RootSystemConfig import RootSystemConfig
    from generated_symbols.data.worldgen.feature.block_state_provider.RotatedStateProvider import RotatedStateProvider
    from generated_symbols.data.worldgen.density_function.Round import Round
    from generated_symbols.data.worldgen.structure.RuinedPortal import RuinedPortal
    from generated_symbols.data.worldgen.structure.RuinedPortalPlacement import RuinedPortalPlacement
    from generated_symbols.data.worldgen.structure.RuinedPortalSetup import RuinedPortalSetup
    from generated_symbols.data.worldgen.structure.RuinedPortalType import RuinedPortalType
    from generated_symbols.data.worldgen.processor_list.Rule import Rule
    from generated_symbols.data.worldgen.feature.RuleBasedBlockStateProvider import RuleBasedBlockStateProvider
    from generated_symbols.data.worldgen.processor_list.RuleTest import RuleTest
    from generated_symbols.data.enchantment.effect.RunFunctionEntityEffect import RunFunctionEntityEffect
    from generated_symbols.data.advancement.trigger.SafelyHarvestHoney import SafelyHarvestHoney
    from generated_symbols.data.advancement.predicate.SalmonPredicate import SalmonPredicate
    from generated_symbols.data.advancement.predicate.SalmonVariant import SalmonVariant
    from generated_symbols.assets.shader.program.Sampler import Sampler
    from generated_symbols.data.number_provider.ScoreNumberProvider import ScoreNumberProvider
    from generated_symbols.data.util.ScoreProvider import ScoreProvider
    from generated_symbols.data.worldgen.feature.SculkPatchConfig import SculkPatchConfig
    from generated_symbols.data.worldgen.feature.SeaPickleConfig import SeaPickleConfig
    from generated_symbols.assets.item_definition.Select import Select
    from generated_symbols.assets.item_definition.SelectCase import SelectCase
    from generated_symbols.assets.item_definition.SelectCases import SelectCases
    from generated_symbols.assets.item_definition.SelectPropertyType import SelectPropertyType
    from generated_symbols.data.loot.function.Sequence import Sequence
    from generated_symbols.data.worldgen.feature.SequenceConfig import SequenceConfig
    from generated_symbols.data.worldgen.material_rule.SequenceRule import SequenceRule
    from generated_symbols.data.dialog.ServerLinksDialog import ServerLinksDialog
    from generated_symbols.data.loot.function.SetAttributes import SetAttributes
    from generated_symbols.data.loot.function.SetBannerPattern import SetBannerPattern
    from generated_symbols.data.enchantment.effect.SetBlockPropertiesEntityEffect import SetBlockPropertiesEntityEffect
    from generated_symbols.data.loot.function.SetBookCover import SetBookCover
    from generated_symbols.data.loot.function.SetComponents import SetComponents
    from generated_symbols.data.loot.function.SetContents import SetContents
    from generated_symbols.data.loot.function.SetCount import SetCount
    from generated_symbols.data.loot.function.SetCustomData import SetCustomData
    from generated_symbols.data.loot.function.SetCustomModelData import SetCustomModelData
    from generated_symbols.data.loot.function.SetDamage import SetDamage
    from generated_symbols.data.enchantment.effect.SetEffectValue import SetEffectValue
    from generated_symbols.data.loot.function.SetEnchantments import SetEnchantments
    from generated_symbols.data.loot.function.SetFireworkExplosion import SetFireworkExplosion
    from generated_symbols.data.loot.function.SetFireworks import SetFireworks
    from generated_symbols.data.loot.function.SetInstrument import SetInstrument
    from generated_symbols.data.loot.function.SetItem import SetItem
    from generated_symbols.data.loot.function.SetLootTable import SetLootTable
    from generated_symbols.data.loot.function.SetLore import SetLore
    from generated_symbols.data.loot.function.SetName import SetName
    from generated_symbols.data.loot.function.SetNameTarget import SetNameTarget
    from generated_symbols.data.loot.function.SetNbt import SetNbt
    from generated_symbols.data.loot.function.SetOminousBottleAmplifier import SetOminousBottleAmplifier
    from generated_symbols.data.loot.function.SetPotion import SetPotion
    from generated_symbols.data.loot.function.SetRandomDyes import SetRandomDyes
    from generated_symbols.data.loot.function.SetRandomPotion import SetRandomPotion
    from generated_symbols.data.loot.function.SetStewEffect import SetStewEffect
    from generated_symbols.data.loot.function.SetWriteableBookPages import SetWriteableBookPages
    from generated_symbols.data.loot.function.SetWrittenBookPages import SetWrittenBookPages
    from generated_symbols.assets.shader.program.ShaderProgram import ShaderProgram
    from generated_symbols.data.advancement.predicate.SheepPredicate import SheepPredicate
    from generated_symbols.data.worldgen.feature.tree.ShelfMushroomTreeDecorator import ShelfMushroomTreeDecorator
    from generated_symbols.data.worldgen.density_function.Shift import Shift
    from generated_symbols.data.worldgen.density_function.ShiftedNoise import ShiftedNoise
    from generated_symbols.data.worldgen.structure.Shipwreck import Shipwreck
    from generated_symbols.data.advancement.trigger.ShotCrossbow import ShotCrossbow
    from generated_symbols.assets.item_definition.ShulkerBox import ShulkerBox
    from generated_symbols.data.worldgen.feature.SimpleBlockConfig import SimpleBlockConfig
    from generated_symbols.data.timeline.SimpleEasingType import SimpleEasingType
    from generated_symbols.data.worldgen.feature.SimpleRandomSelectorConfig import SimpleRandomSelectorConfig
    from generated_symbols.data.worldgen.feature.block_state_provider.SimpleStateProvider import SimpleStateProvider
    from generated_symbols.assets.atlas.Single import Single
    from generated_symbols.assets.model.SingleAxisModelElementRotation import SingleAxisModelElementRotation
    from generated_symbols.data.worldgen.feature.SingleBlockPillarConfig import SingleBlockPillarConfig
    from generated_symbols.data.worldgen.template_pool.SingleElement import SingleElement
    from generated_symbols.data.dialog.input.SingleOptionInput import SingleOptionInput
    from generated_symbols.data.enchantment.provider.SingleProvider import SingleProvider
    from generated_symbols.data.loot.SingletonPoolEntry import SingletonPoolEntry
    from generated_symbols.data.worldgen.dimension.SkyboxType import SkyboxType
    from generated_symbols.data.worldgen.density_function.Slice import Slice
    from generated_symbols.data.advancement.trigger.SlideDownBlock import SlideDownBlock
    from generated_symbols.data.advancement.predicate.SlimePredicate import SlimePredicate
    from generated_symbols.data.slot_source.SlotSource import SlotSource
    from generated_symbols.data.loot.SlotsPoolEntry import SlotsPoolEntry
    from generated_symbols.data.worldgen.feature.SmallDripstoneConfig import SmallDripstoneConfig
    from generated_symbols.data.enchantment.effect_component.SmashDamagePerBlockFallenEnchantmentEffect import SmashDamagePerBlockFallenEnchantmentEffect
    from generated_symbols.data.recipe.Smelting import Smelting
    from generated_symbols.data.recipe.Smithing import Smithing
    from generated_symbols.data.recipe.SmithingIngredients import SmithingIngredients
    from generated_symbols.data.recipe.SmithingTransform import SmithingTransform
    from generated_symbols.data.recipe.SmithingTransformResult import SmithingTransformResult
    from generated_symbols.data.recipe.SmithingTrim import SmithingTrim
    from generated_symbols.assets.sounds.Sound import Sound
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.assets.sounds.SoundEventRegistration import SoundEventRegistration
    from generated_symbols.data.sulfur_cube_archetype.SoundSettings import SoundSettings
    from generated_symbols.assets.sounds.SoundType import SoundType
    from generated_symbols.data.variants.SoundVariant import SoundVariant
    from generated_symbols.assets.sounds.Sounds import Sounds
    from generated_symbols.assets.font.SpaceProvider import SpaceProvider
    from generated_symbols.data.variants.SpawnCondition import SpawnCondition
    from generated_symbols.data.worldgen.structure.SpawnOverride import SpawnOverride
    from generated_symbols.data.enchantment.effect.SpawnParticlesEntityEffect import SpawnParticlesEntityEffect
    from generated_symbols.data.variants.SpawnPrioritySelector import SpawnPrioritySelector
    from generated_symbols.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors
    from generated_symbols.data.worldgen.noise_settings.SpawnTargetPoint import SpawnTargetPoint
    from generated_symbols.data.worldgen.biome.SpawnerData import SpawnerData
    from generated_symbols.data.worldgen.biome.SpawnerDataMap import SpawnerDataMap
    from generated_symbols.data.advancement.trigger.SpearMobs import SpearMobs
    from generated_symbols.assets.item_definition.Special import Special
    from generated_symbols.assets.item_definition.SpecialModel import SpecialModel
    from generated_symbols.assets.item_definition.SpecialModelType import SpecialModelType
    from generated_symbols.data.advancement.predicate.SpecificType import SpecificType
    from generated_symbols.data.worldgen.feature.SpeleothemClusterConfig import SpeleothemClusterConfig
    from generated_symbols.data.worldgen.feature.SpeleothemConfig import SpeleothemConfig
    from generated_symbols.data.worldgen.feature.SpikeConfig import SpikeConfig
    from generated_symbols.data.worldgen.density_function.Spline import Spline
    from generated_symbols.data.worldgen.density_function.SplinePoint import SplinePoint
    from generated_symbols.data.worldgen.density_function.SplineType import SplineType
    from generated_symbols.data.worldgen.structure_set.SpreadType import SpreadType
    from generated_symbols.data.worldgen.feature.SpringConfig import SpringConfig
    from generated_symbols.assets.atlas.SpriteSource import SpriteSource
    from generated_symbols.assets.atlas.SpriteSourceType import SpriteSourceType
    from generated_symbols.data.worldgen.feature.tree.SprucePineFoliagePlacer import SprucePineFoliagePlacer
    from generated_symbols.data.enchantment.level_based_value.SquaredLevelValue import SquaredLevelValue
    from generated_symbols.assets.item_definition.StandingSign import StandingSign
    from generated_symbols.assets.item_definition.StandingSignAttachment import StandingSignAttachment
    from generated_symbols.data.advancement.predicate.StatisticPredicate import StatisticPredicate
    from generated_symbols.data.loot.function.StewEffect import StewEffect
    from generated_symbols.data.worldgen.material_condition.StoneDepthCondition import StoneDepthCondition
    from generated_symbols.data.recipe.Stonecutting import Stonecutting
    from generated_symbols.data.util.StorageNbtProvider import StorageNbtProvider
    from generated_symbols.data.number_provider.StorageNumberProvider import StorageNumberProvider
    from generated_symbols.data.worldgen.structure.Structure import Structure
    from generated_symbols.data.structure.StructureBlock import StructureBlock
    from generated_symbols.data.variants.StructureCheck import StructureCheck
    from generated_symbols.data.structure.StructureEntity import StructureEntity
    from generated_symbols.data.structure.StructureNBT import StructureNBT
    from generated_symbols.data.worldgen.structure_set.StructurePlacement import StructurePlacement
    from generated_symbols.data.worldgen.structure.StructureRef import StructureRef
    from generated_symbols.data.worldgen.structure_set.StructureSet import StructureSet
    from generated_symbols.data.worldgen.structure_set.StructureSetElement import StructureSetElement
    from generated_symbols.data.worldgen.structure_set.StructureSetRef import StructureSetRef
    from generated_symbols.data.worldgen.noise_settings.StructureSettings import StructureSettings
    from generated_symbols.data.sulfur_cube_archetype.SulfurCubeArchetype import SulfurCubeArchetype
    from generated_symbols.data.number_provider.SumNumberProvider import SumNumberProvider
    from generated_symbols.data.enchantment.effect.SummonEntityEffect import SummonEntityEffect
    from generated_symbols.data.advancement.trigger.SummonedEntity import SummonedEntity
    from generated_symbols.data.worldgen.feature.placement.SurfaceRelativeThresholdFilter import SurfaceRelativeThresholdFilter
    from generated_symbols.data.worldgen.feature.placement.SurfaceWaterDepthFilter import SurfaceWaterDepthFilter
    from generated_symbols.data.loot.condition.TableBonus import TableBonus
    from generated_symbols.data.tag.Tag import Tag
    from generated_symbols.data.tag.TagEntry import TagEntry
    from generated_symbols.data.worldgen.processor_list.TagMatch import TagMatch
    from generated_symbols.data.loot.TagPoolEntry import TagPoolEntry
    from generated_symbols.data.advancement.trigger.TameAnimal import TameAnimal
    from generated_symbols.data.worldgen.feature.TargetBlock import TargetBlock
    from generated_symbols.data.advancement.trigger.TargetHit import TargetHit
    from generated_symbols.assets.shader.post.TargetInput import TargetInput
    from generated_symbols.assets.shader.post.Targets import Targets
    from generated_symbols.assets.item_definition.TeamTint import TeamTint
    from generated_symbols.data.worldgen.biome.TemperatureModifier import TemperatureModifier
    from generated_symbols.data.worldgen.feature.TemplateConfig import TemplateConfig
    from generated_symbols.data.worldgen.feature.TemplateEntry import TemplateEntry
    from generated_symbols.data.worldgen.template_pool.TemplatePool import TemplatePool
    from generated_symbols.data.worldgen.structure.TerrainAdaptation import TerrainAdaptation
    from generated_symbols.data.worldgen.density_function.TerrainCoordinate import TerrainCoordinate
    from generated_symbols.data.worldgen.noise_settings.TerrainShaper import TerrainShaper
    from generated_symbols.data.worldgen.density_function.TerrainShaperSpline import TerrainShaperSpline
    from generated_symbols.data.gametest.TestData import TestData
    from generated_symbols.data.gametest.test_environment.TestEnvironment import TestEnvironment
    from generated_symbols.data.gametest.TestInstance import TestInstance
    from generated_symbols.data.chat_type.TextDisplay import TextDisplay
    from generated_symbols.data.dialog.input.TextInput import TextInput
    from generated_symbols.assets.texture_meta.TextureAnimation import TextureAnimation
    from generated_symbols.assets.texture_meta.TextureAnimationFrame import TextureAnimationFrame
    from generated_symbols.assets.shader.post.TextureInput import TextureInput
    from generated_symbols.assets.model.TextureMaterial import TextureMaterial
    from generated_symbols.assets.texture_meta.TextureMeta import TextureMeta
    from generated_symbols.data.worldgen.dimension.biome_source.TheEnd import TheEnd
    from generated_symbols.data.worldgen.feature.tree.ThreeLayersFeatureSize import ThreeLayersFeatureSize
    from generated_symbols.data.advancement.trigger.ThrownItemPickedUpByEntity import ThrownItemPickedUpByEntity
    from generated_symbols.data.advancement.trigger.ThrownItemPickedUpByPlayer import ThrownItemPickedUpByPlayer
    from generated_symbols.data.enchantment.effect_component.TickEnchantmentEffect import TickEnchantmentEffect
    from generated_symbols.assets.texture_meta.TileScaling import TileScaling
    from generated_symbols.data.worldgen.density_function.TilingMode import TilingMode
    from generated_symbols.assets.item_definition.Time import Time
    from generated_symbols.data.loot.condition.TimeCheck import TimeCheck
    from generated_symbols.data.timeline.TimeMarker import TimeMarker
    from generated_symbols.data.timeline.TimeMarkerMap import TimeMarkerMap
    from generated_symbols.data.gametest.test_environment.TimeOfDayTestEnvironment import TimeOfDayTestEnvironment
    from generated_symbols.assets.item_definition.TimeSource import TimeSource
    from generated_symbols.data.timeline.Timeline import Timeline
    from generated_symbols.data.gametest.test_environment.TimelineAttributesTestEnvironment import TimelineAttributesTestEnvironment
    from generated_symbols.assets.item_definition.TintSourceType import TintSourceType
    from generated_symbols.data.loot.function.ToggleTooltips import ToggleTooltips
    from generated_symbols.data.loot.function.ToggleableDataComponent import ToggleableDataComponent
    from generated_symbols.data.trade_set.TradeSet import TradeSet
    from generated_symbols.data.worldgen.attribute.modifier.TranslucentColorAttributeModifier import TranslucentColorAttributeModifier
    from generated_symbols.data.worldgen.TrapezoidHeightProvider import TrapezoidHeightProvider
    from generated_symbols.data.worldgen.feature.tree.TreeConfig import TreeConfig
    from generated_symbols.data.worldgen.feature.tree.TreeDecorator import TreeDecorator
    from generated_symbols.data.worldgen.attribute.TriState import TriState
    from generated_symbols.data.trial_spawner.TrialSpawnerConfig import TrialSpawnerConfig
    from generated_symbols.data.worldgen.structure.TrickyTrialsStructureConfig import TrickyTrialsStructureConfig
    from generated_symbols.data.enchantment.effect_component.TridentReturnAccelerationEnchantmentEffect import TridentReturnAccelerationEnchantmentEffect
    from generated_symbols.data.advancement.Trigger import Trigger
    from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase
    from generated_symbols.data.trim.TrimMaterialOverrides import TrimMaterialOverrides
    from generated_symbols.assets.equipment.TrimOverride import TrimOverride
    from generated_symbols.data.trim.TrimPattern import TrimPattern
    from generated_symbols.assets.equipment.TrimPredicate import TrimPredicate
    from generated_symbols.data.advancement.predicate.TropicalFishPredicate import TropicalFishPredicate
    from generated_symbols.data.worldgen.feature.tree.TrunkPlacer import TrunkPlacer
    from generated_symbols.assets.font.TtfProvider import TtfProvider
    from generated_symbols.data.worldgen.feature.TwistingVinesConfig import TwistingVinesConfig
    from generated_symbols.data.worldgen.density_function.TwoArguments import TwoArguments
    from generated_symbols.data.worldgen.feature.tree.TwoLayersFeatureSize import TwoLayersFeatureSize
    from generated_symbols.data.slot_source.TypedSlotSource import TypedSlotSource
    from generated_symbols.data.worldgen.feature.UnderwaterMagmaConfig import UnderwaterMagmaConfig
    from generated_symbols.assets.shader.program.Uniform import Uniform
    from generated_symbols.assets.shader.post.UniformBlocks import UniformBlocks
    from generated_symbols.data.loot.function.UniformBonusFormula import UniformBonusFormula
    from generated_symbols.data.worldgen.UniformHeightProvider import UniformHeightProvider
    from generated_symbols.data.worldgen.UniformInt import UniformInt
    from generated_symbols.data.util.UniformIntGenerator import UniformIntGenerator
    from generated_symbols.data.worldgen.UniformIntProvider import UniformIntProvider
    from generated_symbols.data.number_provider.UniformNumberProvider import UniformNumberProvider
    from generated_symbols.assets.shader.program.UniformType import UniformType
    from generated_symbols.assets.shader.post.UniformValue import UniformValue
    from generated_symbols.assets.shader.post.UniformValueType import UniformValueType
    from generated_symbols.assets.font.UnihexOverrideRange import UnihexOverrideRange
    from generated_symbols.assets.font.UnihexProvider import UnihexProvider
    from generated_symbols.data.storage.UnknownStorage import UnknownStorage
    from generated_symbols.data.worldgen.feature.block_predicate.UnobstructedPredicate import UnobstructedPredicate
    from generated_symbols.assets.atlas.Unstitch import Unstitch
    from generated_symbols.assets.atlas.UnstitchRegion import UnstitchRegion
    from generated_symbols.data.worldgen.feature.tree.UpwardsBranchingTrunkPlacer import UpwardsBranchingTrunkPlacer
    from generated_symbols.assets.item_definition.UseCycle import UseCycle
    from generated_symbols.assets.item_definition.UseDuration import UseDuration
    from generated_symbols.data.advancement.trigger.UsedEnderEye import UsedEnderEye
    from generated_symbols.data.advancement.trigger.UsedTotem import UsedTotem
    from generated_symbols.data.advancement.trigger.UsingItem import UsingItem
    from generated_symbols.data.loot.condition.ValueCheck import ValueCheck
    from generated_symbols.data.enchantment.effect.ValueEffect import ValueEffect
    from generated_symbols.data.worldgen.dimension.biome_source.VanillaLayered import VanillaLayered
    from generated_symbols.data.worldgen.feature.VegetationPatchConfig import VegetationPatchConfig
    from generated_symbols.data.worldgen.VerticalAnchor import VerticalAnchor
    from generated_symbols.data.worldgen.material_condition.VerticalGradientCondition import VerticalGradientCondition
    from generated_symbols.assets.item_definition.ViewEntity import ViewEntity
    from generated_symbols.assets.texture_meta.VillagerHatType import VillagerHatType
    from generated_symbols.data.advancement.predicate.VillagerPredicate import VillagerPredicate
    from generated_symbols.assets.texture_meta.VillagerTextureMeta import VillagerTextureMeta
    from generated_symbols.data.worldgen.material_condition.WaterCondition import WaterCondition
    from generated_symbols.data.worldgen.feature.decorator.WaterDepthThresholdConfig import WaterDepthThresholdConfig
    from generated_symbols.assets.waypoint_style.WaypointStyle import WaypointStyle
    from generated_symbols.data.gametest.test_environment.Weather import Weather
    from generated_symbols.data.loot.condition.WeatherCheck import WeatherCheck
    from generated_symbols.data.gametest.test_environment.WeatherTestEnvironment import WeatherTestEnvironment
    from generated_symbols.data.worldgen.WeightListHeightProvider import WeightListHeightProvider
    from generated_symbols.data.worldgen.feature.block_state_provider.WeightedBlockStateProvider import WeightedBlockStateProvider
    from generated_symbols.data.worldgen.template_pool.WeightedElement import WeightedElement
    from generated_symbols.assets.block_state_definition.WeightedModelVariant import WeightedModelVariant
    from generated_symbols.data.number_provider.WeightedNumberProvider import WeightedNumberProvider
    from generated_symbols.data.worldgen.feature.WeightedRandomFeatureConfig import WeightedRandomFeatureConfig
    from generated_symbols.data.util.WeightedSoundEvent import WeightedSoundEvent
    from generated_symbols.data.worldgen.density_function.WeirdScaledSampler import WeirdScaledSampler
    from generated_symbols.data.worldgen.structure.WildUpdateStructureConfig import WildUpdateStructureConfig
    from generated_symbols.assets.equipment.WingsLayer import WingsLayer
    from generated_symbols.data.advancement.predicate.WolfPredicate import WolfPredicate
    from generated_symbols.data.variants.wolf.WolfSounds import WolfSounds
    from generated_symbols.data.variants.wolf.WolfVariant import WolfVariant
    from generated_symbols.data.variants.wolf.WolfVariantAssetInfo import WolfVariantAssetInfo
    from generated_symbols.assets.item_definition.WoodType import WoodType
    from generated_symbols.data.worldgen.world_preset.WorldPreset import WorldPreset
    from generated_symbols.data.worldgen.feature.block_predicate.WouldSurvivePredicate import WouldSurvivePredicate
    from generated_symbols.data.worldgen.material_condition.YAboveCondition import YAboveCondition
    from generated_symbols.data.worldgen.density_function.YClampedGradient import YClampedGradient
    from generated_symbols.data.variants.zombie_nautilus.ZombieNautilusModelType import ZombieNautilusModelType
    from generated_symbols.data.variants.zombie_nautilus.ZombieNautilusVariant import ZombieNautilusVariant

__all__ = [
    "ARGBColorAttribute",
    "AboveRootPlacement",
    "ActuallyTranslucentRGB",
    "AddEffectValue",
    "Advancement",
    "AdvancementCriteriaMap",
    "AdvancementCriterion",
    "AdvancementDisplay",
    "AdvancementFrame",
    "AdvancementIcon",
    "AdvancementPredicateRef",
    "AdvancementRewards",
    "AfterAction",
    "AllOf",
    "AllOfEffectValue",
    "AllOfEntityEffect",
    "AllOfLocationBasedEffect",
    "AllOffTestEnvironment",
    "AllayDropItemOnBlock",
    "AlterGroundTreeDecorator",
    "Alternative",
    "AmbientParticle",
    "AmbientSounds",
    "AmmoUseEnchantmentEffect",
    "AnyBlockUse",
    "AnyOf",
    "AppendLoot",
    "AppendStatic",
    "ApplyBonus",
    "ApplyBonusFormula",
    "ApplyExhaustionEntityEffect",
    "ApplyImpulseEntityEffect",
    "ApplyMobEffectEntityEffect",
    "Aquifer",
    "ArmorEffectivenessEnchantmentEffect",
    "ArmorMaterial",
    "Atlas",
    "AttachedToLeavesTreeDecorator",
    "AttachedToLogsTreeDecorator",
    "AttackTarget",
    "AttributeEffect",
    "AttributeEntry",
    "AttributeModifier",
    "AttributeTrackBase",
    "AuxTarget",
    "AxisAlignedLinearPos",
    "AxolotlPredicate",
    "BackgroundMusic",
    "Banner",
    "BannerAttachment",
    "BannerPatternLayer",
    "BaseNoiseProvider",
    "Bed",
    "BedPart",
    "BedRule",
    "BedRuleType",
    "BeeNestDestroyed",
    "BeehiveTreeDecorator",
    "BendingTrunkPlacer",
    "BinomialIntGenerator",
    "BinomialNumberProvider",
    "BinomialWithBonusCountFormula",
    "Biome",
    "BiomeCategory",
    "BiomeCheck",
    "BiomeCondition",
    "BiomeEffects",
    "BiomeMusic",
    "BiomeNoiseEntry",
    "BiomeParticle",
    "BiomeSoundAdditions",
    "BiomeSource",
    "BiomeTemperature",
    "BitmapProvider",
    "BlendFactor",
    "BlendFunc",
    "BlendMode",
    "BlendToGray",
    "BlockAge",
    "BlockBasedTestInstance",
    "BlockBlobConfig",
    "BlockColumnConfig",
    "BlockColumnLayer",
    "BlockEntityModifier",
    "BlockEntityTarget",
    "BlockExperienceEnchantmentEffect",
    "BlockIgnore",
    "BlockInteraction",
    "BlockMatch",
    "BlockPalette",
    "BlockPileConfig",
    "BlockPlacer",
    "BlockPredicateFilter",
    "BlockPredicateState",
    "BlockRot",
    "BlockRule",
    "BlockState",
    "BlockStateDefinition",
    "BlockStateDefinitionMultipart",
    "BlockStateDefinitionMultipartEntry",
    "BlockStateDefinitionVariant",
    "BlockStateDefinitionVariantMap",
    "BlockStateMatch",
    "BlockStateProperty",
    "BlockStateProvider",
    "BlockStateRuleProviderEntry",
    "BoatPredicate",
    "Book",
    "BoolGameRule",
    "BooleanAttribute",
    "BooleanAttributeModifier",
    "BooleanInput",
    "BooleanModifierType",
    "BottomBiasHeightProvider",
    "BoundingBox",
    "BredAnimals",
    "BrewedPotion",
    "Brewing",
    "BuriedTreasure",
    "Button",
    "ButtonListDialogBase",
    "ByCostEnchantmentProvider",
    "ByCostWithDifficultyEnchantmentProvider",
    "CanyonConfig",
    "CanyonShape",
    "Capped",
    "CardinalLightType",
    "CarveStep",
    "CarverConfigBase",
    "CarverDebugSettings",
    "CarverListRef",
    "CarverRef",
    "CarversPerStep",
    "CarvingMaskConfig",
    "CarvingMaskModifier",
    "CatPredicate",
    "CatSounds",
    "CatVariant",
    "CaveConfig",
    "ChanceConfig",
    "ChangeItemDamageEffect",
    "ChangedDimension",
    "ChanneledLightning",
    "ChargeType",
    "ChatDecoration",
    "ChatDecorationParameter",
    "ChatType",
    "Checkerboard",
    "CherryFoliagePlacer",
    "CherryTrunkPlacer",
    "Chest",
    "ChestType",
    "ChickenModelType",
    "ChickenSounds",
    "ChickenVariant",
    "ChunkGenerator",
    "Clamp",
    "ClampedIntProvider",
    "ClampedLevelValue",
    "ClampedNormalIntProvider",
    "ClickAction",
    "ClimateParameter",
    "ClimateParameters",
    "ClockTimeTestEnvironment",
    "CocoaTreeDecorator",
    "Code",
    "ColorAttributeModifier",
    "ColorModifierType",
    "ColormapTextureMeta",
    "ColumnPlacer",
    "ColumnsConfig",
    "CombiningPredicate",
    "Compass",
    "CompassTarget",
    "ComponentFlags",
    "ComponentStrings",
    "Composite",
    "CompositeEntity",
    "CompositeMatch",
    "CompositePoolEntry",
    "ConcentricRingsPlacement",
    "Condition",
    "ConditionRule",
    "ConditionalNumberProvider",
    "ConditionalPropertyType",
    "Config",
    "ConfiguredCarver",
    "ConfiguredDecorator",
    "ConfiguredFeature",
    "ConfiguredFeatureRef",
    "ConfiguredSurfaceBuilder",
    "ConfiguredSurfaceBuilderRef",
    "ConfirmationDialog",
    "Constant",
    "ConstantHeightProvider",
    "ConstantIntGenerator",
    "ConstantIntProvider",
    "ConstantNumberProvider",
    "ConstantTint",
    "ConstructBeacon",
    "ConsumeItem",
    "ContactDamage",
    "ContainerComponents",
    "ContentsSlotSource",
    "ContextDimension",
    "ContextEntityType",
    "ContextNbtProvider",
    "ContextScoreProvider",
    "CookingBookCategory",
    "CookingBookInfo",
    "CopperGolemStatue",
    "CopperGolemStatuePose",
    "CopyComponents",
    "CopyName",
    "CopyNameSource",
    "CopyNbt",
    "CopyNbtOperation",
    "CopyNbtStrategy",
    "CopyPropertiesProvider",
    "CopyState",
    "CoralConfig",
    "Count",
    "CountConfig",
    "CountExtraConfig",
    "CountModifier",
    "CountNoiseBiasedConfig",
    "CountNoiseConfig",
    "CountOnEveryLayerModifier",
    "CowModelType",
    "CowSounds",
    "CowVariant",
    "CraftingBookCategory",
    "CraftingBookInfo",
    "CraftingDecoratedPot",
    "CraftingDye",
    "CraftingImbue",
    "CraftingIngredients",
    "CraftingShaped",
    "CraftingShapeless",
    "CraftingSpecialBannerDuplicate",
    "CraftingSpecialBookCloning",
    "CraftingSpecialFireworkRocket",
    "CraftingSpecialFireworkStar",
    "CraftingSpecialFireworkStarFade",
    "CraftingSpecialMapExtending",
    "CraftingSpecialShieldDecoration",
    "CraftingTransmute",
    "CreakingHeartTreeDecorator",
    "Credits",
    "CreditsCompanySegment",
    "CreditsDiscipline",
    "CreditsJobTitle",
    "CrossbowChargeSoundsEnchantmentEffect",
    "CrossbowChargeType",
    "CubicBezierEase",
    "CubicSpline",
    "CuboidModifier",
    "CuredZombieVillager",
    "CustomModelDataColors",
    "CustomModelDataTint",
    "CustomizableItemDisplayContext",
    "Damage",
    "DamageEffects",
    "DamageEnchantmentEffect",
    "DamageEntityEffect",
    "DamageImmunityEnchantmentEffect",
    "DamageItemEffect",
    "DamagePredicate",
    "DamageProtectionEnchantmentEffect",
    "DamageScaling",
    "DamageSourceFlags",
    "DamageSourcePredicate",
    "DamageSourceProperties",
    "DamageTagPredicate",
    "DamageType",
    "DeathMessageType",
    "DecoratedPotPattern",
    "DecorationStep",
    "DefaultBlockUse",
    "Defines",
    "DefinesValues",
    "DeltaConfig",
    "DensityFunction",
    "DensityFunctionRef",
    "DepthAverageConfig",
    "Dialog",
    "DialogBase",
    "DialogBody",
    "DialogListRef",
    "Difficulty",
    "DifficultyTestEnvironment",
    "Dimension",
    "DimensionPaddingConfig",
    "DimensionType",
    "DimensionTypeEffects",
    "DimensionTypeRef",
    "DirectMultiNoise",
    "DirectPoolAlias",
    "Directory",
    "DiscreteAttribute",
    "DiskConfig",
    "DisplayContext",
    "DistanceMetric",
    "DistancePredicate",
    "DistanceToPoint",
    "DualNoiseProvider",
    "DyeTint",
    "Dyeable",
    "DynamicCustomAction",
    "DynamicDrops",
    "DynamicPoolEntry",
    "DynamicRunCommand",
    "EasingType",
    "EffectsChanged",
    "Element",
    "ElementBase",
    "EmeraldOreConfig",
    "EnchantRandomly",
    "EnchantWithLevels",
    "EnchantedCountBase",
    "EnchantedCountIncrease",
    "EnchantedItem",
    "Enchantment",
    "EnchantmentActiveCheck",
    "EnchantmentCost",
    "EnchantmentEffectComponentMap",
    "EnchantmentLevelProvider",
    "EnchantmentPredicate",
    "EnchantmentProvider",
    "EnchantmentsType",
    "EndCube",
    "EndCubeEffectType",
    "EndGatewayConfig",
    "EndPodiumConfig",
    "EndSpike",
    "EndSpikeConfig",
    "EnterBlock",
    "EntityEffect",
    "EntityEffectsPredicate",
    "EntityEquipmentPredicate",
    "EntityFlagsPredicate",
    "EntityHurtPlayer",
    "EntityKilledPlayer",
    "EntityPredicate",
    "EntityProperties",
    "EntityScores",
    "EntitySlotsPredicate",
    "EntitySubPredicate",
    "EntitySubPredicateMap",
    "EntityTagPredicate",
    "EntityTarget",
    "EntityTypePredicate",
    "EnvironmentAttributeCheck",
    "EnvironmentAttributeMap",
    "EnvironmentAttributeNumberProvider",
    "EnvironmentAttributeTrackMap",
    "EnvironmentScanModifier",
    "Equipment",
    "EquipmentDropsEnchantmentEffect",
    "ExclusionZone",
    "ExplicitTagEntry",
    "ExplodeEntityEffect",
    "ExplorationMap",
    "ExplosionData",
    "ExplosionParticleInfo",
    "ExponentLevelValue",
    "ExponentialEffectValue",
    "FallAfterExplosion",
    "FallFromHeight",
    "FallenTreeConfig",
    "FeatureElement",
    "FeatureRef",
    "FeatureSize",
    "FillLayerConfig",
    "FillPlayerHead",
    "FilledBucket",
    "Filter",
    "FilterPattern",
    "FilterSlotSource",
    "Filtered",
    "FindTopSurface",
    "FireworkExplosions",
    "FireworkShapeIngredients",
    "FireworkTint",
    "FishingHookPredicate",
    "FishingLuckBonusEnchantmentEffect",
    "FishingRodHooked",
    "FishingTimeReductionEnchantmentEffect",
    "Fixed",
    "FixedPlacementModifier",
    "FixedScoreProvider",
    "FixedSizedTarget",
    "Flat",
    "FlatGeneratorLayer",
    "FlatGeneratorPreset",
    "FlatGeneratorSettings",
    "FloatAttribute",
    "FloatAttributeModifier",
    "FloatModifierType",
    "FloatProvider",
    "FloatWithAlpha",
    "FluidPredicate",
    "FluidPredicateState",
    "FoliagePlacer",
    "Font",
    "FontOption",
    "FoodPredicate",
    "ForestRockConfig",
    "FossilConfig",
    "FoxPredicate",
    "FractionLevelValue",
    "FrequencyReductionMethod",
    "FrogPredicate",
    "FrogVariant",
    "FullScreenTarget",
    "FunctionTestEnvironment",
    "FunctionTestInstance",
    "GameMode",
    "GameRuleMap",
    "GameRulesTestEnvironment",
    "GeodeBlockSettings",
    "GeodeConfig",
    "GeodeCrackSettings",
    "GeodeLayerSettings",
    "GlobalEnvironmentAttributeMap",
    "GlyphProvider",
    "GlyphProviderType",
    "GpuWarnlist",
    "Gradient",
    "GrassColorModifier",
    "GrassTint",
    "Gravity",
    "GroupSlotSource",
    "GrowingPlantConfig",
    "GrowingPlantHeight",
    "GuiMeta",
    "GuiSpriteScaling",
    "GuiSpriteScalingType",
    "HangingSign",
    "HangingSignAttachment",
    "HasComponent",
    "HasSturdyFacePredicate",
    "Head",
    "HeadType",
    "HeightFoliagePlacer",
    "HeightMatch",
    "HeightProvider",
    "HeightRangeModifier",
    "HeightRangePredicate",
    "HeightmapConfig",
    "HeightmapModifier",
    "HeightmapType",
    "HitBlockEnchantmentEffect",
    "HoneyHarvestedBlock",
    "HorsePredicate",
    "HugeFungusConfig",
    "HugeMushroomConfig",
    "IcebergConfig",
    "IgniteEntityEffect",
    "Ingredient",
    "IngredientItem",
    "IngredientTag",
    "IngredientValue",
    "InputControl",
    "InputPredicate",
    "InsertListOperation",
    "InsideWorldBoundsPredicate",
    "Instrument",
    "IntGameRule",
    "IntLimiter",
    "IntProvider",
    "IntRange",
    "InternalTarget",
    "InventoryChanged",
    "InventoryChangedSlots",
    "Inverted",
    "InvertedMatch",
    "InvervalSelect",
    "ItemBody",
    "ItemDamageEnchantmentEffect",
    "ItemDefinition",
    "ItemDisplayContext",
    "ItemDurabilityChanged",
    "ItemModel",
    "ItemModeltype",
    "ItemModifier",
    "ItemPoolEntry",
    "ItemPredicate",
    "ItemResult",
    "ItemStackTarget",
    "ItemTransform",
    "ItemUsedOnBlock",
    "Jigsaw",
    "JigsawDistanceLimits",
    "JukeboxSong",
    "KeybindDown",
    "KillMobNearSculkCatalyst",
    "KilledByArrow",
    "KilledByCrossbow",
    "KilledByPlayer",
    "KnockbackEnchantmentEffect",
    "KnockbackModifiers",
    "LakeConfig",
    "Lang",
    "LangDeprecated",
    "LargeDripstoneConfig",
    "Layer",
    "Layers",
    "LeaveVineTreeDecorator",
    "LegacyExplorationMapDestination",
    "LegacyUnicodeProvider",
    "Lerp",
    "LevelBasedValueMap",
    "Levitation",
    "LightningBoltPredicate",
    "LightningStrike",
    "LimitCount",
    "LimitCountSlotSource",
    "LinearLevelValue",
    "LinearPos",
    "LiquidSettings",
    "ListAttribute",
    "ListDialogBase",
    "ListElement",
    "ListModifier",
    "ListModifierType",
    "ListOperation",
    "ListOperationMode",
    "LlamaPredicate",
    "LocalTime",
    "LocationBasedEffect",
    "LocationChangedEnchantmentEffect",
    "LocationCheck",
    "LocationPredicate",
    "LocationPredicateLight",
    "LocationPredicatePosition",
    "LookupLevelValue",
    "LootConditionType",
    "LootContextParamSets",
    "LootEntryType",
    "LootFunctionType",
    "LootPool",
    "LootPoolEntry",
    "LootPoolEntryBase",
    "LootTable",
    "LootTableListRef",
    "LootTablePoolEntry",
    "LootTableRef",
    "LootingEnchant",
    "MainHand",
    "MangroveRootPlacement",
    "MangroveRootPlacer",
    "MapColorTint",
    "MapDecoration",
    "MatchTool",
    "MatchingBiomesPredicate",
    "MatchingBlockTagPredicate",
    "MatchingBlocksPredicate",
    "MatchingFluidsPredicate",
    "MaterialCondition",
    "MaterialConditionRef",
    "MaterialRule",
    "MaterialRuleRef",
    "MegaPineFoliagePlacer",
    "MergeableAttribute",
    "MergeableModifier",
    "MergeableModifierType",
    "MinMaxBounds",
    "Mineshaft",
    "MineshaftType",
    "MipmapStrategy",
    "MobCategory",
    "MobEffectPredicate",
    "MobExperienceEnchantmentEffect",
    "MobSpawnCost",
    "ModelDisplay",
    "ModelElement",
    "ModelElementFace",
    "ModelElementFaceMap",
    "ModelElementRotation",
    "ModelElementRotationBase",
    "ModelOverride",
    "ModelOverridePredicates",
    "ModelRef",
    "ModelTextures",
    "ModelTint",
    "ModelVariant",
    "ModelVariantBase",
    "ModernNetherVegetationConfig",
    "ModernPatchConfig",
    "ModifyContents",
    "MoodSound",
    "MoonBrightnessCheck",
    "MoonPhase",
    "MooshroomPredicate",
    "MovementPredicate",
    "MultiActionDialog",
    "MultiLine",
    "MultiNoise",
    "MultiNoiseBase",
    "MultiNoiseBiomeSourceParameterList",
    "MultiNoisePreset",
    "MultiPartAlternatives",
    "MultiPartAnd",
    "MultiPartCondition",
    "MultifaceBlock",
    "MultifaceGrowthConfig",
    "MultipleAxesModelElementRotation",
    "MultiplyEffectValue",
    "Narration",
    "NarrationPriority",
    "NaturalMobSpawns",
    "NbtContextTarget",
    "NbtProvider",
    "NbtProviderSource",
    "NetherForestVegetationConfig",
    "NetherFossil",
    "NetherTravel",
    "NetherrackReplaceBlobsConfig",
    "NineSlice",
    "NineSliceBorder",
    "NoiseBasedCountModifier",
    "NoiseGeneratorFlags",
    "NoiseGeneratorSettings",
    "NoiseGeneratorSettingsRef",
    "NoiseParameters",
    "NoiseParametersRef",
    "NoiseProvider",
    "NoiseRange",
    "NoiseRouter",
    "NoiseSamplingSettings",
    "NoiseSettings",
    "NoiseSlideSettings",
    "NoiseThresholdCondition",
    "NoiseThresholdCountModifier",
    "NoiseThresholdProvider",
    "NotCondition",
    "NotPredicate",
    "NoticeDialog",
    "Notification",
    "NotificationInfo",
    "NumberDispatcher",
    "NumberProvider",
    "NumberProviderListRef",
    "NumberProviderRef",
    "NumberRangeInput",
    "NumericPropertyType",
    "NumericalEnvironmentAttribute",
    "OceanRuin",
    "OffsetModifier",
    "OldBlendedNoise",
    "OldChatType",
    "OldEntityPredicate",
    "OldPatchConfig",
    "OldRangeConfig",
    "OldSimpleBlockConfig",
    "OldTarget",
    "OldTrimMaterialOverrides",
    "OneArgument",
    "Option",
    "OptionalSimpleBlockConfig",
    "OptionalSmithingIngredients",
    "OreConfig",
    "OreVeinifier",
    "OverlayConfig",
    "OverrideModifier",
    "PaintingPredicate",
    "PaintingVariant",
    "PaleMossTreeDecorator",
    "Palette",
    "PaletteMeta",
    "PaletteRef",
    "PaletteTexture",
    "PalettedPermutations",
    "ParrotPredicate",
    "Particle",
    "ParticlePosition",
    "ParticleVelocity",
    "Pass",
    "PermutationsMap",
    "PigModelType",
    "PigSounds",
    "PigVariant",
    "PineFoliagePlacer",
    "PlaceOnGroundTreeDecorator",
    "PlacedBlock",
    "PlacedFeature",
    "PlacedFeatureListRef",
    "PlacedFeatureRef",
    "PlacementModifier",
    "PlainMessage",
    "PlaySoundEntityEffect",
    "PlayerAdvancementCriteria",
    "PlayerAdvancements",
    "PlayerGeneratesContainerLoot",
    "PlayerHurtEntity",
    "PlayerInteract",
    "PlayerKilledEntity",
    "PlayerPredicate",
    "PlayerRecipes",
    "PlayerTrigger",
    "PoolAlias",
    "PoplarFoliagePlacer",
    "PoplarTrunkPlacer",
    "PosRuleTest",
    "PositionalEnvironmentAttribute",
    "PositionalEnvironmentAttributeMap",
    "PostAttackEnchantmentEffect",
    "PostComponentsItemPredicate",
    "PostEffect",
    "PostPiercingAttackEnchantmentEffect",
    "PotionIngredient",
    "PotionTint",
    "Pow",
    "PreComponentsItemPredicate",
    "Precipitation",
    "Predicate",
    "PredicateListRef",
    "PredicateOffset",
    "PredicateRef",
    "Predicates",
    "ProbabilityConfig",
    "Processor",
    "ProcessorList",
    "ProcessorListObject",
    "ProcessorListRef",
    "ProcessorRule",
    "ProjectedSquareConfig",
    "ProjectileCountEnchantmentEffect",
    "ProjectilePiercingEnchantmentEffect",
    "ProjectileSpawnedEnchantmentEffect",
    "ProjectileSpreadEnchantmentEffect",
    "Projection",
    "ProtectedBlocks",
    "RGBColorAttribute",
    "RabbitPredicate",
    "RaiderPredicate",
    "RandomBlockMatch",
    "RandomBlockStateMatch",
    "RandomBlockStateProvider",
    "RandomBooleanSelector",
    "RandomChance",
    "RandomChanceModifier",
    "RandomChanceWithEnchantedBonus",
    "RandomChanceWithLooting",
    "RandomFeatureEntry",
    "RandomGroupPoolAlias",
    "RandomIntGenerator",
    "RandomIntGeneratorType",
    "RandomNeighborSpreadConfig",
    "RandomOffsetModifier",
    "RandomPatchConfig",
    "RandomPoolAlias",
    "RandomSelector",
    "RandomSpreadFoliagePlacer",
    "RandomSpreadPlacement",
    "RandomValueBounds",
    "RandomizedIntStateProvider",
    "RandomizedPalette",
    "RangeChoice",
    "RangeConfig",
    "RangeDispatch",
    "RangeDispatchEntry",
    "RangeSlotSource",
    "RarityFilter",
    "RarityType",
    "Recipe",
    "RecipeCrafted",
    "RecipeListRef",
    "RecipeUnlocked",
    "RedirectDialog",
    "ReduceBinomialEffectValue",
    "ReferenceProvider",
    "RegionalCompliancies",
    "RepairWithXpEnchantmentEffect",
    "ReplaceBlockEntityEffect",
    "ReplaceDiskEntityEffect",
    "ReplaceSectionListOperation",
    "ReplaceSingleBlockConfig",
    "RequiredConditions",
    "RequiredSmithingIngredients",
    "ResolvableNumber",
    "RideEntityInLava",
    "RootPlacer",
    "RootSystemConfig",
    "RotatedStateProvider",
    "Round",
    "RuinedPortal",
    "RuinedPortalPlacement",
    "RuinedPortalSetup",
    "RuinedPortalType",
    "Rule",
    "RuleBasedBlockStateProvider",
    "RuleTest",
    "RunFunctionEntityEffect",
    "SafelyHarvestHoney",
    "SalmonPredicate",
    "SalmonVariant",
    "Sampler",
    "ScoreNumberProvider",
    "ScoreProvider",
    "SculkPatchConfig",
    "SeaPickleConfig",
    "Select",
    "SelectCase",
    "SelectCases",
    "SelectPropertyType",
    "Sequence",
    "SequenceConfig",
    "SequenceRule",
    "ServerLinksDialog",
    "SetAttributes",
    "SetBannerPattern",
    "SetBlockPropertiesEntityEffect",
    "SetBookCover",
    "SetComponents",
    "SetContents",
    "SetCount",
    "SetCustomData",
    "SetCustomModelData",
    "SetDamage",
    "SetEffectValue",
    "SetEnchantments",
    "SetFireworkExplosion",
    "SetFireworks",
    "SetInstrument",
    "SetItem",
    "SetLootTable",
    "SetLore",
    "SetName",
    "SetNameTarget",
    "SetNbt",
    "SetOminousBottleAmplifier",
    "SetPotion",
    "SetRandomDyes",
    "SetRandomPotion",
    "SetStewEffect",
    "SetWriteableBookPages",
    "SetWrittenBookPages",
    "ShaderProgram",
    "SheepPredicate",
    "ShelfMushroomTreeDecorator",
    "Shift",
    "ShiftedNoise",
    "Shipwreck",
    "ShotCrossbow",
    "ShulkerBox",
    "SimpleBlockConfig",
    "SimpleEasingType",
    "SimpleRandomSelectorConfig",
    "SimpleStateProvider",
    "Single",
    "SingleAxisModelElementRotation",
    "SingleBlockPillarConfig",
    "SingleElement",
    "SingleOptionInput",
    "SingleProvider",
    "SingletonPoolEntry",
    "SkyboxType",
    "Slice",
    "SlideDownBlock",
    "SlimePredicate",
    "SlotSource",
    "SlotsPoolEntry",
    "SmallDripstoneConfig",
    "SmashDamagePerBlockFallenEnchantmentEffect",
    "Smelting",
    "Smithing",
    "SmithingIngredients",
    "SmithingTransform",
    "SmithingTransformResult",
    "SmithingTrim",
    "Sound",
    "SoundEventRef",
    "SoundEventRegistration",
    "SoundSettings",
    "SoundType",
    "SoundVariant",
    "Sounds",
    "SpaceProvider",
    "SpawnCondition",
    "SpawnOverride",
    "SpawnParticlesEntityEffect",
    "SpawnPrioritySelector",
    "SpawnPrioritySelectors",
    "SpawnTargetPoint",
    "SpawnerData",
    "SpawnerDataMap",
    "SpearMobs",
    "Special",
    "SpecialModel",
    "SpecialModelType",
    "SpecificType",
    "SpeleothemClusterConfig",
    "SpeleothemConfig",
    "SpikeConfig",
    "Spline",
    "SplinePoint",
    "SplineType",
    "SpreadType",
    "SpringConfig",
    "SpriteSource",
    "SpriteSourceType",
    "SprucePineFoliagePlacer",
    "SquaredLevelValue",
    "StandingSign",
    "StandingSignAttachment",
    "StatisticPredicate",
    "StewEffect",
    "StoneDepthCondition",
    "Stonecutting",
    "StorageNbtProvider",
    "StorageNumberProvider",
    "Structure",
    "StructureBlock",
    "StructureCheck",
    "StructureEntity",
    "StructureNBT",
    "StructurePlacement",
    "StructureRef",
    "StructureSet",
    "StructureSetElement",
    "StructureSetRef",
    "StructureSettings",
    "SulfurCubeArchetype",
    "SumNumberProvider",
    "SummonEntityEffect",
    "SummonedEntity",
    "SurfaceRelativeThresholdFilter",
    "SurfaceWaterDepthFilter",
    "TableBonus",
    "Tag",
    "TagEntry",
    "TagMatch",
    "TagPoolEntry",
    "TameAnimal",
    "TargetBlock",
    "TargetHit",
    "TargetInput",
    "Targets",
    "TeamTint",
    "TemperatureModifier",
    "TemplateConfig",
    "TemplateEntry",
    "TemplatePool",
    "TerrainAdaptation",
    "TerrainCoordinate",
    "TerrainShaper",
    "TerrainShaperSpline",
    "TestData",
    "TestEnvironment",
    "TestInstance",
    "TextDisplay",
    "TextInput",
    "TextureAnimation",
    "TextureAnimationFrame",
    "TextureInput",
    "TextureMaterial",
    "TextureMeta",
    "TheEnd",
    "ThreeLayersFeatureSize",
    "ThrownItemPickedUpByEntity",
    "ThrownItemPickedUpByPlayer",
    "TickEnchantmentEffect",
    "TileScaling",
    "TilingMode",
    "Time",
    "TimeCheck",
    "TimeMarker",
    "TimeMarkerMap",
    "TimeOfDayTestEnvironment",
    "TimeSource",
    "Timeline",
    "TimelineAttributesTestEnvironment",
    "TintSourceType",
    "ToggleTooltips",
    "ToggleableDataComponent",
    "TradeSet",
    "TranslucentColorAttributeModifier",
    "TrapezoidHeightProvider",
    "TreeConfig",
    "TreeDecorator",
    "TriState",
    "TrialSpawnerConfig",
    "TrickyTrialsStructureConfig",
    "TridentReturnAccelerationEnchantmentEffect",
    "Trigger",
    "TriggerBase",
    "TrimMaterialOverrides",
    "TrimOverride",
    "TrimPattern",
    "TrimPredicate",
    "TropicalFishPredicate",
    "TrunkPlacer",
    "TtfProvider",
    "TwistingVinesConfig",
    "TwoArguments",
    "TwoLayersFeatureSize",
    "TypedSlotSource",
    "UnderwaterMagmaConfig",
    "Uniform",
    "UniformBlocks",
    "UniformBonusFormula",
    "UniformHeightProvider",
    "UniformInt",
    "UniformIntGenerator",
    "UniformIntProvider",
    "UniformNumberProvider",
    "UniformType",
    "UniformValue",
    "UniformValueType",
    "UnihexOverrideRange",
    "UnihexProvider",
    "UnknownStorage",
    "UnobstructedPredicate",
    "Unstitch",
    "UnstitchRegion",
    "UpwardsBranchingTrunkPlacer",
    "UseCycle",
    "UseDuration",
    "UsedEnderEye",
    "UsedTotem",
    "UsingItem",
    "ValueCheck",
    "ValueEffect",
    "VanillaLayered",
    "VegetationPatchConfig",
    "VerticalAnchor",
    "VerticalGradientCondition",
    "ViewEntity",
    "VillagerHatType",
    "VillagerPredicate",
    "VillagerTextureMeta",
    "WaterCondition",
    "WaterDepthThresholdConfig",
    "WaypointStyle",
    "Weather",
    "WeatherCheck",
    "WeatherTestEnvironment",
    "WeightListHeightProvider",
    "WeightedBlockStateProvider",
    "WeightedElement",
    "WeightedModelVariant",
    "WeightedNumberProvider",
    "WeightedRandomFeatureConfig",
    "WeightedSoundEvent",
    "WeirdScaledSampler",
    "WildUpdateStructureConfig",
    "WingsLayer",
    "WolfPredicate",
    "WolfSounds",
    "WolfVariant",
    "WolfVariantAssetInfo",
    "WoodType",
    "WorldPreset",
    "WouldSurvivePredicate",
    "YAboveCondition",
    "YClampedGradient",
    "ZombieNautilusModelType",
    "ZombieNautilusVariant",
]

_EXPORTS = {
    "ARGBColorAttribute": "generated_symbols.data.worldgen.attribute.ARGBColorAttribute",
    "AboveRootPlacement": "generated_symbols.data.worldgen.feature.tree.AboveRootPlacement",
    "ActuallyTranslucentRGB": "generated_symbols.assets.item_definition.ActuallyTranslucentRGB",
    "AddEffectValue": "generated_symbols.data.enchantment.effect.AddEffectValue",
    "Advancement": "generated_symbols.data.advancement.Advancement",
    "AdvancementCriteriaMap": "generated_symbols.data.advancement.AdvancementCriteriaMap",
    "AdvancementCriterion": "generated_symbols.data.advancement.AdvancementCriterion",
    "AdvancementDisplay": "generated_symbols.data.advancement.AdvancementDisplay",
    "AdvancementFrame": "generated_symbols.data.advancement.AdvancementFrame",
    "AdvancementIcon": "generated_symbols.data.advancement.AdvancementIcon",
    "AdvancementPredicateRef": "generated_symbols.data.advancement.trigger.AdvancementPredicateRef",
    "AdvancementRewards": "generated_symbols.data.advancement.AdvancementRewards",
    "AfterAction": "generated_symbols.data.dialog.AfterAction",
    "AllOf": "generated_symbols.data.loot.condition.AllOf",
    "AllOfEffectValue": "generated_symbols.data.enchantment.effect.AllOfEffectValue",
    "AllOfEntityEffect": "generated_symbols.data.enchantment.effect.AllOfEntityEffect",
    "AllOfLocationBasedEffect": "generated_symbols.data.enchantment.effect.AllOfLocationBasedEffect",
    "AllOffTestEnvironment": "generated_symbols.data.gametest.test_environment.AllOffTestEnvironment",
    "AllayDropItemOnBlock": "generated_symbols.data.advancement.trigger.AllayDropItemOnBlock",
    "AlterGroundTreeDecorator": "generated_symbols.data.worldgen.feature.tree.AlterGroundTreeDecorator",
    "Alternative": "generated_symbols.data.loot.condition.Alternative",
    "AmbientParticle": "generated_symbols.data.worldgen.attribute.AmbientParticle",
    "AmbientSounds": "generated_symbols.data.worldgen.attribute.AmbientSounds",
    "AmmoUseEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.AmmoUseEnchantmentEffect",
    "AnyBlockUse": "generated_symbols.data.advancement.trigger.AnyBlockUse",
    "AnyOf": "generated_symbols.data.loot.condition.AnyOf",
    "AppendLoot": "generated_symbols.data.worldgen.processor_list.AppendLoot",
    "AppendStatic": "generated_symbols.data.worldgen.processor_list.AppendStatic",
    "ApplyBonus": "generated_symbols.data.loot.function.ApplyBonus",
    "ApplyBonusFormula": "generated_symbols.data.loot.function.ApplyBonusFormula",
    "ApplyExhaustionEntityEffect": "generated_symbols.data.enchantment.effect.ApplyExhaustionEntityEffect",
    "ApplyImpulseEntityEffect": "generated_symbols.data.enchantment.effect.ApplyImpulseEntityEffect",
    "ApplyMobEffectEntityEffect": "generated_symbols.data.enchantment.effect.ApplyMobEffectEntityEffect",
    "Aquifer": "generated_symbols.data.worldgen.noise_settings.Aquifer",
    "ArmorEffectivenessEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.ArmorEffectivenessEnchantmentEffect",
    "ArmorMaterial": "generated_symbols.data.trim.ArmorMaterial",
    "Atlas": "generated_symbols.assets.atlas.Atlas",
    "AttachedToLeavesTreeDecorator": "generated_symbols.data.worldgen.feature.tree.AttachedToLeavesTreeDecorator",
    "AttachedToLogsTreeDecorator": "generated_symbols.data.worldgen.feature.tree.AttachedToLogsTreeDecorator",
    "AttackTarget": "generated_symbols.data.enchantment.effect_component.AttackTarget",
    "AttributeEffect": "generated_symbols.data.enchantment.effect.AttributeEffect",
    "AttributeEntry": "generated_symbols.data.sulfur_cube_archetype.AttributeEntry",
    "AttributeModifier": "generated_symbols.data.loot.function.AttributeModifier",
    "AttributeTrackBase": "generated_symbols.data.timeline.AttributeTrackBase",
    "AuxTarget": "generated_symbols.assets.shader.post.AuxTarget",
    "AxisAlignedLinearPos": "generated_symbols.data.worldgen.processor_list.AxisAlignedLinearPos",
    "AxolotlPredicate": "generated_symbols.data.advancement.predicate.AxolotlPredicate",
    "BackgroundMusic": "generated_symbols.data.worldgen.attribute.BackgroundMusic",
    "Banner": "generated_symbols.assets.item_definition.Banner",
    "BannerAttachment": "generated_symbols.assets.item_definition.BannerAttachment",
    "BannerPatternLayer": "generated_symbols.data.loot.function.BannerPatternLayer",
    "BaseNoiseProvider": "generated_symbols.data.worldgen.feature.block_state_provider.BaseNoiseProvider",
    "Bed": "generated_symbols.assets.item_definition.Bed",
    "BedPart": "generated_symbols.assets.item_definition.BedPart",
    "BedRule": "generated_symbols.data.worldgen.attribute.BedRule",
    "BedRuleType": "generated_symbols.data.worldgen.attribute.BedRuleType",
    "BeeNestDestroyed": "generated_symbols.data.advancement.trigger.BeeNestDestroyed",
    "BeehiveTreeDecorator": "generated_symbols.data.worldgen.feature.tree.BeehiveTreeDecorator",
    "BendingTrunkPlacer": "generated_symbols.data.worldgen.feature.tree.BendingTrunkPlacer",
    "BinomialIntGenerator": "generated_symbols.data.util.BinomialIntGenerator",
    "BinomialNumberProvider": "generated_symbols.data.number_provider.BinomialNumberProvider",
    "BinomialWithBonusCountFormula": "generated_symbols.data.loot.function.BinomialWithBonusCountFormula",
    "Biome": "generated_symbols.data.worldgen.biome.Biome",
    "BiomeCategory": "generated_symbols.data.worldgen.biome.BiomeCategory",
    "BiomeCheck": "generated_symbols.data.variants.BiomeCheck",
    "BiomeCondition": "generated_symbols.data.worldgen.material_condition.BiomeCondition",
    "BiomeEffects": "generated_symbols.data.worldgen.biome.BiomeEffects",
    "BiomeMusic": "generated_symbols.data.worldgen.biome.BiomeMusic",
    "BiomeNoiseEntry": "generated_symbols.data.worldgen.dimension.biome_source.BiomeNoiseEntry",
    "BiomeParticle": "generated_symbols.data.worldgen.biome.BiomeParticle",
    "BiomeSoundAdditions": "generated_symbols.data.worldgen.biome.BiomeSoundAdditions",
    "BiomeSource": "generated_symbols.data.worldgen.dimension.biome_source.BiomeSource",
    "BiomeTemperature": "generated_symbols.data.worldgen.structure.BiomeTemperature",
    "BitmapProvider": "generated_symbols.assets.font.BitmapProvider",
    "BlendFactor": "generated_symbols.assets.shader.program.BlendFactor",
    "BlendFunc": "generated_symbols.assets.shader.program.BlendFunc",
    "BlendMode": "generated_symbols.assets.shader.program.BlendMode",
    "BlendToGray": "generated_symbols.data.worldgen.attribute.modifier.BlendToGray",
    "BlockAge": "generated_symbols.data.worldgen.processor_list.BlockAge",
    "BlockBasedTestInstance": "generated_symbols.data.gametest.BlockBasedTestInstance",
    "BlockBlobConfig": "generated_symbols.data.worldgen.feature.BlockBlobConfig",
    "BlockColumnConfig": "generated_symbols.data.worldgen.feature.BlockColumnConfig",
    "BlockColumnLayer": "generated_symbols.data.worldgen.feature.BlockColumnLayer",
    "BlockEntityModifier": "generated_symbols.data.worldgen.processor_list.BlockEntityModifier",
    "BlockEntityTarget": "generated_symbols.data.loot.BlockEntityTarget",
    "BlockExperienceEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.BlockExperienceEnchantmentEffect",
    "BlockIgnore": "generated_symbols.data.worldgen.processor_list.BlockIgnore",
    "BlockInteraction": "generated_symbols.data.enchantment.effect.BlockInteraction",
    "BlockMatch": "generated_symbols.data.worldgen.processor_list.BlockMatch",
    "BlockPalette": "generated_symbols.data.structure.BlockPalette",
    "BlockPileConfig": "generated_symbols.data.worldgen.feature.BlockPileConfig",
    "BlockPlacer": "generated_symbols.data.worldgen.feature.BlockPlacer",
    "BlockPredicateFilter": "generated_symbols.data.worldgen.feature.placement.BlockPredicateFilter",
    "BlockPredicateState": "generated_symbols.data.advancement.predicate.BlockPredicateState",
    "BlockRot": "generated_symbols.data.worldgen.processor_list.BlockRot",
    "BlockRule": "generated_symbols.data.worldgen.material_rule.BlockRule",
    "BlockState": "generated_symbols.assets.item_definition.BlockState",
    "BlockStateDefinition": "generated_symbols.assets.block_state_definition.BlockStateDefinition",
    "BlockStateDefinitionMultipart": "generated_symbols.assets.block_state_definition.BlockStateDefinitionMultipart",
    "BlockStateDefinitionMultipartEntry": "generated_symbols.assets.block_state_definition.BlockStateDefinitionMultipartEntry",
    "BlockStateDefinitionVariant": "generated_symbols.assets.block_state_definition.BlockStateDefinitionVariant",
    "BlockStateDefinitionVariantMap": "generated_symbols.assets.block_state_definition.BlockStateDefinitionVariantMap",
    "BlockStateMatch": "generated_symbols.data.worldgen.processor_list.BlockStateMatch",
    "BlockStateProperty": "generated_symbols.data.loot.condition.BlockStateProperty",
    "BlockStateProvider": "generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider",
    "BlockStateRuleProviderEntry": "generated_symbols.data.worldgen.feature.BlockStateRuleProviderEntry",
    "BoatPredicate": "generated_symbols.data.advancement.predicate.BoatPredicate",
    "Book": "generated_symbols.assets.item_definition.Book",
    "BoolGameRule": "generated_symbols.data.gametest.test_environment.BoolGameRule",
    "BooleanAttribute": "generated_symbols.data.worldgen.attribute.BooleanAttribute",
    "BooleanAttributeModifier": "generated_symbols.data.worldgen.attribute.modifier.BooleanAttributeModifier",
    "BooleanInput": "generated_symbols.data.dialog.input.BooleanInput",
    "BooleanModifierType": "generated_symbols.data.worldgen.attribute.modifier.BooleanModifierType",
    "BottomBiasHeightProvider": "generated_symbols.data.worldgen.BottomBiasHeightProvider",
    "BoundingBox": "generated_symbols.data.worldgen.structure.BoundingBox",
    "BredAnimals": "generated_symbols.data.advancement.trigger.BredAnimals",
    "BrewedPotion": "generated_symbols.data.advancement.trigger.BrewedPotion",
    "Brewing": "generated_symbols.data.recipe.Brewing",
    "BuriedTreasure": "generated_symbols.data.worldgen.structure.BuriedTreasure",
    "Button": "generated_symbols.data.dialog.Button",
    "ButtonListDialogBase": "generated_symbols.data.dialog.ButtonListDialogBase",
    "ByCostEnchantmentProvider": "generated_symbols.data.enchantment.provider.ByCostEnchantmentProvider",
    "ByCostWithDifficultyEnchantmentProvider": "generated_symbols.data.enchantment.provider.ByCostWithDifficultyEnchantmentProvider",
    "CanyonConfig": "generated_symbols.data.worldgen.carver.CanyonConfig",
    "CanyonShape": "generated_symbols.data.worldgen.carver.CanyonShape",
    "Capped": "generated_symbols.data.worldgen.processor_list.Capped",
    "CardinalLightType": "generated_symbols.data.worldgen.dimension.CardinalLightType",
    "CarveStep": "generated_symbols.data.worldgen.CarveStep",
    "CarverConfigBase": "generated_symbols.data.worldgen.carver.CarverConfigBase",
    "CarverDebugSettings": "generated_symbols.data.worldgen.carver.CarverDebugSettings",
    "CarverListRef": "generated_symbols.data.worldgen.carver.CarverListRef",
    "CarverRef": "generated_symbols.data.worldgen.carver.CarverRef",
    "CarversPerStep": "generated_symbols.data.worldgen.biome.CarversPerStep",
    "CarvingMaskConfig": "generated_symbols.data.worldgen.feature.decorator.CarvingMaskConfig",
    "CarvingMaskModifier": "generated_symbols.data.worldgen.feature.placement.CarvingMaskModifier",
    "CatPredicate": "generated_symbols.data.advancement.predicate.CatPredicate",
    "CatSounds": "generated_symbols.data.variants.cat.CatSounds",
    "CatVariant": "generated_symbols.data.variants.cat.CatVariant",
    "CaveConfig": "generated_symbols.data.worldgen.carver.CaveConfig",
    "ChanceConfig": "generated_symbols.data.worldgen.feature.decorator.ChanceConfig",
    "ChangeItemDamageEffect": "generated_symbols.data.enchantment.effect.ChangeItemDamageEffect",
    "ChangedDimension": "generated_symbols.data.advancement.trigger.ChangedDimension",
    "ChanneledLightning": "generated_symbols.data.advancement.trigger.ChanneledLightning",
    "ChargeType": "generated_symbols.assets.item_definition.ChargeType",
    "ChatDecoration": "generated_symbols.data.chat_type.ChatDecoration",
    "ChatDecorationParameter": "generated_symbols.data.chat_type.ChatDecorationParameter",
    "ChatType": "generated_symbols.data.chat_type.ChatType",
    "Checkerboard": "generated_symbols.data.worldgen.dimension.biome_source.Checkerboard",
    "CherryFoliagePlacer": "generated_symbols.data.worldgen.feature.tree.CherryFoliagePlacer",
    "CherryTrunkPlacer": "generated_symbols.data.worldgen.feature.tree.CherryTrunkPlacer",
    "Chest": "generated_symbols.assets.item_definition.Chest",
    "ChestType": "generated_symbols.assets.item_definition.ChestType",
    "ChickenModelType": "generated_symbols.data.variants.chicken.ChickenModelType",
    "ChickenSounds": "generated_symbols.data.variants.chicken.ChickenSounds",
    "ChickenVariant": "generated_symbols.data.variants.chicken.ChickenVariant",
    "ChunkGenerator": "generated_symbols.data.worldgen.dimension.chunk_generator.ChunkGenerator",
    "Clamp": "generated_symbols.data.worldgen.density_function.Clamp",
    "ClampedIntProvider": "generated_symbols.data.worldgen.ClampedIntProvider",
    "ClampedLevelValue": "generated_symbols.data.enchantment.level_based_value.ClampedLevelValue",
    "ClampedNormalIntProvider": "generated_symbols.data.worldgen.ClampedNormalIntProvider",
    "ClickAction": "generated_symbols.data.dialog.action.ClickAction",
    "ClimateParameter": "generated_symbols.data.worldgen.dimension.biome_source.ClimateParameter",
    "ClimateParameters": "generated_symbols.data.worldgen.dimension.biome_source.ClimateParameters",
    "ClockTimeTestEnvironment": "generated_symbols.data.gametest.test_environment.ClockTimeTestEnvironment",
    "CocoaTreeDecorator": "generated_symbols.data.worldgen.feature.tree.CocoaTreeDecorator",
    "Code": "generated_symbols.assets.regional_compliancies.Code",
    "ColorAttributeModifier": "generated_symbols.data.worldgen.attribute.modifier.ColorAttributeModifier",
    "ColorModifierType": "generated_symbols.data.worldgen.attribute.modifier.ColorModifierType",
    "ColormapTextureMeta": "generated_symbols.assets.texture_meta.ColormapTextureMeta",
    "ColumnPlacer": "generated_symbols.data.worldgen.feature.ColumnPlacer",
    "ColumnsConfig": "generated_symbols.data.worldgen.feature.ColumnsConfig",
    "CombiningPredicate": "generated_symbols.data.worldgen.feature.block_predicate.CombiningPredicate",
    "Compass": "generated_symbols.assets.item_definition.Compass",
    "CompassTarget": "generated_symbols.assets.item_definition.CompassTarget",
    "ComponentFlags": "generated_symbols.assets.item_definition.ComponentFlags",
    "ComponentStrings": "generated_symbols.assets.item_definition.ComponentStrings",
    "Composite": "generated_symbols.assets.item_definition.Composite",
    "CompositeEntity": "generated_symbols.data.advancement.trigger.CompositeEntity",
    "CompositeMatch": "generated_symbols.data.worldgen.processor_list.CompositeMatch",
    "CompositePoolEntry": "generated_symbols.data.loot.CompositePoolEntry",
    "ConcentricRingsPlacement": "generated_symbols.data.worldgen.structure_set.ConcentricRingsPlacement",
    "Condition": "generated_symbols.assets.item_definition.Condition",
    "ConditionRule": "generated_symbols.data.worldgen.material_rule.ConditionRule",
    "ConditionalNumberProvider": "generated_symbols.data.number_provider.ConditionalNumberProvider",
    "ConditionalPropertyType": "generated_symbols.assets.item_definition.ConditionalPropertyType",
    "Config": "generated_symbols.data.worldgen.surface_builder.Config",
    "ConfiguredCarver": "generated_symbols.data.worldgen.carver.ConfiguredCarver",
    "ConfiguredDecorator": "generated_symbols.data.worldgen.feature.decorator.ConfiguredDecorator",
    "ConfiguredFeature": "generated_symbols.data.worldgen.feature.ConfiguredFeature",
    "ConfiguredFeatureRef": "generated_symbols.data.worldgen.feature.ConfiguredFeatureRef",
    "ConfiguredSurfaceBuilder": "generated_symbols.data.worldgen.surface_builder.ConfiguredSurfaceBuilder",
    "ConfiguredSurfaceBuilderRef": "generated_symbols.data.worldgen.surface_builder.ConfiguredSurfaceBuilderRef",
    "ConfirmationDialog": "generated_symbols.data.dialog.ConfirmationDialog",
    "Constant": "generated_symbols.data.worldgen.density_function.Constant",
    "ConstantHeightProvider": "generated_symbols.data.worldgen.ConstantHeightProvider",
    "ConstantIntGenerator": "generated_symbols.data.util.ConstantIntGenerator",
    "ConstantIntProvider": "generated_symbols.data.worldgen.ConstantIntProvider",
    "ConstantNumberProvider": "generated_symbols.data.number_provider.ConstantNumberProvider",
    "ConstantTint": "generated_symbols.assets.item_definition.ConstantTint",
    "ConstructBeacon": "generated_symbols.data.advancement.trigger.ConstructBeacon",
    "ConsumeItem": "generated_symbols.data.advancement.trigger.ConsumeItem",
    "ContactDamage": "generated_symbols.data.sulfur_cube_archetype.ContactDamage",
    "ContainerComponents": "generated_symbols.data.loot.function.ContainerComponents",
    "ContentsSlotSource": "generated_symbols.data.slot_source.ContentsSlotSource",
    "ContextDimension": "generated_symbols.assets.item_definition.ContextDimension",
    "ContextEntityType": "generated_symbols.assets.item_definition.ContextEntityType",
    "ContextNbtProvider": "generated_symbols.data.util.ContextNbtProvider",
    "ContextScoreProvider": "generated_symbols.data.util.ContextScoreProvider",
    "CookingBookCategory": "generated_symbols.data.recipe.CookingBookCategory",
    "CookingBookInfo": "generated_symbols.data.recipe.CookingBookInfo",
    "CopperGolemStatue": "generated_symbols.assets.item_definition.CopperGolemStatue",
    "CopperGolemStatuePose": "generated_symbols.assets.item_definition.CopperGolemStatuePose",
    "CopyComponents": "generated_symbols.data.loot.function.CopyComponents",
    "CopyName": "generated_symbols.data.loot.function.CopyName",
    "CopyNameSource": "generated_symbols.data.loot.function.CopyNameSource",
    "CopyNbt": "generated_symbols.data.loot.function.CopyNbt",
    "CopyNbtOperation": "generated_symbols.data.loot.function.CopyNbtOperation",
    "CopyNbtStrategy": "generated_symbols.data.loot.function.CopyNbtStrategy",
    "CopyPropertiesProvider": "generated_symbols.data.worldgen.feature.block_state_provider.CopyPropertiesProvider",
    "CopyState": "generated_symbols.data.loot.function.CopyState",
    "CoralConfig": "generated_symbols.data.worldgen.feature.CoralConfig",
    "Count": "generated_symbols.assets.item_definition.Count",
    "CountConfig": "generated_symbols.data.worldgen.feature.decorator.CountConfig",
    "CountExtraConfig": "generated_symbols.data.worldgen.feature.decorator.CountExtraConfig",
    "CountModifier": "generated_symbols.data.worldgen.feature.placement.CountModifier",
    "CountNoiseBiasedConfig": "generated_symbols.data.worldgen.feature.decorator.CountNoiseBiasedConfig",
    "CountNoiseConfig": "generated_symbols.data.worldgen.feature.decorator.CountNoiseConfig",
    "CountOnEveryLayerModifier": "generated_symbols.data.worldgen.feature.placement.CountOnEveryLayerModifier",
    "CowModelType": "generated_symbols.data.variants.cow.CowModelType",
    "CowSounds": "generated_symbols.data.variants.cow.CowSounds",
    "CowVariant": "generated_symbols.data.variants.cow.CowVariant",
    "CraftingBookCategory": "generated_symbols.data.recipe.CraftingBookCategory",
    "CraftingBookInfo": "generated_symbols.data.recipe.CraftingBookInfo",
    "CraftingDecoratedPot": "generated_symbols.data.recipe.CraftingDecoratedPot",
    "CraftingDye": "generated_symbols.data.recipe.CraftingDye",
    "CraftingImbue": "generated_symbols.data.recipe.CraftingImbue",
    "CraftingIngredients": "generated_symbols.data.recipe.CraftingIngredients",
    "CraftingShaped": "generated_symbols.data.recipe.CraftingShaped",
    "CraftingShapeless": "generated_symbols.data.recipe.CraftingShapeless",
    "CraftingSpecialBannerDuplicate": "generated_symbols.data.recipe.CraftingSpecialBannerDuplicate",
    "CraftingSpecialBookCloning": "generated_symbols.data.recipe.CraftingSpecialBookCloning",
    "CraftingSpecialFireworkRocket": "generated_symbols.data.recipe.CraftingSpecialFireworkRocket",
    "CraftingSpecialFireworkStar": "generated_symbols.data.recipe.CraftingSpecialFireworkStar",
    "CraftingSpecialFireworkStarFade": "generated_symbols.data.recipe.CraftingSpecialFireworkStarFade",
    "CraftingSpecialMapExtending": "generated_symbols.data.recipe.CraftingSpecialMapExtending",
    "CraftingSpecialShieldDecoration": "generated_symbols.data.recipe.CraftingSpecialShieldDecoration",
    "CraftingTransmute": "generated_symbols.data.recipe.CraftingTransmute",
    "CreakingHeartTreeDecorator": "generated_symbols.data.worldgen.feature.tree.CreakingHeartTreeDecorator",
    "Credits": "generated_symbols.assets.credits.Credits",
    "CreditsCompanySegment": "generated_symbols.assets.credits.CreditsCompanySegment",
    "CreditsDiscipline": "generated_symbols.assets.credits.CreditsDiscipline",
    "CreditsJobTitle": "generated_symbols.assets.credits.CreditsJobTitle",
    "CrossbowChargeSoundsEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.CrossbowChargeSoundsEnchantmentEffect",
    "CrossbowChargeType": "generated_symbols.assets.item_definition.CrossbowChargeType",
    "CubicBezierEase": "generated_symbols.data.timeline.CubicBezierEase",
    "CubicSpline": "generated_symbols.data.worldgen.density_function.CubicSpline",
    "CuboidModifier": "generated_symbols.data.worldgen.feature.placement.CuboidModifier",
    "CuredZombieVillager": "generated_symbols.data.advancement.trigger.CuredZombieVillager",
    "CustomModelDataColors": "generated_symbols.data.loot.function.CustomModelDataColors",
    "CustomModelDataTint": "generated_symbols.assets.item_definition.CustomModelDataTint",
    "CustomizableItemDisplayContext": "generated_symbols.assets.model.CustomizableItemDisplayContext",
    "Damage": "generated_symbols.assets.item_definition.Damage",
    "DamageEffects": "generated_symbols.data.damage_type.DamageEffects",
    "DamageEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.DamageEnchantmentEffect",
    "DamageEntityEffect": "generated_symbols.data.enchantment.effect.DamageEntityEffect",
    "DamageImmunityEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.DamageImmunityEnchantmentEffect",
    "DamageItemEffect": "generated_symbols.data.enchantment.effect.DamageItemEffect",
    "DamagePredicate": "generated_symbols.data.advancement.predicate.DamagePredicate",
    "DamageProtectionEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.DamageProtectionEnchantmentEffect",
    "DamageScaling": "generated_symbols.data.damage_type.DamageScaling",
    "DamageSourceFlags": "generated_symbols.data.advancement.predicate.DamageSourceFlags",
    "DamageSourcePredicate": "generated_symbols.data.advancement.predicate.DamageSourcePredicate",
    "DamageSourceProperties": "generated_symbols.data.loot.condition.DamageSourceProperties",
    "DamageTagPredicate": "generated_symbols.data.advancement.predicate.DamageTagPredicate",
    "DamageType": "generated_symbols.data.damage_type.DamageType",
    "DeathMessageType": "generated_symbols.data.damage_type.DeathMessageType",
    "DecoratedPotPattern": "generated_symbols.data.decorated_pot_pattern.DecoratedPotPattern",
    "DecorationStep": "generated_symbols.data.worldgen.DecorationStep",
    "DefaultBlockUse": "generated_symbols.data.advancement.trigger.DefaultBlockUse",
    "Defines": "generated_symbols.assets.shader.program.Defines",
    "DefinesValues": "generated_symbols.assets.shader.program.DefinesValues",
    "DeltaConfig": "generated_symbols.data.worldgen.feature.DeltaConfig",
    "DensityFunction": "generated_symbols.data.worldgen.density_function.DensityFunction",
    "DensityFunctionRef": "generated_symbols.data.worldgen.density_function.DensityFunctionRef",
    "DepthAverageConfig": "generated_symbols.data.worldgen.feature.decorator.DepthAverageConfig",
    "Dialog": "generated_symbols.data.dialog.Dialog",
    "DialogBase": "generated_symbols.data.dialog.DialogBase",
    "DialogBody": "generated_symbols.data.dialog.body.DialogBody",
    "DialogListRef": "generated_symbols.data.dialog.DialogListRef",
    "Difficulty": "generated_symbols.data.gametest.test_environment.Difficulty",
    "DifficultyTestEnvironment": "generated_symbols.data.gametest.test_environment.DifficultyTestEnvironment",
    "Dimension": "generated_symbols.data.worldgen.dimension.Dimension",
    "DimensionPaddingConfig": "generated_symbols.data.worldgen.structure.DimensionPaddingConfig",
    "DimensionType": "generated_symbols.data.worldgen.dimension.DimensionType",
    "DimensionTypeEffects": "generated_symbols.data.worldgen.dimension.DimensionTypeEffects",
    "DimensionTypeRef": "generated_symbols.data.worldgen.dimension.DimensionTypeRef",
    "DirectMultiNoise": "generated_symbols.data.worldgen.dimension.biome_source.DirectMultiNoise",
    "DirectPoolAlias": "generated_symbols.data.worldgen.structure.DirectPoolAlias",
    "Directory": "generated_symbols.assets.atlas.Directory",
    "DiscreteAttribute": "generated_symbols.data.worldgen.attribute.DiscreteAttribute",
    "DiskConfig": "generated_symbols.data.worldgen.feature.DiskConfig",
    "DisplayContext": "generated_symbols.assets.item_definition.DisplayContext",
    "DistanceMetric": "generated_symbols.data.worldgen.density_function.DistanceMetric",
    "DistancePredicate": "generated_symbols.data.advancement.predicate.DistancePredicate",
    "DistanceToPoint": "generated_symbols.data.worldgen.density_function.DistanceToPoint",
    "DualNoiseProvider": "generated_symbols.data.worldgen.feature.block_state_provider.DualNoiseProvider",
    "DyeTint": "generated_symbols.assets.item_definition.DyeTint",
    "Dyeable": "generated_symbols.assets.equipment.Dyeable",
    "DynamicCustomAction": "generated_symbols.data.dialog.action.DynamicCustomAction",
    "DynamicDrops": "generated_symbols.data.loot.DynamicDrops",
    "DynamicPoolEntry": "generated_symbols.data.loot.DynamicPoolEntry",
    "DynamicRunCommand": "generated_symbols.data.dialog.action.DynamicRunCommand",
    "EasingType": "generated_symbols.data.timeline.EasingType",
    "EffectsChanged": "generated_symbols.data.advancement.trigger.EffectsChanged",
    "Element": "generated_symbols.data.worldgen.template_pool.Element",
    "ElementBase": "generated_symbols.data.worldgen.template_pool.ElementBase",
    "EmeraldOreConfig": "generated_symbols.data.worldgen.feature.EmeraldOreConfig",
    "EnchantRandomly": "generated_symbols.data.loot.function.EnchantRandomly",
    "EnchantWithLevels": "generated_symbols.data.loot.function.EnchantWithLevels",
    "EnchantedCountBase": "generated_symbols.data.loot.function.EnchantedCountBase",
    "EnchantedCountIncrease": "generated_symbols.data.loot.function.EnchantedCountIncrease",
    "EnchantedItem": "generated_symbols.data.advancement.trigger.EnchantedItem",
    "Enchantment": "generated_symbols.data.enchantment.Enchantment",
    "EnchantmentActiveCheck": "generated_symbols.data.loot.condition.EnchantmentActiveCheck",
    "EnchantmentCost": "generated_symbols.data.enchantment.EnchantmentCost",
    "EnchantmentEffectComponentMap": "generated_symbols.data.enchantment.effect_component.EnchantmentEffectComponentMap",
    "EnchantmentLevelProvider": "generated_symbols.data.number_provider.EnchantmentLevelProvider",
    "EnchantmentPredicate": "generated_symbols.data.advancement.predicate.EnchantmentPredicate",
    "EnchantmentProvider": "generated_symbols.data.enchantment.provider.EnchantmentProvider",
    "EnchantmentsType": "generated_symbols.data.enchantment.provider.EnchantmentsType",
    "EndCube": "generated_symbols.assets.item_definition.EndCube",
    "EndCubeEffectType": "generated_symbols.assets.item_definition.EndCubeEffectType",
    "EndGatewayConfig": "generated_symbols.data.worldgen.feature.EndGatewayConfig",
    "EndPodiumConfig": "generated_symbols.data.worldgen.feature.EndPodiumConfig",
    "EndSpike": "generated_symbols.data.worldgen.feature.EndSpike",
    "EndSpikeConfig": "generated_symbols.data.worldgen.feature.EndSpikeConfig",
    "EnterBlock": "generated_symbols.data.advancement.trigger.EnterBlock",
    "EntityEffect": "generated_symbols.data.enchantment.effect.EntityEffect",
    "EntityEffectsPredicate": "generated_symbols.data.advancement.predicate.EntityEffectsPredicate",
    "EntityEquipmentPredicate": "generated_symbols.data.advancement.predicate.EntityEquipmentPredicate",
    "EntityFlagsPredicate": "generated_symbols.data.advancement.predicate.EntityFlagsPredicate",
    "EntityHurtPlayer": "generated_symbols.data.advancement.trigger.EntityHurtPlayer",
    "EntityKilledPlayer": "generated_symbols.data.advancement.trigger.EntityKilledPlayer",
    "EntityPredicate": "generated_symbols.data.advancement.predicate.EntityPredicate",
    "EntityProperties": "generated_symbols.data.loot.condition.EntityProperties",
    "EntityScores": "generated_symbols.data.loot.condition.EntityScores",
    "EntitySlotsPredicate": "generated_symbols.data.advancement.predicate.EntitySlotsPredicate",
    "EntitySubPredicate": "generated_symbols.data.advancement.predicate.EntitySubPredicate",
    "EntitySubPredicateMap": "generated_symbols.data.advancement.predicate.EntitySubPredicateMap",
    "EntityTagPredicate": "generated_symbols.data.advancement.predicate.EntityTagPredicate",
    "EntityTarget": "generated_symbols.data.loot.EntityTarget",
    "EntityTypePredicate": "generated_symbols.data.advancement.predicate.EntityTypePredicate",
    "EnvironmentAttributeCheck": "generated_symbols.data.loot.condition.EnvironmentAttributeCheck",
    "EnvironmentAttributeMap": "generated_symbols.data.worldgen.attribute.EnvironmentAttributeMap",
    "EnvironmentAttributeNumberProvider": "generated_symbols.data.number_provider.EnvironmentAttributeNumberProvider",
    "EnvironmentAttributeTrackMap": "generated_symbols.data.timeline.EnvironmentAttributeTrackMap",
    "EnvironmentScanModifier": "generated_symbols.data.worldgen.feature.placement.EnvironmentScanModifier",
    "Equipment": "generated_symbols.assets.equipment.Equipment",
    "EquipmentDropsEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.EquipmentDropsEnchantmentEffect",
    "ExclusionZone": "generated_symbols.data.worldgen.structure_set.ExclusionZone",
    "ExplicitTagEntry": "generated_symbols.data.tag.ExplicitTagEntry",
    "ExplodeEntityEffect": "generated_symbols.data.enchantment.effect.ExplodeEntityEffect",
    "ExplorationMap": "generated_symbols.data.loot.function.ExplorationMap",
    "ExplosionData": "generated_symbols.data.sulfur_cube_archetype.ExplosionData",
    "ExplosionParticleInfo": "generated_symbols.data.enchantment.effect.ExplosionParticleInfo",
    "ExponentLevelValue": "generated_symbols.data.enchantment.level_based_value.ExponentLevelValue",
    "ExponentialEffectValue": "generated_symbols.data.enchantment.effect.ExponentialEffectValue",
    "FallAfterExplosion": "generated_symbols.data.advancement.trigger.FallAfterExplosion",
    "FallFromHeight": "generated_symbols.data.advancement.trigger.FallFromHeight",
    "FallenTreeConfig": "generated_symbols.data.worldgen.feature.tree.FallenTreeConfig",
    "FeatureElement": "generated_symbols.data.worldgen.template_pool.FeatureElement",
    "FeatureRef": "generated_symbols.data.worldgen.feature.FeatureRef",
    "FeatureSize": "generated_symbols.data.worldgen.feature.tree.FeatureSize",
    "FillLayerConfig": "generated_symbols.data.worldgen.feature.FillLayerConfig",
    "FillPlayerHead": "generated_symbols.data.loot.function.FillPlayerHead",
    "FilledBucket": "generated_symbols.data.advancement.trigger.FilledBucket",
    "Filter": "generated_symbols.assets.atlas.Filter",
    "FilterPattern": "generated_symbols.assets.atlas.FilterPattern",
    "FilterSlotSource": "generated_symbols.data.slot_source.FilterSlotSource",
    "Filtered": "generated_symbols.data.loot.function.Filtered",
    "FindTopSurface": "generated_symbols.data.worldgen.density_function.FindTopSurface",
    "FireworkExplosions": "generated_symbols.data.loot.function.FireworkExplosions",
    "FireworkShapeIngredients": "generated_symbols.data.recipe.FireworkShapeIngredients",
    "FireworkTint": "generated_symbols.assets.item_definition.FireworkTint",
    "FishingHookPredicate": "generated_symbols.data.advancement.predicate.FishingHookPredicate",
    "FishingLuckBonusEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.FishingLuckBonusEnchantmentEffect",
    "FishingRodHooked": "generated_symbols.data.advancement.trigger.FishingRodHooked",
    "FishingTimeReductionEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.FishingTimeReductionEnchantmentEffect",
    "Fixed": "generated_symbols.data.worldgen.dimension.biome_source.Fixed",
    "FixedPlacementModifier": "generated_symbols.data.worldgen.feature.placement.FixedPlacementModifier",
    "FixedScoreProvider": "generated_symbols.data.util.FixedScoreProvider",
    "FixedSizedTarget": "generated_symbols.assets.shader.post.FixedSizedTarget",
    "Flat": "generated_symbols.data.worldgen.dimension.chunk_generator.Flat",
    "FlatGeneratorLayer": "generated_symbols.data.worldgen.dimension.chunk_generator.FlatGeneratorLayer",
    "FlatGeneratorPreset": "generated_symbols.data.worldgen.world_preset.FlatGeneratorPreset",
    "FlatGeneratorSettings": "generated_symbols.data.worldgen.dimension.chunk_generator.FlatGeneratorSettings",
    "FloatAttribute": "generated_symbols.data.worldgen.attribute.FloatAttribute",
    "FloatAttributeModifier": "generated_symbols.data.worldgen.attribute.modifier.FloatAttributeModifier",
    "FloatModifierType": "generated_symbols.data.worldgen.attribute.modifier.FloatModifierType",
    "FloatProvider": "generated_symbols.data.worldgen.FloatProvider",
    "FloatWithAlpha": "generated_symbols.data.worldgen.attribute.modifier.FloatWithAlpha",
    "FluidPredicate": "generated_symbols.data.advancement.predicate.FluidPredicate",
    "FluidPredicateState": "generated_symbols.data.advancement.predicate.FluidPredicateState",
    "FoliagePlacer": "generated_symbols.data.worldgen.feature.tree.FoliagePlacer",
    "Font": "generated_symbols.assets.font.Font",
    "FontOption": "generated_symbols.assets.font.FontOption",
    "FoodPredicate": "generated_symbols.data.advancement.predicate.FoodPredicate",
    "ForestRockConfig": "generated_symbols.data.worldgen.feature.ForestRockConfig",
    "FossilConfig": "generated_symbols.data.worldgen.feature.FossilConfig",
    "FoxPredicate": "generated_symbols.data.advancement.predicate.FoxPredicate",
    "FractionLevelValue": "generated_symbols.data.enchantment.level_based_value.FractionLevelValue",
    "FrequencyReductionMethod": "generated_symbols.data.worldgen.structure_set.FrequencyReductionMethod",
    "FrogPredicate": "generated_symbols.data.advancement.predicate.FrogPredicate",
    "FrogVariant": "generated_symbols.data.variants.frog.FrogVariant",
    "FullScreenTarget": "generated_symbols.assets.shader.post.FullScreenTarget",
    "FunctionTestEnvironment": "generated_symbols.data.gametest.test_environment.FunctionTestEnvironment",
    "FunctionTestInstance": "generated_symbols.data.gametest.FunctionTestInstance",
    "GameMode": "generated_symbols.data.advancement.predicate.GameMode",
    "GameRuleMap": "generated_symbols.data.gametest.test_environment.GameRuleMap",
    "GameRulesTestEnvironment": "generated_symbols.data.gametest.test_environment.GameRulesTestEnvironment",
    "GeodeBlockSettings": "generated_symbols.data.worldgen.feature.GeodeBlockSettings",
    "GeodeConfig": "generated_symbols.data.worldgen.feature.GeodeConfig",
    "GeodeCrackSettings": "generated_symbols.data.worldgen.feature.GeodeCrackSettings",
    "GeodeLayerSettings": "generated_symbols.data.worldgen.feature.GeodeLayerSettings",
    "GlobalEnvironmentAttributeMap": "generated_symbols.data.worldgen.attribute.GlobalEnvironmentAttributeMap",
    "GlyphProvider": "generated_symbols.assets.font.GlyphProvider",
    "GlyphProviderType": "generated_symbols.assets.font.GlyphProviderType",
    "GpuWarnlist": "generated_symbols.assets.gpu_warnlist.GpuWarnlist",
    "Gradient": "generated_symbols.data.worldgen.density_function.Gradient",
    "GrassColorModifier": "generated_symbols.data.worldgen.biome.GrassColorModifier",
    "GrassTint": "generated_symbols.assets.item_definition.GrassTint",
    "Gravity": "generated_symbols.data.worldgen.processor_list.Gravity",
    "GroupSlotSource": "generated_symbols.data.slot_source.GroupSlotSource",
    "GrowingPlantConfig": "generated_symbols.data.worldgen.feature.GrowingPlantConfig",
    "GrowingPlantHeight": "generated_symbols.data.worldgen.feature.GrowingPlantHeight",
    "GuiMeta": "generated_symbols.assets.texture_meta.GuiMeta",
    "GuiSpriteScaling": "generated_symbols.assets.texture_meta.GuiSpriteScaling",
    "GuiSpriteScalingType": "generated_symbols.assets.texture_meta.GuiSpriteScalingType",
    "HangingSign": "generated_symbols.assets.item_definition.HangingSign",
    "HangingSignAttachment": "generated_symbols.assets.item_definition.HangingSignAttachment",
    "HasComponent": "generated_symbols.assets.item_definition.HasComponent",
    "HasSturdyFacePredicate": "generated_symbols.data.worldgen.feature.block_predicate.HasSturdyFacePredicate",
    "Head": "generated_symbols.assets.item_definition.Head",
    "HeadType": "generated_symbols.assets.item_definition.HeadType",
    "HeightFoliagePlacer": "generated_symbols.data.worldgen.feature.tree.HeightFoliagePlacer",
    "HeightMatch": "generated_symbols.data.worldgen.processor_list.HeightMatch",
    "HeightProvider": "generated_symbols.data.worldgen.HeightProvider",
    "HeightRangeModifier": "generated_symbols.data.worldgen.feature.placement.HeightRangeModifier",
    "HeightRangePredicate": "generated_symbols.data.worldgen.feature.block_predicate.HeightRangePredicate",
    "HeightmapConfig": "generated_symbols.data.worldgen.feature.decorator.HeightmapConfig",
    "HeightmapModifier": "generated_symbols.data.worldgen.feature.placement.HeightmapModifier",
    "HeightmapType": "generated_symbols.data.worldgen.HeightmapType",
    "HitBlockEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.HitBlockEnchantmentEffect",
    "HoneyHarvestedBlock": "generated_symbols.data.advancement.trigger.HoneyHarvestedBlock",
    "HorsePredicate": "generated_symbols.data.advancement.predicate.HorsePredicate",
    "HugeFungusConfig": "generated_symbols.data.worldgen.feature.HugeFungusConfig",
    "HugeMushroomConfig": "generated_symbols.data.worldgen.feature.HugeMushroomConfig",
    "IcebergConfig": "generated_symbols.data.worldgen.feature.IcebergConfig",
    "IgniteEntityEffect": "generated_symbols.data.enchantment.effect.IgniteEntityEffect",
    "Ingredient": "generated_symbols.data.recipe.Ingredient",
    "IngredientItem": "generated_symbols.data.recipe.IngredientItem",
    "IngredientTag": "generated_symbols.data.recipe.IngredientTag",
    "IngredientValue": "generated_symbols.data.recipe.IngredientValue",
    "InputControl": "generated_symbols.data.dialog.input.InputControl",
    "InputPredicate": "generated_symbols.data.advancement.predicate.InputPredicate",
    "InsertListOperation": "generated_symbols.data.loot.function.InsertListOperation",
    "InsideWorldBoundsPredicate": "generated_symbols.data.worldgen.feature.block_predicate.InsideWorldBoundsPredicate",
    "Instrument": "generated_symbols.data.variants.instrument.Instrument",
    "IntGameRule": "generated_symbols.data.gametest.test_environment.IntGameRule",
    "IntLimiter": "generated_symbols.data.util.IntLimiter",
    "IntProvider": "generated_symbols.data.worldgen.IntProvider",
    "IntRange": "generated_symbols.data.util.IntRange",
    "InternalTarget": "generated_symbols.assets.shader.post.InternalTarget",
    "InventoryChanged": "generated_symbols.data.advancement.trigger.InventoryChanged",
    "InventoryChangedSlots": "generated_symbols.data.advancement.trigger.InventoryChangedSlots",
    "Inverted": "generated_symbols.data.loot.condition.Inverted",
    "InvertedMatch": "generated_symbols.data.worldgen.processor_list.InvertedMatch",
    "InvervalSelect": "generated_symbols.data.worldgen.density_function.InvervalSelect",
    "ItemBody": "generated_symbols.data.dialog.body.ItemBody",
    "ItemDamageEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.ItemDamageEnchantmentEffect",
    "ItemDefinition": "generated_symbols.assets.item_definition.ItemDefinition",
    "ItemDisplayContext": "generated_symbols.assets.model.ItemDisplayContext",
    "ItemDurabilityChanged": "generated_symbols.data.advancement.trigger.ItemDurabilityChanged",
    "ItemModel": "generated_symbols.assets.item_definition.ItemModel",
    "ItemModeltype": "generated_symbols.assets.item_definition.ItemModeltype",
    "ItemModifier": "generated_symbols.data.item_modifier.ItemModifier",
    "ItemPoolEntry": "generated_symbols.data.loot.ItemPoolEntry",
    "ItemPredicate": "generated_symbols.data.advancement.predicate.ItemPredicate",
    "ItemResult": "generated_symbols.data.recipe.ItemResult",
    "ItemStackTarget": "generated_symbols.data.loot.ItemStackTarget",
    "ItemTransform": "generated_symbols.assets.model.ItemTransform",
    "ItemUsedOnBlock": "generated_symbols.data.advancement.trigger.ItemUsedOnBlock",
    "Jigsaw": "generated_symbols.data.worldgen.structure.Jigsaw",
    "JigsawDistanceLimits": "generated_symbols.data.worldgen.structure.JigsawDistanceLimits",
    "JukeboxSong": "generated_symbols.data.variants.jukebox_song.JukeboxSong",
    "KeybindDown": "generated_symbols.assets.item_definition.KeybindDown",
    "KillMobNearSculkCatalyst": "generated_symbols.data.advancement.trigger.KillMobNearSculkCatalyst",
    "KilledByArrow": "generated_symbols.data.advancement.trigger.KilledByArrow",
    "KilledByCrossbow": "generated_symbols.data.advancement.trigger.KilledByCrossbow",
    "KilledByPlayer": "generated_symbols.data.loot.condition.KilledByPlayer",
    "KnockbackEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.KnockbackEnchantmentEffect",
    "KnockbackModifiers": "generated_symbols.data.sulfur_cube_archetype.KnockbackModifiers",
    "LakeConfig": "generated_symbols.data.worldgen.feature.LakeConfig",
    "Lang": "generated_symbols.assets.lang.Lang",
    "LangDeprecated": "generated_symbols.assets.lang.LangDeprecated",
    "LargeDripstoneConfig": "generated_symbols.data.worldgen.feature.LargeDripstoneConfig",
    "Layer": "generated_symbols.assets.equipment.Layer",
    "Layers": "generated_symbols.assets.equipment.Layers",
    "LeaveVineTreeDecorator": "generated_symbols.data.worldgen.feature.tree.LeaveVineTreeDecorator",
    "LegacyExplorationMapDestination": "generated_symbols.data.loot.function.LegacyExplorationMapDestination",
    "LegacyUnicodeProvider": "generated_symbols.assets.font.LegacyUnicodeProvider",
    "Lerp": "generated_symbols.data.worldgen.density_function.Lerp",
    "LevelBasedValueMap": "generated_symbols.data.enchantment.level_based_value.LevelBasedValueMap",
    "Levitation": "generated_symbols.data.advancement.trigger.Levitation",
    "LightningBoltPredicate": "generated_symbols.data.advancement.predicate.LightningBoltPredicate",
    "LightningStrike": "generated_symbols.data.advancement.trigger.LightningStrike",
    "LimitCount": "generated_symbols.data.loot.function.LimitCount",
    "LimitCountSlotSource": "generated_symbols.data.slot_source.LimitCountSlotSource",
    "LinearLevelValue": "generated_symbols.data.enchantment.level_based_value.LinearLevelValue",
    "LinearPos": "generated_symbols.data.worldgen.processor_list.LinearPos",
    "LiquidSettings": "generated_symbols.data.worldgen.structure.LiquidSettings",
    "ListAttribute": "generated_symbols.data.worldgen.attribute.ListAttribute",
    "ListDialogBase": "generated_symbols.data.dialog.ListDialogBase",
    "ListElement": "generated_symbols.data.worldgen.template_pool.ListElement",
    "ListModifier": "generated_symbols.data.worldgen.attribute.modifier.ListModifier",
    "ListModifierType": "generated_symbols.data.worldgen.attribute.modifier.ListModifierType",
    "ListOperation": "generated_symbols.data.loot.function.ListOperation",
    "ListOperationMode": "generated_symbols.data.loot.function.ListOperationMode",
    "LlamaPredicate": "generated_symbols.data.advancement.predicate.LlamaPredicate",
    "LocalTime": "generated_symbols.assets.item_definition.LocalTime",
    "LocationBasedEffect": "generated_symbols.data.enchantment.effect.LocationBasedEffect",
    "LocationChangedEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.LocationChangedEnchantmentEffect",
    "LocationCheck": "generated_symbols.data.loot.condition.LocationCheck",
    "LocationPredicate": "generated_symbols.data.advancement.predicate.LocationPredicate",
    "LocationPredicateLight": "generated_symbols.data.advancement.predicate.LocationPredicateLight",
    "LocationPredicatePosition": "generated_symbols.data.advancement.predicate.LocationPredicatePosition",
    "LookupLevelValue": "generated_symbols.data.enchantment.level_based_value.LookupLevelValue",
    "LootConditionType": "generated_symbols.data.loot.LootConditionType",
    "LootContextParamSets": "generated_symbols.data.loot.LootContextParamSets",
    "LootEntryType": "generated_symbols.data.loot.LootEntryType",
    "LootFunctionType": "generated_symbols.data.loot.LootFunctionType",
    "LootPool": "generated_symbols.data.loot.LootPool",
    "LootPoolEntry": "generated_symbols.data.loot.LootPoolEntry",
    "LootPoolEntryBase": "generated_symbols.data.loot.LootPoolEntryBase",
    "LootTable": "generated_symbols.data.loot.LootTable",
    "LootTableListRef": "generated_symbols.data.loot.LootTableListRef",
    "LootTablePoolEntry": "generated_symbols.data.loot.LootTablePoolEntry",
    "LootTableRef": "generated_symbols.data.loot.LootTableRef",
    "LootingEnchant": "generated_symbols.data.loot.function.LootingEnchant",
    "MainHand": "generated_symbols.assets.item_definition.MainHand",
    "MangroveRootPlacement": "generated_symbols.data.worldgen.feature.tree.MangroveRootPlacement",
    "MangroveRootPlacer": "generated_symbols.data.worldgen.feature.tree.MangroveRootPlacer",
    "MapColorTint": "generated_symbols.assets.item_definition.MapColorTint",
    "MapDecoration": "generated_symbols.data.loot.function.MapDecoration",
    "MatchTool": "generated_symbols.data.loot.condition.MatchTool",
    "MatchingBiomesPredicate": "generated_symbols.data.worldgen.feature.block_predicate.MatchingBiomesPredicate",
    "MatchingBlockTagPredicate": "generated_symbols.data.worldgen.feature.block_predicate.MatchingBlockTagPredicate",
    "MatchingBlocksPredicate": "generated_symbols.data.worldgen.feature.block_predicate.MatchingBlocksPredicate",
    "MatchingFluidsPredicate": "generated_symbols.data.worldgen.feature.block_predicate.MatchingFluidsPredicate",
    "MaterialCondition": "generated_symbols.data.worldgen.material_condition.MaterialCondition",
    "MaterialConditionRef": "generated_symbols.data.worldgen.material_condition.MaterialConditionRef",
    "MaterialRule": "generated_symbols.data.worldgen.material_rule.MaterialRule",
    "MaterialRuleRef": "generated_symbols.data.worldgen.material_rule.MaterialRuleRef",
    "MegaPineFoliagePlacer": "generated_symbols.data.worldgen.feature.tree.MegaPineFoliagePlacer",
    "MergeableAttribute": "generated_symbols.data.worldgen.attribute.MergeableAttribute",
    "MergeableModifier": "generated_symbols.data.worldgen.attribute.modifier.MergeableModifier",
    "MergeableModifierType": "generated_symbols.data.worldgen.attribute.modifier.MergeableModifierType",
    "MinMaxBounds": "generated_symbols.data.util.MinMaxBounds",
    "Mineshaft": "generated_symbols.data.worldgen.structure.Mineshaft",
    "MineshaftType": "generated_symbols.data.worldgen.structure.MineshaftType",
    "MipmapStrategy": "generated_symbols.assets.texture_meta.MipmapStrategy",
    "MobCategory": "generated_symbols.data.worldgen.biome.MobCategory",
    "MobEffectPredicate": "generated_symbols.data.advancement.predicate.MobEffectPredicate",
    "MobExperienceEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.MobExperienceEnchantmentEffect",
    "MobSpawnCost": "generated_symbols.data.worldgen.biome.MobSpawnCost",
    "ModelDisplay": "generated_symbols.assets.model.ModelDisplay",
    "ModelElement": "generated_symbols.assets.model.ModelElement",
    "ModelElementFace": "generated_symbols.assets.model.ModelElementFace",
    "ModelElementFaceMap": "generated_symbols.assets.model.ModelElementFaceMap",
    "ModelElementRotation": "generated_symbols.assets.model.ModelElementRotation",
    "ModelElementRotationBase": "generated_symbols.assets.model.ModelElementRotationBase",
    "ModelOverride": "generated_symbols.assets.model.ModelOverride",
    "ModelOverridePredicates": "generated_symbols.assets.model.ModelOverridePredicates",
    "ModelRef": "generated_symbols.assets.model.ModelRef",
    "ModelTextures": "generated_symbols.assets.model.ModelTextures",
    "ModelTint": "generated_symbols.assets.item_definition.ModelTint",
    "ModelVariant": "generated_symbols.assets.block_state_definition.ModelVariant",
    "ModelVariantBase": "generated_symbols.assets.block_state_definition.ModelVariantBase",
    "ModernNetherVegetationConfig": "generated_symbols.data.worldgen.feature.ModernNetherVegetationConfig",
    "ModernPatchConfig": "generated_symbols.data.worldgen.feature.ModernPatchConfig",
    "ModifyContents": "generated_symbols.data.loot.function.ModifyContents",
    "MoodSound": "generated_symbols.data.worldgen.biome.MoodSound",
    "MoonBrightnessCheck": "generated_symbols.data.variants.MoonBrightnessCheck",
    "MoonPhase": "generated_symbols.data.util.MoonPhase",
    "MooshroomPredicate": "generated_symbols.data.advancement.predicate.MooshroomPredicate",
    "MovementPredicate": "generated_symbols.data.advancement.predicate.MovementPredicate",
    "MultiActionDialog": "generated_symbols.data.dialog.MultiActionDialog",
    "MultiLine": "generated_symbols.data.dialog.input.MultiLine",
    "MultiNoise": "generated_symbols.data.worldgen.dimension.biome_source.MultiNoise",
    "MultiNoiseBase": "generated_symbols.data.worldgen.dimension.biome_source.MultiNoiseBase",
    "MultiNoiseBiomeSourceParameterList": "generated_symbols.data.worldgen.dimension.biome_source.MultiNoiseBiomeSourceParameterList",
    "MultiNoisePreset": "generated_symbols.data.worldgen.dimension.biome_source.MultiNoisePreset",
    "MultiPartAlternatives": "generated_symbols.assets.block_state_definition.MultiPartAlternatives",
    "MultiPartAnd": "generated_symbols.assets.block_state_definition.MultiPartAnd",
    "MultiPartCondition": "generated_symbols.assets.block_state_definition.MultiPartCondition",
    "MultifaceBlock": "generated_symbols.data.worldgen.feature.MultifaceBlock",
    "MultifaceGrowthConfig": "generated_symbols.data.worldgen.feature.MultifaceGrowthConfig",
    "MultipleAxesModelElementRotation": "generated_symbols.assets.model.MultipleAxesModelElementRotation",
    "MultiplyEffectValue": "generated_symbols.data.enchantment.effect.MultiplyEffectValue",
    "Narration": "generated_symbols.data.chat_type.Narration",
    "NarrationPriority": "generated_symbols.data.chat_type.NarrationPriority",
    "NaturalMobSpawns": "generated_symbols.data.worldgen.biome.NaturalMobSpawns",
    "NbtContextTarget": "generated_symbols.data.util.NbtContextTarget",
    "NbtProvider": "generated_symbols.data.util.NbtProvider",
    "NbtProviderSource": "generated_symbols.data.util.NbtProviderSource",
    "NetherForestVegetationConfig": "generated_symbols.data.worldgen.feature.NetherForestVegetationConfig",
    "NetherFossil": "generated_symbols.data.worldgen.structure.NetherFossil",
    "NetherTravel": "generated_symbols.data.advancement.trigger.NetherTravel",
    "NetherrackReplaceBlobsConfig": "generated_symbols.data.worldgen.feature.NetherrackReplaceBlobsConfig",
    "NineSlice": "generated_symbols.assets.texture_meta.NineSlice",
    "NineSliceBorder": "generated_symbols.assets.texture_meta.NineSliceBorder",
    "NoiseBasedCountModifier": "generated_symbols.data.worldgen.feature.placement.NoiseBasedCountModifier",
    "NoiseGeneratorFlags": "generated_symbols.data.worldgen.noise_settings.NoiseGeneratorFlags",
    "NoiseGeneratorSettings": "generated_symbols.data.worldgen.noise_settings.NoiseGeneratorSettings",
    "NoiseGeneratorSettingsRef": "generated_symbols.data.worldgen.noise_settings.NoiseGeneratorSettingsRef",
    "NoiseParameters": "generated_symbols.data.worldgen.dimension.biome_source.NoiseParameters",
    "NoiseParametersRef": "generated_symbols.data.worldgen.density_function.NoiseParametersRef",
    "NoiseProvider": "generated_symbols.data.worldgen.feature.block_state_provider.NoiseProvider",
    "NoiseRange": "generated_symbols.data.worldgen.density_function.NoiseRange",
    "NoiseRouter": "generated_symbols.data.worldgen.noise_settings.NoiseRouter",
    "NoiseSamplingSettings": "generated_symbols.data.worldgen.noise_settings.NoiseSamplingSettings",
    "NoiseSettings": "generated_symbols.data.worldgen.noise_settings.NoiseSettings",
    "NoiseSlideSettings": "generated_symbols.data.worldgen.noise_settings.NoiseSlideSettings",
    "NoiseThresholdCondition": "generated_symbols.data.worldgen.material_condition.NoiseThresholdCondition",
    "NoiseThresholdCountModifier": "generated_symbols.data.worldgen.feature.placement.NoiseThresholdCountModifier",
    "NoiseThresholdProvider": "generated_symbols.data.worldgen.feature.block_state_provider.NoiseThresholdProvider",
    "NotCondition": "generated_symbols.data.worldgen.material_condition.NotCondition",
    "NotPredicate": "generated_symbols.data.worldgen.feature.block_predicate.NotPredicate",
    "NoticeDialog": "generated_symbols.data.dialog.NoticeDialog",
    "Notification": "generated_symbols.assets.regional_compliancies.Notification",
    "NotificationInfo": "generated_symbols.data.recipe.NotificationInfo",
    "NumberDispatcher": "generated_symbols.data.number_provider.NumberDispatcher",
    "NumberProvider": "generated_symbols.data.number_provider.NumberProvider",
    "NumberProviderListRef": "generated_symbols.data.number_provider.NumberProviderListRef",
    "NumberProviderRef": "generated_symbols.data.number_provider.NumberProviderRef",
    "NumberRangeInput": "generated_symbols.data.dialog.input.NumberRangeInput",
    "NumericPropertyType": "generated_symbols.assets.item_definition.NumericPropertyType",
    "NumericalEnvironmentAttribute": "generated_symbols.data.worldgen.attribute.NumericalEnvironmentAttribute",
    "OceanRuin": "generated_symbols.data.worldgen.structure.OceanRuin",
    "OffsetModifier": "generated_symbols.data.worldgen.feature.placement.OffsetModifier",
    "OldBlendedNoise": "generated_symbols.data.worldgen.density_function.OldBlendedNoise",
    "OldChatType": "generated_symbols.data.chat_type.OldChatType",
    "OldEntityPredicate": "generated_symbols.data.advancement.predicate.OldEntityPredicate",
    "OldPatchConfig": "generated_symbols.data.worldgen.feature.OldPatchConfig",
    "OldRangeConfig": "generated_symbols.data.worldgen.feature.decorator.OldRangeConfig",
    "OldSimpleBlockConfig": "generated_symbols.data.worldgen.feature.OldSimpleBlockConfig",
    "OldTarget": "generated_symbols.assets.shader.post.OldTarget",
    "OldTrimMaterialOverrides": "generated_symbols.data.trim.OldTrimMaterialOverrides",
    "OneArgument": "generated_symbols.data.worldgen.density_function.OneArgument",
    "Option": "generated_symbols.data.dialog.input.Option",
    "OptionalSimpleBlockConfig": "generated_symbols.data.worldgen.feature.OptionalSimpleBlockConfig",
    "OptionalSmithingIngredients": "generated_symbols.data.recipe.OptionalSmithingIngredients",
    "OreConfig": "generated_symbols.data.worldgen.feature.OreConfig",
    "OreVeinifier": "generated_symbols.data.worldgen.noise_settings.OreVeinifier",
    "OverlayConfig": "generated_symbols.data.worldgen.feature.OverlayConfig",
    "OverrideModifier": "generated_symbols.data.worldgen.attribute.modifier.OverrideModifier",
    "PaintingPredicate": "generated_symbols.data.advancement.predicate.PaintingPredicate",
    "PaintingVariant": "generated_symbols.data.variants.painting.PaintingVariant",
    "PaleMossTreeDecorator": "generated_symbols.data.worldgen.feature.tree.PaleMossTreeDecorator",
    "Palette": "generated_symbols.data.structure.Palette",
    "PaletteMeta": "generated_symbols.assets.texture_meta.PaletteMeta",
    "PaletteRef": "generated_symbols.assets.atlas.PaletteRef",
    "PaletteTexture": "generated_symbols.assets.atlas.PaletteTexture",
    "PalettedPermutations": "generated_symbols.assets.atlas.PalettedPermutations",
    "ParrotPredicate": "generated_symbols.data.advancement.predicate.ParrotPredicate",
    "Particle": "generated_symbols.assets.particle.Particle",
    "ParticlePosition": "generated_symbols.data.enchantment.effect.ParticlePosition",
    "ParticleVelocity": "generated_symbols.data.enchantment.effect.ParticleVelocity",
    "Pass": "generated_symbols.assets.shader.post.Pass",
    "PermutationsMap": "generated_symbols.assets.atlas.PermutationsMap",
    "PigModelType": "generated_symbols.data.variants.pig.PigModelType",
    "PigSounds": "generated_symbols.data.variants.pig.PigSounds",
    "PigVariant": "generated_symbols.data.variants.pig.PigVariant",
    "PineFoliagePlacer": "generated_symbols.data.worldgen.feature.tree.PineFoliagePlacer",
    "PlaceOnGroundTreeDecorator": "generated_symbols.data.worldgen.feature.tree.PlaceOnGroundTreeDecorator",
    "PlacedBlock": "generated_symbols.data.advancement.trigger.PlacedBlock",
    "PlacedFeature": "generated_symbols.data.worldgen.feature.placement.PlacedFeature",
    "PlacedFeatureListRef": "generated_symbols.data.worldgen.feature.placement.PlacedFeatureListRef",
    "PlacedFeatureRef": "generated_symbols.data.worldgen.feature.placement.PlacedFeatureRef",
    "PlacementModifier": "generated_symbols.data.worldgen.feature.placement.PlacementModifier",
    "PlainMessage": "generated_symbols.data.dialog.body.PlainMessage",
    "PlaySoundEntityEffect": "generated_symbols.data.enchantment.effect.PlaySoundEntityEffect",
    "PlayerAdvancementCriteria": "generated_symbols.data.advancement.predicate.PlayerAdvancementCriteria",
    "PlayerAdvancements": "generated_symbols.data.advancement.predicate.PlayerAdvancements",
    "PlayerGeneratesContainerLoot": "generated_symbols.data.advancement.trigger.PlayerGeneratesContainerLoot",
    "PlayerHurtEntity": "generated_symbols.data.advancement.trigger.PlayerHurtEntity",
    "PlayerInteract": "generated_symbols.data.advancement.trigger.PlayerInteract",
    "PlayerKilledEntity": "generated_symbols.data.advancement.trigger.PlayerKilledEntity",
    "PlayerPredicate": "generated_symbols.data.advancement.predicate.PlayerPredicate",
    "PlayerRecipes": "generated_symbols.data.advancement.predicate.PlayerRecipes",
    "PlayerTrigger": "generated_symbols.data.advancement.trigger.PlayerTrigger",
    "PoolAlias": "generated_symbols.data.worldgen.structure.PoolAlias",
    "PoplarFoliagePlacer": "generated_symbols.data.worldgen.feature.tree.PoplarFoliagePlacer",
    "PoplarTrunkPlacer": "generated_symbols.data.worldgen.feature.tree.PoplarTrunkPlacer",
    "PosRuleTest": "generated_symbols.data.worldgen.processor_list.PosRuleTest",
    "PositionalEnvironmentAttribute": "generated_symbols.data.worldgen.attribute.PositionalEnvironmentAttribute",
    "PositionalEnvironmentAttributeMap": "generated_symbols.data.worldgen.attribute.PositionalEnvironmentAttributeMap",
    "PostAttackEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.PostAttackEnchantmentEffect",
    "PostComponentsItemPredicate": "generated_symbols.data.advancement.predicate.PostComponentsItemPredicate",
    "PostEffect": "generated_symbols.assets.shader.post.PostEffect",
    "PostPiercingAttackEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.PostPiercingAttackEnchantmentEffect",
    "PotionIngredient": "generated_symbols.data.recipe.PotionIngredient",
    "PotionTint": "generated_symbols.assets.item_definition.PotionTint",
    "Pow": "generated_symbols.data.worldgen.density_function.Pow",
    "PreComponentsItemPredicate": "generated_symbols.data.advancement.predicate.PreComponentsItemPredicate",
    "Precipitation": "generated_symbols.data.worldgen.biome.Precipitation",
    "Predicate": "generated_symbols.data.predicate.Predicate",
    "PredicateListRef": "generated_symbols.data.predicate.PredicateListRef",
    "PredicateOffset": "generated_symbols.data.worldgen.feature.block_predicate.PredicateOffset",
    "PredicateRef": "generated_symbols.data.predicate.PredicateRef",
    "Predicates": "generated_symbols.assets.model.Predicates",
    "ProbabilityConfig": "generated_symbols.data.worldgen.feature.ProbabilityConfig",
    "Processor": "generated_symbols.data.worldgen.processor_list.Processor",
    "ProcessorList": "generated_symbols.data.worldgen.processor_list.ProcessorList",
    "ProcessorListObject": "generated_symbols.data.worldgen.processor_list.ProcessorListObject",
    "ProcessorListRef": "generated_symbols.data.worldgen.processor_list.ProcessorListRef",
    "ProcessorRule": "generated_symbols.data.worldgen.processor_list.ProcessorRule",
    "ProjectedSquareConfig": "generated_symbols.data.worldgen.feature.ProjectedSquareConfig",
    "ProjectileCountEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.ProjectileCountEnchantmentEffect",
    "ProjectilePiercingEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.ProjectilePiercingEnchantmentEffect",
    "ProjectileSpawnedEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.ProjectileSpawnedEnchantmentEffect",
    "ProjectileSpreadEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.ProjectileSpreadEnchantmentEffect",
    "Projection": "generated_symbols.data.worldgen.template_pool.Projection",
    "ProtectedBlocks": "generated_symbols.data.worldgen.processor_list.ProtectedBlocks",
    "RGBColorAttribute": "generated_symbols.data.worldgen.attribute.RGBColorAttribute",
    "RabbitPredicate": "generated_symbols.data.advancement.predicate.RabbitPredicate",
    "RaiderPredicate": "generated_symbols.data.advancement.predicate.RaiderPredicate",
    "RandomBlockMatch": "generated_symbols.data.worldgen.processor_list.RandomBlockMatch",
    "RandomBlockStateMatch": "generated_symbols.data.worldgen.processor_list.RandomBlockStateMatch",
    "RandomBlockStateProvider": "generated_symbols.data.worldgen.feature.block_state_provider.RandomBlockStateProvider",
    "RandomBooleanSelector": "generated_symbols.data.worldgen.feature.RandomBooleanSelector",
    "RandomChance": "generated_symbols.data.loot.condition.RandomChance",
    "RandomChanceModifier": "generated_symbols.data.worldgen.feature.placement.RandomChanceModifier",
    "RandomChanceWithEnchantedBonus": "generated_symbols.data.loot.condition.RandomChanceWithEnchantedBonus",
    "RandomChanceWithLooting": "generated_symbols.data.loot.condition.RandomChanceWithLooting",
    "RandomFeatureEntry": "generated_symbols.data.worldgen.feature.RandomFeatureEntry",
    "RandomGroupPoolAlias": "generated_symbols.data.worldgen.structure.RandomGroupPoolAlias",
    "RandomIntGenerator": "generated_symbols.data.util.RandomIntGenerator",
    "RandomIntGeneratorType": "generated_symbols.data.util.RandomIntGeneratorType",
    "RandomNeighborSpreadConfig": "generated_symbols.data.worldgen.feature.RandomNeighborSpreadConfig",
    "RandomOffsetModifier": "generated_symbols.data.worldgen.feature.placement.RandomOffsetModifier",
    "RandomPatchConfig": "generated_symbols.data.worldgen.feature.RandomPatchConfig",
    "RandomPoolAlias": "generated_symbols.data.worldgen.structure.RandomPoolAlias",
    "RandomSelector": "generated_symbols.data.worldgen.feature.RandomSelector",
    "RandomSpreadFoliagePlacer": "generated_symbols.data.worldgen.feature.tree.RandomSpreadFoliagePlacer",
    "RandomSpreadPlacement": "generated_symbols.data.worldgen.structure_set.RandomSpreadPlacement",
    "RandomValueBounds": "generated_symbols.data.util.RandomValueBounds",
    "RandomizedIntStateProvider": "generated_symbols.data.worldgen.feature.block_state_provider.RandomizedIntStateProvider",
    "RandomizedPalette": "generated_symbols.data.structure.RandomizedPalette",
    "RangeChoice": "generated_symbols.data.worldgen.density_function.RangeChoice",
    "RangeConfig": "generated_symbols.data.worldgen.feature.decorator.RangeConfig",
    "RangeDispatch": "generated_symbols.assets.item_definition.RangeDispatch",
    "RangeDispatchEntry": "generated_symbols.assets.item_definition.RangeDispatchEntry",
    "RangeSlotSource": "generated_symbols.data.slot_source.RangeSlotSource",
    "RarityFilter": "generated_symbols.data.worldgen.feature.placement.RarityFilter",
    "RarityType": "generated_symbols.data.worldgen.density_function.RarityType",
    "Recipe": "generated_symbols.data.recipe.Recipe",
    "RecipeCrafted": "generated_symbols.data.advancement.trigger.RecipeCrafted",
    "RecipeListRef": "generated_symbols.data.recipe.RecipeListRef",
    "RecipeUnlocked": "generated_symbols.data.advancement.trigger.RecipeUnlocked",
    "RedirectDialog": "generated_symbols.data.dialog.RedirectDialog",
    "ReduceBinomialEffectValue": "generated_symbols.data.enchantment.effect.ReduceBinomialEffectValue",
    "ReferenceProvider": "generated_symbols.assets.font.ReferenceProvider",
    "RegionalCompliancies": "generated_symbols.assets.regional_compliancies.RegionalCompliancies",
    "RepairWithXpEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.RepairWithXpEnchantmentEffect",
    "ReplaceBlockEntityEffect": "generated_symbols.data.enchantment.effect.ReplaceBlockEntityEffect",
    "ReplaceDiskEntityEffect": "generated_symbols.data.enchantment.effect.ReplaceDiskEntityEffect",
    "ReplaceSectionListOperation": "generated_symbols.data.loot.function.ReplaceSectionListOperation",
    "ReplaceSingleBlockConfig": "generated_symbols.data.worldgen.feature.ReplaceSingleBlockConfig",
    "RequiredConditions": "generated_symbols.data.advancement.trigger.RequiredConditions",
    "RequiredSmithingIngredients": "generated_symbols.data.recipe.RequiredSmithingIngredients",
    "ResolvableNumber": "generated_symbols.data.number_provider.ResolvableNumber",
    "RideEntityInLava": "generated_symbols.data.advancement.trigger.RideEntityInLava",
    "RootPlacer": "generated_symbols.data.worldgen.feature.tree.RootPlacer",
    "RootSystemConfig": "generated_symbols.data.worldgen.feature.RootSystemConfig",
    "RotatedStateProvider": "generated_symbols.data.worldgen.feature.block_state_provider.RotatedStateProvider",
    "Round": "generated_symbols.data.worldgen.density_function.Round",
    "RuinedPortal": "generated_symbols.data.worldgen.structure.RuinedPortal",
    "RuinedPortalPlacement": "generated_symbols.data.worldgen.structure.RuinedPortalPlacement",
    "RuinedPortalSetup": "generated_symbols.data.worldgen.structure.RuinedPortalSetup",
    "RuinedPortalType": "generated_symbols.data.worldgen.structure.RuinedPortalType",
    "Rule": "generated_symbols.data.worldgen.processor_list.Rule",
    "RuleBasedBlockStateProvider": "generated_symbols.data.worldgen.feature.RuleBasedBlockStateProvider",
    "RuleTest": "generated_symbols.data.worldgen.processor_list.RuleTest",
    "RunFunctionEntityEffect": "generated_symbols.data.enchantment.effect.RunFunctionEntityEffect",
    "SafelyHarvestHoney": "generated_symbols.data.advancement.trigger.SafelyHarvestHoney",
    "SalmonPredicate": "generated_symbols.data.advancement.predicate.SalmonPredicate",
    "SalmonVariant": "generated_symbols.data.advancement.predicate.SalmonVariant",
    "Sampler": "generated_symbols.assets.shader.program.Sampler",
    "ScoreNumberProvider": "generated_symbols.data.number_provider.ScoreNumberProvider",
    "ScoreProvider": "generated_symbols.data.util.ScoreProvider",
    "SculkPatchConfig": "generated_symbols.data.worldgen.feature.SculkPatchConfig",
    "SeaPickleConfig": "generated_symbols.data.worldgen.feature.SeaPickleConfig",
    "Select": "generated_symbols.assets.item_definition.Select",
    "SelectCase": "generated_symbols.assets.item_definition.SelectCase",
    "SelectCases": "generated_symbols.assets.item_definition.SelectCases",
    "SelectPropertyType": "generated_symbols.assets.item_definition.SelectPropertyType",
    "Sequence": "generated_symbols.data.loot.function.Sequence",
    "SequenceConfig": "generated_symbols.data.worldgen.feature.SequenceConfig",
    "SequenceRule": "generated_symbols.data.worldgen.material_rule.SequenceRule",
    "ServerLinksDialog": "generated_symbols.data.dialog.ServerLinksDialog",
    "SetAttributes": "generated_symbols.data.loot.function.SetAttributes",
    "SetBannerPattern": "generated_symbols.data.loot.function.SetBannerPattern",
    "SetBlockPropertiesEntityEffect": "generated_symbols.data.enchantment.effect.SetBlockPropertiesEntityEffect",
    "SetBookCover": "generated_symbols.data.loot.function.SetBookCover",
    "SetComponents": "generated_symbols.data.loot.function.SetComponents",
    "SetContents": "generated_symbols.data.loot.function.SetContents",
    "SetCount": "generated_symbols.data.loot.function.SetCount",
    "SetCustomData": "generated_symbols.data.loot.function.SetCustomData",
    "SetCustomModelData": "generated_symbols.data.loot.function.SetCustomModelData",
    "SetDamage": "generated_symbols.data.loot.function.SetDamage",
    "SetEffectValue": "generated_symbols.data.enchantment.effect.SetEffectValue",
    "SetEnchantments": "generated_symbols.data.loot.function.SetEnchantments",
    "SetFireworkExplosion": "generated_symbols.data.loot.function.SetFireworkExplosion",
    "SetFireworks": "generated_symbols.data.loot.function.SetFireworks",
    "SetInstrument": "generated_symbols.data.loot.function.SetInstrument",
    "SetItem": "generated_symbols.data.loot.function.SetItem",
    "SetLootTable": "generated_symbols.data.loot.function.SetLootTable",
    "SetLore": "generated_symbols.data.loot.function.SetLore",
    "SetName": "generated_symbols.data.loot.function.SetName",
    "SetNameTarget": "generated_symbols.data.loot.function.SetNameTarget",
    "SetNbt": "generated_symbols.data.loot.function.SetNbt",
    "SetOminousBottleAmplifier": "generated_symbols.data.loot.function.SetOminousBottleAmplifier",
    "SetPotion": "generated_symbols.data.loot.function.SetPotion",
    "SetRandomDyes": "generated_symbols.data.loot.function.SetRandomDyes",
    "SetRandomPotion": "generated_symbols.data.loot.function.SetRandomPotion",
    "SetStewEffect": "generated_symbols.data.loot.function.SetStewEffect",
    "SetWriteableBookPages": "generated_symbols.data.loot.function.SetWriteableBookPages",
    "SetWrittenBookPages": "generated_symbols.data.loot.function.SetWrittenBookPages",
    "ShaderProgram": "generated_symbols.assets.shader.program.ShaderProgram",
    "SheepPredicate": "generated_symbols.data.advancement.predicate.SheepPredicate",
    "ShelfMushroomTreeDecorator": "generated_symbols.data.worldgen.feature.tree.ShelfMushroomTreeDecorator",
    "Shift": "generated_symbols.data.worldgen.density_function.Shift",
    "ShiftedNoise": "generated_symbols.data.worldgen.density_function.ShiftedNoise",
    "Shipwreck": "generated_symbols.data.worldgen.structure.Shipwreck",
    "ShotCrossbow": "generated_symbols.data.advancement.trigger.ShotCrossbow",
    "ShulkerBox": "generated_symbols.assets.item_definition.ShulkerBox",
    "SimpleBlockConfig": "generated_symbols.data.worldgen.feature.SimpleBlockConfig",
    "SimpleEasingType": "generated_symbols.data.timeline.SimpleEasingType",
    "SimpleRandomSelectorConfig": "generated_symbols.data.worldgen.feature.SimpleRandomSelectorConfig",
    "SimpleStateProvider": "generated_symbols.data.worldgen.feature.block_state_provider.SimpleStateProvider",
    "Single": "generated_symbols.assets.atlas.Single",
    "SingleAxisModelElementRotation": "generated_symbols.assets.model.SingleAxisModelElementRotation",
    "SingleBlockPillarConfig": "generated_symbols.data.worldgen.feature.SingleBlockPillarConfig",
    "SingleElement": "generated_symbols.data.worldgen.template_pool.SingleElement",
    "SingleOptionInput": "generated_symbols.data.dialog.input.SingleOptionInput",
    "SingleProvider": "generated_symbols.data.enchantment.provider.SingleProvider",
    "SingletonPoolEntry": "generated_symbols.data.loot.SingletonPoolEntry",
    "SkyboxType": "generated_symbols.data.worldgen.dimension.SkyboxType",
    "Slice": "generated_symbols.data.worldgen.density_function.Slice",
    "SlideDownBlock": "generated_symbols.data.advancement.trigger.SlideDownBlock",
    "SlimePredicate": "generated_symbols.data.advancement.predicate.SlimePredicate",
    "SlotSource": "generated_symbols.data.slot_source.SlotSource",
    "SlotsPoolEntry": "generated_symbols.data.loot.SlotsPoolEntry",
    "SmallDripstoneConfig": "generated_symbols.data.worldgen.feature.SmallDripstoneConfig",
    "SmashDamagePerBlockFallenEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.SmashDamagePerBlockFallenEnchantmentEffect",
    "Smelting": "generated_symbols.data.recipe.Smelting",
    "Smithing": "generated_symbols.data.recipe.Smithing",
    "SmithingIngredients": "generated_symbols.data.recipe.SmithingIngredients",
    "SmithingTransform": "generated_symbols.data.recipe.SmithingTransform",
    "SmithingTransformResult": "generated_symbols.data.recipe.SmithingTransformResult",
    "SmithingTrim": "generated_symbols.data.recipe.SmithingTrim",
    "Sound": "generated_symbols.assets.sounds.Sound",
    "SoundEventRef": "generated_symbols.data.util.SoundEventRef",
    "SoundEventRegistration": "generated_symbols.assets.sounds.SoundEventRegistration",
    "SoundSettings": "generated_symbols.data.sulfur_cube_archetype.SoundSettings",
    "SoundType": "generated_symbols.assets.sounds.SoundType",
    "SoundVariant": "generated_symbols.data.variants.SoundVariant",
    "Sounds": "generated_symbols.assets.sounds.Sounds",
    "SpaceProvider": "generated_symbols.assets.font.SpaceProvider",
    "SpawnCondition": "generated_symbols.data.variants.SpawnCondition",
    "SpawnOverride": "generated_symbols.data.worldgen.structure.SpawnOverride",
    "SpawnParticlesEntityEffect": "generated_symbols.data.enchantment.effect.SpawnParticlesEntityEffect",
    "SpawnPrioritySelector": "generated_symbols.data.variants.SpawnPrioritySelector",
    "SpawnPrioritySelectors": "generated_symbols.data.variants.SpawnPrioritySelectors",
    "SpawnTargetPoint": "generated_symbols.data.worldgen.noise_settings.SpawnTargetPoint",
    "SpawnerData": "generated_symbols.data.worldgen.biome.SpawnerData",
    "SpawnerDataMap": "generated_symbols.data.worldgen.biome.SpawnerDataMap",
    "SpearMobs": "generated_symbols.data.advancement.trigger.SpearMobs",
    "Special": "generated_symbols.assets.item_definition.Special",
    "SpecialModel": "generated_symbols.assets.item_definition.SpecialModel",
    "SpecialModelType": "generated_symbols.assets.item_definition.SpecialModelType",
    "SpecificType": "generated_symbols.data.advancement.predicate.SpecificType",
    "SpeleothemClusterConfig": "generated_symbols.data.worldgen.feature.SpeleothemClusterConfig",
    "SpeleothemConfig": "generated_symbols.data.worldgen.feature.SpeleothemConfig",
    "SpikeConfig": "generated_symbols.data.worldgen.feature.SpikeConfig",
    "Spline": "generated_symbols.data.worldgen.density_function.Spline",
    "SplinePoint": "generated_symbols.data.worldgen.density_function.SplinePoint",
    "SplineType": "generated_symbols.data.worldgen.density_function.SplineType",
    "SpreadType": "generated_symbols.data.worldgen.structure_set.SpreadType",
    "SpringConfig": "generated_symbols.data.worldgen.feature.SpringConfig",
    "SpriteSource": "generated_symbols.assets.atlas.SpriteSource",
    "SpriteSourceType": "generated_symbols.assets.atlas.SpriteSourceType",
    "SprucePineFoliagePlacer": "generated_symbols.data.worldgen.feature.tree.SprucePineFoliagePlacer",
    "SquaredLevelValue": "generated_symbols.data.enchantment.level_based_value.SquaredLevelValue",
    "StandingSign": "generated_symbols.assets.item_definition.StandingSign",
    "StandingSignAttachment": "generated_symbols.assets.item_definition.StandingSignAttachment",
    "StatisticPredicate": "generated_symbols.data.advancement.predicate.StatisticPredicate",
    "StewEffect": "generated_symbols.data.loot.function.StewEffect",
    "StoneDepthCondition": "generated_symbols.data.worldgen.material_condition.StoneDepthCondition",
    "Stonecutting": "generated_symbols.data.recipe.Stonecutting",
    "StorageNbtProvider": "generated_symbols.data.util.StorageNbtProvider",
    "StorageNumberProvider": "generated_symbols.data.number_provider.StorageNumberProvider",
    "Structure": "generated_symbols.data.worldgen.structure.Structure",
    "StructureBlock": "generated_symbols.data.structure.StructureBlock",
    "StructureCheck": "generated_symbols.data.variants.StructureCheck",
    "StructureEntity": "generated_symbols.data.structure.StructureEntity",
    "StructureNBT": "generated_symbols.data.structure.StructureNBT",
    "StructurePlacement": "generated_symbols.data.worldgen.structure_set.StructurePlacement",
    "StructureRef": "generated_symbols.data.worldgen.structure.StructureRef",
    "StructureSet": "generated_symbols.data.worldgen.structure_set.StructureSet",
    "StructureSetElement": "generated_symbols.data.worldgen.structure_set.StructureSetElement",
    "StructureSetRef": "generated_symbols.data.worldgen.structure_set.StructureSetRef",
    "StructureSettings": "generated_symbols.data.worldgen.noise_settings.StructureSettings",
    "SulfurCubeArchetype": "generated_symbols.data.sulfur_cube_archetype.SulfurCubeArchetype",
    "SumNumberProvider": "generated_symbols.data.number_provider.SumNumberProvider",
    "SummonEntityEffect": "generated_symbols.data.enchantment.effect.SummonEntityEffect",
    "SummonedEntity": "generated_symbols.data.advancement.trigger.SummonedEntity",
    "SurfaceRelativeThresholdFilter": "generated_symbols.data.worldgen.feature.placement.SurfaceRelativeThresholdFilter",
    "SurfaceWaterDepthFilter": "generated_symbols.data.worldgen.feature.placement.SurfaceWaterDepthFilter",
    "TableBonus": "generated_symbols.data.loot.condition.TableBonus",
    "Tag": "generated_symbols.data.tag.Tag",
    "TagEntry": "generated_symbols.data.tag.TagEntry",
    "TagMatch": "generated_symbols.data.worldgen.processor_list.TagMatch",
    "TagPoolEntry": "generated_symbols.data.loot.TagPoolEntry",
    "TameAnimal": "generated_symbols.data.advancement.trigger.TameAnimal",
    "TargetBlock": "generated_symbols.data.worldgen.feature.TargetBlock",
    "TargetHit": "generated_symbols.data.advancement.trigger.TargetHit",
    "TargetInput": "generated_symbols.assets.shader.post.TargetInput",
    "Targets": "generated_symbols.assets.shader.post.Targets",
    "TeamTint": "generated_symbols.assets.item_definition.TeamTint",
    "TemperatureModifier": "generated_symbols.data.worldgen.biome.TemperatureModifier",
    "TemplateConfig": "generated_symbols.data.worldgen.feature.TemplateConfig",
    "TemplateEntry": "generated_symbols.data.worldgen.feature.TemplateEntry",
    "TemplatePool": "generated_symbols.data.worldgen.template_pool.TemplatePool",
    "TerrainAdaptation": "generated_symbols.data.worldgen.structure.TerrainAdaptation",
    "TerrainCoordinate": "generated_symbols.data.worldgen.density_function.TerrainCoordinate",
    "TerrainShaper": "generated_symbols.data.worldgen.noise_settings.TerrainShaper",
    "TerrainShaperSpline": "generated_symbols.data.worldgen.density_function.TerrainShaperSpline",
    "TestData": "generated_symbols.data.gametest.TestData",
    "TestEnvironment": "generated_symbols.data.gametest.test_environment.TestEnvironment",
    "TestInstance": "generated_symbols.data.gametest.TestInstance",
    "TextDisplay": "generated_symbols.data.chat_type.TextDisplay",
    "TextInput": "generated_symbols.data.dialog.input.TextInput",
    "TextureAnimation": "generated_symbols.assets.texture_meta.TextureAnimation",
    "TextureAnimationFrame": "generated_symbols.assets.texture_meta.TextureAnimationFrame",
    "TextureInput": "generated_symbols.assets.shader.post.TextureInput",
    "TextureMaterial": "generated_symbols.assets.model.TextureMaterial",
    "TextureMeta": "generated_symbols.assets.texture_meta.TextureMeta",
    "TheEnd": "generated_symbols.data.worldgen.dimension.biome_source.TheEnd",
    "ThreeLayersFeatureSize": "generated_symbols.data.worldgen.feature.tree.ThreeLayersFeatureSize",
    "ThrownItemPickedUpByEntity": "generated_symbols.data.advancement.trigger.ThrownItemPickedUpByEntity",
    "ThrownItemPickedUpByPlayer": "generated_symbols.data.advancement.trigger.ThrownItemPickedUpByPlayer",
    "TickEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.TickEnchantmentEffect",
    "TileScaling": "generated_symbols.assets.texture_meta.TileScaling",
    "TilingMode": "generated_symbols.data.worldgen.density_function.TilingMode",
    "Time": "generated_symbols.assets.item_definition.Time",
    "TimeCheck": "generated_symbols.data.loot.condition.TimeCheck",
    "TimeMarker": "generated_symbols.data.timeline.TimeMarker",
    "TimeMarkerMap": "generated_symbols.data.timeline.TimeMarkerMap",
    "TimeOfDayTestEnvironment": "generated_symbols.data.gametest.test_environment.TimeOfDayTestEnvironment",
    "TimeSource": "generated_symbols.assets.item_definition.TimeSource",
    "Timeline": "generated_symbols.data.timeline.Timeline",
    "TimelineAttributesTestEnvironment": "generated_symbols.data.gametest.test_environment.TimelineAttributesTestEnvironment",
    "TintSourceType": "generated_symbols.assets.item_definition.TintSourceType",
    "ToggleTooltips": "generated_symbols.data.loot.function.ToggleTooltips",
    "ToggleableDataComponent": "generated_symbols.data.loot.function.ToggleableDataComponent",
    "TradeSet": "generated_symbols.data.trade_set.TradeSet",
    "TranslucentColorAttributeModifier": "generated_symbols.data.worldgen.attribute.modifier.TranslucentColorAttributeModifier",
    "TrapezoidHeightProvider": "generated_symbols.data.worldgen.TrapezoidHeightProvider",
    "TreeConfig": "generated_symbols.data.worldgen.feature.tree.TreeConfig",
    "TreeDecorator": "generated_symbols.data.worldgen.feature.tree.TreeDecorator",
    "TriState": "generated_symbols.data.worldgen.attribute.TriState",
    "TrialSpawnerConfig": "generated_symbols.data.trial_spawner.TrialSpawnerConfig",
    "TrickyTrialsStructureConfig": "generated_symbols.data.worldgen.structure.TrickyTrialsStructureConfig",
    "TridentReturnAccelerationEnchantmentEffect": "generated_symbols.data.enchantment.effect_component.TridentReturnAccelerationEnchantmentEffect",
    "Trigger": "generated_symbols.data.advancement.Trigger",
    "TriggerBase": "generated_symbols.data.advancement.trigger.TriggerBase",
    "TrimMaterialOverrides": "generated_symbols.data.trim.TrimMaterialOverrides",
    "TrimOverride": "generated_symbols.assets.equipment.TrimOverride",
    "TrimPattern": "generated_symbols.data.trim.TrimPattern",
    "TrimPredicate": "generated_symbols.assets.equipment.TrimPredicate",
    "TropicalFishPredicate": "generated_symbols.data.advancement.predicate.TropicalFishPredicate",
    "TrunkPlacer": "generated_symbols.data.worldgen.feature.tree.TrunkPlacer",
    "TtfProvider": "generated_symbols.assets.font.TtfProvider",
    "TwistingVinesConfig": "generated_symbols.data.worldgen.feature.TwistingVinesConfig",
    "TwoArguments": "generated_symbols.data.worldgen.density_function.TwoArguments",
    "TwoLayersFeatureSize": "generated_symbols.data.worldgen.feature.tree.TwoLayersFeatureSize",
    "TypedSlotSource": "generated_symbols.data.slot_source.TypedSlotSource",
    "UnderwaterMagmaConfig": "generated_symbols.data.worldgen.feature.UnderwaterMagmaConfig",
    "Uniform": "generated_symbols.assets.shader.program.Uniform",
    "UniformBlocks": "generated_symbols.assets.shader.post.UniformBlocks",
    "UniformBonusFormula": "generated_symbols.data.loot.function.UniformBonusFormula",
    "UniformHeightProvider": "generated_symbols.data.worldgen.UniformHeightProvider",
    "UniformInt": "generated_symbols.data.worldgen.UniformInt",
    "UniformIntGenerator": "generated_symbols.data.util.UniformIntGenerator",
    "UniformIntProvider": "generated_symbols.data.worldgen.UniformIntProvider",
    "UniformNumberProvider": "generated_symbols.data.number_provider.UniformNumberProvider",
    "UniformType": "generated_symbols.assets.shader.program.UniformType",
    "UniformValue": "generated_symbols.assets.shader.post.UniformValue",
    "UniformValueType": "generated_symbols.assets.shader.post.UniformValueType",
    "UnihexOverrideRange": "generated_symbols.assets.font.UnihexOverrideRange",
    "UnihexProvider": "generated_symbols.assets.font.UnihexProvider",
    "UnknownStorage": "generated_symbols.data.storage.UnknownStorage",
    "UnobstructedPredicate": "generated_symbols.data.worldgen.feature.block_predicate.UnobstructedPredicate",
    "Unstitch": "generated_symbols.assets.atlas.Unstitch",
    "UnstitchRegion": "generated_symbols.assets.atlas.UnstitchRegion",
    "UpwardsBranchingTrunkPlacer": "generated_symbols.data.worldgen.feature.tree.UpwardsBranchingTrunkPlacer",
    "UseCycle": "generated_symbols.assets.item_definition.UseCycle",
    "UseDuration": "generated_symbols.assets.item_definition.UseDuration",
    "UsedEnderEye": "generated_symbols.data.advancement.trigger.UsedEnderEye",
    "UsedTotem": "generated_symbols.data.advancement.trigger.UsedTotem",
    "UsingItem": "generated_symbols.data.advancement.trigger.UsingItem",
    "ValueCheck": "generated_symbols.data.loot.condition.ValueCheck",
    "ValueEffect": "generated_symbols.data.enchantment.effect.ValueEffect",
    "VanillaLayered": "generated_symbols.data.worldgen.dimension.biome_source.VanillaLayered",
    "VegetationPatchConfig": "generated_symbols.data.worldgen.feature.VegetationPatchConfig",
    "VerticalAnchor": "generated_symbols.data.worldgen.VerticalAnchor",
    "VerticalGradientCondition": "generated_symbols.data.worldgen.material_condition.VerticalGradientCondition",
    "ViewEntity": "generated_symbols.assets.item_definition.ViewEntity",
    "VillagerHatType": "generated_symbols.assets.texture_meta.VillagerHatType",
    "VillagerPredicate": "generated_symbols.data.advancement.predicate.VillagerPredicate",
    "VillagerTextureMeta": "generated_symbols.assets.texture_meta.VillagerTextureMeta",
    "WaterCondition": "generated_symbols.data.worldgen.material_condition.WaterCondition",
    "WaterDepthThresholdConfig": "generated_symbols.data.worldgen.feature.decorator.WaterDepthThresholdConfig",
    "WaypointStyle": "generated_symbols.assets.waypoint_style.WaypointStyle",
    "Weather": "generated_symbols.data.gametest.test_environment.Weather",
    "WeatherCheck": "generated_symbols.data.loot.condition.WeatherCheck",
    "WeatherTestEnvironment": "generated_symbols.data.gametest.test_environment.WeatherTestEnvironment",
    "WeightListHeightProvider": "generated_symbols.data.worldgen.WeightListHeightProvider",
    "WeightedBlockStateProvider": "generated_symbols.data.worldgen.feature.block_state_provider.WeightedBlockStateProvider",
    "WeightedElement": "generated_symbols.data.worldgen.template_pool.WeightedElement",
    "WeightedModelVariant": "generated_symbols.assets.block_state_definition.WeightedModelVariant",
    "WeightedNumberProvider": "generated_symbols.data.number_provider.WeightedNumberProvider",
    "WeightedRandomFeatureConfig": "generated_symbols.data.worldgen.feature.WeightedRandomFeatureConfig",
    "WeightedSoundEvent": "generated_symbols.data.util.WeightedSoundEvent",
    "WeirdScaledSampler": "generated_symbols.data.worldgen.density_function.WeirdScaledSampler",
    "WildUpdateStructureConfig": "generated_symbols.data.worldgen.structure.WildUpdateStructureConfig",
    "WingsLayer": "generated_symbols.assets.equipment.WingsLayer",
    "WolfPredicate": "generated_symbols.data.advancement.predicate.WolfPredicate",
    "WolfSounds": "generated_symbols.data.variants.wolf.WolfSounds",
    "WolfVariant": "generated_symbols.data.variants.wolf.WolfVariant",
    "WolfVariantAssetInfo": "generated_symbols.data.variants.wolf.WolfVariantAssetInfo",
    "WoodType": "generated_symbols.assets.item_definition.WoodType",
    "WorldPreset": "generated_symbols.data.worldgen.world_preset.WorldPreset",
    "WouldSurvivePredicate": "generated_symbols.data.worldgen.feature.block_predicate.WouldSurvivePredicate",
    "YAboveCondition": "generated_symbols.data.worldgen.material_condition.YAboveCondition",
    "YClampedGradient": "generated_symbols.data.worldgen.density_function.YClampedGradient",
    "ZombieNautilusModelType": "generated_symbols.data.variants.zombie_nautilus.ZombieNautilusModelType",
    "ZombieNautilusVariant": "generated_symbols.data.variants.zombie_nautilus.ZombieNautilusVariant",
}


def __getattr__(name: str) -> object:
    module_name = _EXPORTS.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    value = getattr(import_module(module_name), name)
    globals()[name] = value
    return value
