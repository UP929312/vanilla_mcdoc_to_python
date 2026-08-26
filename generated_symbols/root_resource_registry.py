"""Generated root-resource registry for datapack and resource-pack classes."""

from generated_symbols.data.advancement.Advancement import Advancement
from generated_symbols.data.block_transformer.BlockTransformData import BlockTransformData
from generated_symbols.data.chat_type.ChatType import ChatType
from generated_symbols.data.damage_type.DamageType import DamageType
from generated_symbols.data.decorated_pot_pattern.DecoratedPotPattern import DecoratedPotPattern
from generated_symbols.data.dialog.ConfirmationDialog import ConfirmationDialog
from generated_symbols.data.dialog.Dialog import Dialog
from generated_symbols.data.dialog.MultiActionDialog import MultiActionDialog
from generated_symbols.data.dialog.NoticeDialog import NoticeDialog
from generated_symbols.data.dialog.RedirectDialog import RedirectDialog
from generated_symbols.data.dialog.ServerLinksDialog import ServerLinksDialog
from generated_symbols.data.enchantment.Enchantment import Enchantment
from generated_symbols.data.enchantment.provider.ByCostEnchantmentProvider import ByCostEnchantmentProvider
from generated_symbols.data.enchantment.provider.ByCostWithDifficultyEnchantmentProvider import ByCostWithDifficultyEnchantmentProvider
from generated_symbols.data.enchantment.provider.EnchantmentProvider import EnchantmentProvider
from generated_symbols.data.enchantment.provider.SingleProvider import SingleProvider
from generated_symbols.data.gametest.BlockBasedTestInstance import BlockBasedTestInstance
from generated_symbols.data.gametest.FunctionTestInstance import FunctionTestInstance
from generated_symbols.data.gametest.TestInstance import TestInstance
from generated_symbols.data.gametest.test_environment.AllOffTestEnvironment import AllOffTestEnvironment
from generated_symbols.data.gametest.test_environment.ClockTimeTestEnvironment import ClockTimeTestEnvironment
from generated_symbols.data.gametest.test_environment.DifficultyTestEnvironment import DifficultyTestEnvironment
from generated_symbols.data.gametest.test_environment.FunctionTestEnvironment import FunctionTestEnvironment
from generated_symbols.data.gametest.test_environment.GameRulesTestEnvironment import GameRulesTestEnvironment
from generated_symbols.data.gametest.test_environment.TestEnvironment import TestEnvironment
from generated_symbols.data.gametest.test_environment.TimeOfDayTestEnvironment import TimeOfDayTestEnvironment
from generated_symbols.data.gametest.test_environment.TimelineAttributesTestEnvironment import TimelineAttributesTestEnvironment
from generated_symbols.data.gametest.test_environment.WeatherTestEnvironment import WeatherTestEnvironment
from generated_symbols.data.item_modifier.ItemModifierRoot import ItemModifierRoot
from generated_symbols.data.loot.LootTable import LootTable
from generated_symbols.data.number_provider.NumberProvider import NumberProvider
from generated_symbols.data.predicate.Predicate import Predicate
from generated_symbols.data.recipe.Brewing import Brewing
from generated_symbols.data.recipe.CraftingDecoratedPot import CraftingDecoratedPot
from generated_symbols.data.recipe.CraftingDye import CraftingDye
from generated_symbols.data.recipe.CraftingImbue import CraftingImbue
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
from generated_symbols.data.recipe.Recipe import Recipe
from generated_symbols.data.recipe.Smelting import Smelting
from generated_symbols.data.recipe.Smithing import Smithing
from generated_symbols.data.recipe.SmithingTransform import SmithingTransform
from generated_symbols.data.recipe.SmithingTrim import SmithingTrim
from generated_symbols.data.recipe.Stonecutting import Stonecutting
from generated_symbols.data.slot_source.ContentsSlotSource import ContentsSlotSource
from generated_symbols.data.slot_source.FilterSlotSource import FilterSlotSource
from generated_symbols.data.slot_source.GroupSlotSource import GroupSlotSource
from generated_symbols.data.slot_source.LimitCountSlotSource import LimitCountSlotSource
from generated_symbols.data.slot_source.RangeSlotSource import RangeSlotSource
from generated_symbols.data.slot_source.TypedSlotSource import TypedSlotSource
from generated_symbols.data.sulfur_cube_archetype.SulfurCubeArchetype import SulfurCubeArchetype
from generated_symbols.data.timeline.Timeline import Timeline
from generated_symbols.data.trade_set.TradeSet import TradeSet
from generated_symbols.data.trial_spawner.TrialSpawnerConfig import TrialSpawnerConfig
from generated_symbols.data.trim.TrimMaterial import TrimMaterial
from generated_symbols.data.trim.TrimPattern import TrimPattern
from generated_symbols.data.variants.banner_pattern.BannerPattern import BannerPattern
from generated_symbols.data.variants.cat.CatSounds import CatSounds
from generated_symbols.data.variants.cat.CatVariant import CatVariant
from generated_symbols.data.variants.chicken.ChickenSounds import ChickenSounds
from generated_symbols.data.variants.chicken.ChickenVariant import ChickenVariant
from generated_symbols.data.variants.cow.CowSounds import CowSounds
from generated_symbols.data.variants.cow.CowVariant import CowVariant
from generated_symbols.data.variants.frog.FrogVariant import FrogVariant
from generated_symbols.data.variants.instrument.Instrument import Instrument
from generated_symbols.data.variants.jukebox_song.JukeboxSong import JukeboxSong
from generated_symbols.data.variants.painting.PaintingVariant import PaintingVariant
from generated_symbols.data.variants.pig.PigSounds import PigSounds
from generated_symbols.data.variants.pig.PigVariant import PigVariant
from generated_symbols.data.variants.wolf.WolfSounds import WolfSounds
from generated_symbols.data.variants.wolf.WolfVariant import WolfVariant
from generated_symbols.data.variants.zombie_nautilus.ZombieNautilusVariant import ZombieNautilusVariant
from generated_symbols.data.villager_trade.VillagerTrade import VillagerTrade
from generated_symbols.data.worldgen.biome.Biome import Biome
from generated_symbols.data.worldgen.carver.CanyonConfig import CanyonConfig
from generated_symbols.data.worldgen.carver.CaveConfig import CaveConfig
from generated_symbols.data.worldgen.carver.ConfiguredCarver import ConfiguredCarver
from generated_symbols.data.worldgen.density_function.DensityFunction import DensityFunction
from generated_symbols.data.worldgen.dimension.Dimension import Dimension
from generated_symbols.data.worldgen.dimension.DimensionType import DimensionType
from generated_symbols.data.worldgen.dimension.biome_source.MultiNoiseBiomeSourceParameterList import MultiNoiseBiomeSourceParameterList
from generated_symbols.data.worldgen.dimension.biome_source.NoiseParameters import NoiseParameters
from generated_symbols.data.worldgen.feature.BlockBlobConfig import BlockBlobConfig
from generated_symbols.data.worldgen.feature.BlockColumnConfig import BlockColumnConfig
from generated_symbols.data.worldgen.feature.BlockPileConfig import BlockPileConfig
from generated_symbols.data.worldgen.feature.ColumnsConfig import ColumnsConfig
from generated_symbols.data.worldgen.feature.ConfiguredFeature import ConfiguredFeature
from generated_symbols.data.worldgen.feature.CoralConfig import CoralConfig
from generated_symbols.data.worldgen.feature.DecoratedConfig import DecoratedConfig
from generated_symbols.data.worldgen.feature.DeltaConfig import DeltaConfig
from generated_symbols.data.worldgen.feature.DiskConfig import DiskConfig
from generated_symbols.data.worldgen.feature.EmeraldOreConfig import EmeraldOreConfig
from generated_symbols.data.worldgen.feature.EndGatewayConfig import EndGatewayConfig
from generated_symbols.data.worldgen.feature.EndPodiumConfig import EndPodiumConfig
from generated_symbols.data.worldgen.feature.EndSpikeConfig import EndSpikeConfig
from generated_symbols.data.worldgen.feature.FillLayerConfig import FillLayerConfig
from generated_symbols.data.worldgen.feature.ForestRockConfig import ForestRockConfig
from generated_symbols.data.worldgen.feature.FossilConfig import FossilConfig
from generated_symbols.data.worldgen.feature.GeodeConfig import GeodeConfig
from generated_symbols.data.worldgen.feature.GrowingPlantConfig import GrowingPlantConfig
from generated_symbols.data.worldgen.feature.HugeFungusConfig import HugeFungusConfig
from generated_symbols.data.worldgen.feature.HugeMushroomConfig import HugeMushroomConfig
from generated_symbols.data.worldgen.feature.IcebergConfig import IcebergConfig
from generated_symbols.data.worldgen.feature.LakeConfig import LakeConfig
from generated_symbols.data.worldgen.feature.LargeDripstoneConfig import LargeDripstoneConfig
from generated_symbols.data.worldgen.feature.MultifaceGrowthConfig import MultifaceGrowthConfig
from generated_symbols.data.worldgen.feature.NetherForestVegetationConfig import NetherForestVegetationConfig
from generated_symbols.data.worldgen.feature.NetherrackReplaceBlobsConfig import NetherrackReplaceBlobsConfig
from generated_symbols.data.worldgen.feature.OreConfig import OreConfig
from generated_symbols.data.worldgen.feature.OverlayConfig import OverlayConfig
from generated_symbols.data.worldgen.feature.ProbabilityConfig import ProbabilityConfig
from generated_symbols.data.worldgen.feature.ProjectedSquareConfig import ProjectedSquareConfig
from generated_symbols.data.worldgen.feature.RandomBooleanSelector import RandomBooleanSelector
from generated_symbols.data.worldgen.feature.RandomNeighborSpreadConfig import RandomNeighborSpreadConfig
from generated_symbols.data.worldgen.feature.RandomPatchConfig import RandomPatchConfig
from generated_symbols.data.worldgen.feature.RandomSelector import RandomSelector
from generated_symbols.data.worldgen.feature.ReplaceSingleBlockConfig import ReplaceSingleBlockConfig
from generated_symbols.data.worldgen.feature.RootSystemConfig import RootSystemConfig
from generated_symbols.data.worldgen.feature.SculkPatchConfig import SculkPatchConfig
from generated_symbols.data.worldgen.feature.SeaPickleConfig import SeaPickleConfig
from generated_symbols.data.worldgen.feature.SequenceConfig import SequenceConfig
from generated_symbols.data.worldgen.feature.SimpleBlockConfig import SimpleBlockConfig
from generated_symbols.data.worldgen.feature.SimpleRandomSelectorConfig import SimpleRandomSelectorConfig
from generated_symbols.data.worldgen.feature.SingleBlockPillarConfig import SingleBlockPillarConfig
from generated_symbols.data.worldgen.feature.SmallDripstoneConfig import SmallDripstoneConfig
from generated_symbols.data.worldgen.feature.SpeleothemClusterConfig import SpeleothemClusterConfig
from generated_symbols.data.worldgen.feature.SpeleothemConfig import SpeleothemConfig
from generated_symbols.data.worldgen.feature.SpikeConfig import SpikeConfig
from generated_symbols.data.worldgen.feature.SpringConfig import SpringConfig
from generated_symbols.data.worldgen.feature.TemplateConfig import TemplateConfig
from generated_symbols.data.worldgen.feature.TwistingVinesConfig import TwistingVinesConfig
from generated_symbols.data.worldgen.feature.UnderwaterMagmaConfig import UnderwaterMagmaConfig
from generated_symbols.data.worldgen.feature.VegetationPatchConfig import VegetationPatchConfig
from generated_symbols.data.worldgen.feature.WeightedRandomFeatureConfig import WeightedRandomFeatureConfig
from generated_symbols.data.worldgen.feature.placement.PlacedFeature import PlacedFeature
from generated_symbols.data.worldgen.feature.tree.FallenTreeConfig import FallenTreeConfig
from generated_symbols.data.worldgen.feature.tree.TreeConfig import TreeConfig
from generated_symbols.data.worldgen.material_condition.BiomeCondition import BiomeCondition
from generated_symbols.data.worldgen.material_condition.MaterialCondition import MaterialCondition
from generated_symbols.data.worldgen.material_condition.NoiseThresholdCondition import NoiseThresholdCondition
from generated_symbols.data.worldgen.material_condition.NotCondition import NotCondition
from generated_symbols.data.worldgen.material_condition.StoneDepthCondition import StoneDepthCondition
from generated_symbols.data.worldgen.material_condition.VerticalGradientCondition import VerticalGradientCondition
from generated_symbols.data.worldgen.material_condition.WaterCondition import WaterCondition
from generated_symbols.data.worldgen.material_condition.YAboveCondition import YAboveCondition
from generated_symbols.data.worldgen.material_rule.BlockRule import BlockRule
from generated_symbols.data.worldgen.material_rule.ConditionRule import ConditionRule
from generated_symbols.data.worldgen.material_rule.MaterialRule import MaterialRule
from generated_symbols.data.worldgen.material_rule.OreVeinifier import OreVeinifier
from generated_symbols.data.worldgen.material_rule.SequenceRule import SequenceRule
from generated_symbols.data.worldgen.noise_settings.NoiseGeneratorSettings import NoiseGeneratorSettings
from generated_symbols.data.worldgen.processor_list.ProcessorList import ProcessorList
from generated_symbols.data.worldgen.structure.BuriedTreasure import BuriedTreasure
from generated_symbols.data.worldgen.structure.Jigsaw import Jigsaw
from generated_symbols.data.worldgen.structure.Mineshaft import Mineshaft
from generated_symbols.data.worldgen.structure.NetherFossil import NetherFossil
from generated_symbols.data.worldgen.structure.OceanRuin import OceanRuin
from generated_symbols.data.worldgen.structure.RuinedPortal import RuinedPortal
from generated_symbols.data.worldgen.structure.Shipwreck import Shipwreck
from generated_symbols.data.worldgen.structure.Structure import Structure
from generated_symbols.data.worldgen.structure_set.StructureSet import StructureSet
from generated_symbols.data.worldgen.template_pool.TemplatePool import TemplatePool
from generated_symbols.data.worldgen.world_preset.FlatGeneratorPreset import FlatGeneratorPreset
from generated_symbols.data.worldgen.world_preset.WorldPreset import WorldPreset
from generated_symbols.assets.atlas.Atlas import Atlas
from generated_symbols.assets.block_state_definition.BlockStateDefinition import BlockStateDefinition
from generated_symbols.assets.credits.Credits import Credits
from generated_symbols.assets.equipment.Equipment import Equipment
from generated_symbols.assets.font.Font import Font
from generated_symbols.assets.gpu_warnlist.GpuWarnlist import GpuWarnlist
from generated_symbols.assets.item_definition.ItemDefinition import ItemDefinition
from generated_symbols.assets.lang.Lang import Lang
from generated_symbols.assets.lang.LangDeprecated import LangDeprecated
from generated_symbols.assets.model.Model import Model
from generated_symbols.assets.particle.Particle import Particle
from generated_symbols.assets.regional_compliancies.RegionalCompliancies import RegionalCompliancies
from generated_symbols.assets.shader.post.PostEffect import PostEffect
from generated_symbols.assets.shader.program.ShaderProgram import ShaderProgram
from generated_symbols.assets.sounds.Sounds import Sounds
from generated_symbols.assets.texture_meta.TextureMeta import TextureMeta
from generated_symbols.assets.waypoint_style.WaypointStyle import WaypointStyle

root_datapack_classes = (
    Advancement,
    BlockTransformData,
    ChatType,
    DamageType,
    DecoratedPotPattern,
    ConfirmationDialog,
    Dialog,
    MultiActionDialog,
    NoticeDialog,
    RedirectDialog,
    ServerLinksDialog,
    Enchantment,
    ByCostEnchantmentProvider,
    ByCostWithDifficultyEnchantmentProvider,
    EnchantmentProvider,
    SingleProvider,
    BlockBasedTestInstance,
    FunctionTestInstance,
    TestInstance,
    AllOffTestEnvironment,
    ClockTimeTestEnvironment,
    DifficultyTestEnvironment,
    FunctionTestEnvironment,
    GameRulesTestEnvironment,
    TestEnvironment,
    TimeOfDayTestEnvironment,
    TimelineAttributesTestEnvironment,
    WeatherTestEnvironment,
    ItemModifierRoot,
    LootTable,
    NumberProvider,
    Predicate,
    Brewing,
    CraftingDecoratedPot,
    CraftingDye,
    CraftingImbue,
    CraftingShaped,
    CraftingShapeless,
    CraftingSpecialBannerDuplicate,
    CraftingSpecialBookCloning,
    CraftingSpecialFireworkRocket,
    CraftingSpecialFireworkStar,
    CraftingSpecialFireworkStarFade,
    CraftingSpecialMapExtending,
    CraftingSpecialShieldDecoration,
    CraftingTransmute,
    Recipe,
    Smelting,
    Smithing,
    SmithingTransform,
    SmithingTrim,
    Stonecutting,
    ContentsSlotSource,
    FilterSlotSource,
    GroupSlotSource,
    LimitCountSlotSource,
    RangeSlotSource,
    TypedSlotSource,
    SulfurCubeArchetype,
    Timeline,
    TradeSet,
    TrialSpawnerConfig,
    TrimMaterial,
    TrimPattern,
    BannerPattern,
    CatSounds,
    CatVariant,
    ChickenSounds,
    ChickenVariant,
    CowSounds,
    CowVariant,
    FrogVariant,
    Instrument,
    JukeboxSong,
    PaintingVariant,
    PigSounds,
    PigVariant,
    WolfSounds,
    WolfVariant,
    ZombieNautilusVariant,
    VillagerTrade,
    Biome,
    CanyonConfig,
    CaveConfig,
    ConfiguredCarver,
    DensityFunction,
    Dimension,
    DimensionType,
    MultiNoiseBiomeSourceParameterList,
    NoiseParameters,
    BlockBlobConfig,
    BlockColumnConfig,
    BlockPileConfig,
    ColumnsConfig,
    ConfiguredFeature,
    CoralConfig,
    DecoratedConfig,
    DeltaConfig,
    DiskConfig,
    EmeraldOreConfig,
    EndGatewayConfig,
    EndPodiumConfig,
    EndSpikeConfig,
    FillLayerConfig,
    ForestRockConfig,
    FossilConfig,
    GeodeConfig,
    GrowingPlantConfig,
    HugeFungusConfig,
    HugeMushroomConfig,
    IcebergConfig,
    LakeConfig,
    LargeDripstoneConfig,
    MultifaceGrowthConfig,
    NetherForestVegetationConfig,
    NetherrackReplaceBlobsConfig,
    OreConfig,
    OverlayConfig,
    ProbabilityConfig,
    ProjectedSquareConfig,
    RandomBooleanSelector,
    RandomNeighborSpreadConfig,
    RandomPatchConfig,
    RandomSelector,
    ReplaceSingleBlockConfig,
    RootSystemConfig,
    SculkPatchConfig,
    SeaPickleConfig,
    SequenceConfig,
    SimpleBlockConfig,
    SimpleRandomSelectorConfig,
    SingleBlockPillarConfig,
    SmallDripstoneConfig,
    SpeleothemClusterConfig,
    SpeleothemConfig,
    SpikeConfig,
    SpringConfig,
    TemplateConfig,
    TwistingVinesConfig,
    UnderwaterMagmaConfig,
    VegetationPatchConfig,
    WeightedRandomFeatureConfig,
    PlacedFeature,
    FallenTreeConfig,
    TreeConfig,
    BiomeCondition,
    MaterialCondition,
    NoiseThresholdCondition,
    NotCondition,
    StoneDepthCondition,
    VerticalGradientCondition,
    WaterCondition,
    YAboveCondition,
    BlockRule,
    ConditionRule,
    MaterialRule,
    OreVeinifier,
    SequenceRule,
    NoiseGeneratorSettings,
    ProcessorList,
    BuriedTreasure,
    Jigsaw,
    Mineshaft,
    NetherFossil,
    OceanRuin,
    RuinedPortal,
    Shipwreck,
    Structure,
    StructureSet,
    TemplatePool,
    FlatGeneratorPreset,
    WorldPreset,
)

root_resource_pack_classes = (
    Atlas,
    BlockStateDefinition,
    Credits,
    Equipment,
    Font,
    GpuWarnlist,
    ItemDefinition,
    Lang,
    LangDeprecated,
    Model,
    Particle,
    RegionalCompliancies,
    PostEffect,
    ShaderProgram,
    Sounds,
    TextureMeta,
    WaypointStyle,
)

