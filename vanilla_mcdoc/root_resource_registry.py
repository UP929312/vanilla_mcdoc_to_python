"""Generated root-resource registry for datapack and resource-pack classes."""

from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.block_sound_set.BlockSoundSet import BlockSoundSet
from vanilla_mcdoc.data.block_transformer.BlockTransformData import BlockTransformData
from vanilla_mcdoc.data.chat_type.ChatType import ChatType
from vanilla_mcdoc.data.damage_type.DamageType import DamageType
from vanilla_mcdoc.data.decorated_pot_pattern.DecoratedPotPattern import DecoratedPotPattern
from vanilla_mcdoc.data.dialog.ConfirmationDialog import ConfirmationDialog
from vanilla_mcdoc.data.dialog.Dialog import Dialog
from vanilla_mcdoc.data.dialog.MultiActionDialog import MultiActionDialog
from vanilla_mcdoc.data.dialog.NoticeDialog import NoticeDialog
from vanilla_mcdoc.data.dialog.RedirectDialog import RedirectDialog
from vanilla_mcdoc.data.dialog.ServerLinksDialog import ServerLinksDialog
from vanilla_mcdoc.data.enchantment.Enchantment import Enchantment
from vanilla_mcdoc.data.enchantment.provider.ByCostEnchantmentProvider import ByCostEnchantmentProvider
from vanilla_mcdoc.data.enchantment.provider.ByCostWithDifficultyEnchantmentProvider import ByCostWithDifficultyEnchantmentProvider
from vanilla_mcdoc.data.enchantment.provider.EnchantmentProvider import EnchantmentProvider
from vanilla_mcdoc.data.enchantment.provider.SingleProvider import SingleProvider
from vanilla_mcdoc.data.gametest.BlockBasedTestInstance import BlockBasedTestInstance
from vanilla_mcdoc.data.gametest.FunctionTestInstance import FunctionTestInstance
from vanilla_mcdoc.data.gametest.TestInstance import TestInstance
from vanilla_mcdoc.data.gametest.test_environment.AllOffTestEnvironment import AllOffTestEnvironment
from vanilla_mcdoc.data.gametest.test_environment.ClockTimeTestEnvironment import ClockTimeTestEnvironment
from vanilla_mcdoc.data.gametest.test_environment.DifficultyTestEnvironment import DifficultyTestEnvironment
from vanilla_mcdoc.data.gametest.test_environment.FunctionTestEnvironment import FunctionTestEnvironment
from vanilla_mcdoc.data.gametest.test_environment.GameRulesTestEnvironment import GameRulesTestEnvironment
from vanilla_mcdoc.data.gametest.test_environment.TestEnvironment import TestEnvironment
from vanilla_mcdoc.data.gametest.test_environment.TimelineAttributesTestEnvironment import TimelineAttributesTestEnvironment
from vanilla_mcdoc.data.gametest.test_environment.WeatherTestEnvironment import WeatherTestEnvironment
from vanilla_mcdoc.data.item_modifier.ItemModifierRoot import ItemModifierRoot
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.number_provider.context_float.ContextFloatProvider import ContextFloatProvider
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProvider
from vanilla_mcdoc.data.predicate.Predicate import Predicate
from vanilla_mcdoc.data.recipe.Brewing import Brewing
from vanilla_mcdoc.data.recipe.CraftingDecoratedPot import CraftingDecoratedPot
from vanilla_mcdoc.data.recipe.CraftingDye import CraftingDye
from vanilla_mcdoc.data.recipe.CraftingImbue import CraftingImbue
from vanilla_mcdoc.data.recipe.CraftingShaped import CraftingShaped
from vanilla_mcdoc.data.recipe.CraftingShapeless import CraftingShapeless
from vanilla_mcdoc.data.recipe.CraftingSpecialBannerDuplicate import CraftingSpecialBannerDuplicate
from vanilla_mcdoc.data.recipe.CraftingSpecialBookCloning import CraftingSpecialBookCloning
from vanilla_mcdoc.data.recipe.CraftingSpecialFireworkRocket import CraftingSpecialFireworkRocket
from vanilla_mcdoc.data.recipe.CraftingSpecialFireworkStar import CraftingSpecialFireworkStar
from vanilla_mcdoc.data.recipe.CraftingSpecialFireworkStarFade import CraftingSpecialFireworkStarFade
from vanilla_mcdoc.data.recipe.CraftingSpecialMapExtending import CraftingSpecialMapExtending
from vanilla_mcdoc.data.recipe.CraftingSpecialShieldDecoration import CraftingSpecialShieldDecoration
from vanilla_mcdoc.data.recipe.CraftingTransmute import CraftingTransmute
from vanilla_mcdoc.data.recipe.Recipe import Recipe
from vanilla_mcdoc.data.recipe.Smelting import Smelting
from vanilla_mcdoc.data.recipe.SmithingTransform import SmithingTransform
from vanilla_mcdoc.data.recipe.SmithingTrim import SmithingTrim
from vanilla_mcdoc.data.recipe.Stonecutting import Stonecutting
from vanilla_mcdoc.data.slot_source.ContentsSlotSource import ContentsSlotSource
from vanilla_mcdoc.data.slot_source.FilterSlotSource import FilterSlotSource
from vanilla_mcdoc.data.slot_source.GroupSlotSource import GroupSlotSource
from vanilla_mcdoc.data.slot_source.LimitCountSlotSource import LimitCountSlotSource
from vanilla_mcdoc.data.slot_source.RangeSlotSource import RangeSlotSource
from vanilla_mcdoc.data.slot_source.TypedSlotSource import TypedSlotSource
from vanilla_mcdoc.data.sulfur_cube_archetype.SulfurCubeArchetype import SulfurCubeArchetype
from vanilla_mcdoc.data.timeline.Timeline import Timeline
from vanilla_mcdoc.data.trade_set.TradeSet import TradeSet
from vanilla_mcdoc.data.trial_spawner.TrialSpawnerConfig import TrialSpawnerConfig
from vanilla_mcdoc.data.trim.TrimMaterial import TrimMaterial
from vanilla_mcdoc.data.trim.TrimPattern import TrimPattern
from vanilla_mcdoc.data.variants.banner_pattern.BannerPattern import BannerPattern
from vanilla_mcdoc.data.variants.cat.CatSounds import CatSounds
from vanilla_mcdoc.data.variants.cat.CatVariant import CatVariant
from vanilla_mcdoc.data.variants.chicken.ChickenSounds import ChickenSounds
from vanilla_mcdoc.data.variants.chicken.ChickenVariant import ChickenVariant
from vanilla_mcdoc.data.variants.cow.CowSounds import CowSounds
from vanilla_mcdoc.data.variants.cow.CowVariant import CowVariant
from vanilla_mcdoc.data.variants.frog.FrogVariant import FrogVariant
from vanilla_mcdoc.data.variants.instrument.Instrument import Instrument
from vanilla_mcdoc.data.variants.jukebox_song.JukeboxSong import JukeboxSong
from vanilla_mcdoc.data.variants.painting.PaintingVariant import PaintingVariant
from vanilla_mcdoc.data.variants.pig.PigSounds import PigSounds
from vanilla_mcdoc.data.variants.pig.PigVariant import PigVariant
from vanilla_mcdoc.data.variants.wolf.WolfSounds import WolfSounds
from vanilla_mcdoc.data.variants.wolf.WolfVariant import WolfVariant
from vanilla_mcdoc.data.variants.zombie_nautilus.ZombieNautilusVariant import ZombieNautilusVariant
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.data.worldgen.biome.Biome import Biome
from vanilla_mcdoc.data.worldgen.carver.CanyonConfig import CanyonConfig
from vanilla_mcdoc.data.worldgen.carver.CaveConfig import CaveConfig
from vanilla_mcdoc.data.worldgen.carver.ConfiguredCarver import ConfiguredCarver
from vanilla_mcdoc.data.worldgen.density_function.DensityFunction import DensityFunction
from vanilla_mcdoc.data.worldgen.dimension.Dimension import Dimension
from vanilla_mcdoc.data.worldgen.dimension.DimensionType import DimensionType
from vanilla_mcdoc.data.worldgen.dimension.biome_source.MultiNoiseBiomeSourceParameterList import MultiNoiseBiomeSourceParameterList
from vanilla_mcdoc.data.worldgen.dimension.biome_source.NoiseParameters import NoiseParameters
from vanilla_mcdoc.data.worldgen.feature.BlockBlobConfig import BlockBlobConfig
from vanilla_mcdoc.data.worldgen.feature.BlockColumnConfig import BlockColumnConfig
from vanilla_mcdoc.data.worldgen.feature.BlockPileConfig import BlockPileConfig
from vanilla_mcdoc.data.worldgen.feature.ColumnsConfig import ColumnsConfig
from vanilla_mcdoc.data.worldgen.feature.ConfiguredFeature import ConfiguredFeature
from vanilla_mcdoc.data.worldgen.feature.CoralConfig import CoralConfig
from vanilla_mcdoc.data.worldgen.feature.DeltaConfig import DeltaConfig
from vanilla_mcdoc.data.worldgen.feature.DiskConfig import DiskConfig
from vanilla_mcdoc.data.worldgen.feature.EmeraldOreConfig import EmeraldOreConfig
from vanilla_mcdoc.data.worldgen.feature.EndGatewayConfig import EndGatewayConfig
from vanilla_mcdoc.data.worldgen.feature.EndPodiumConfig import EndPodiumConfig
from vanilla_mcdoc.data.worldgen.feature.EndSpikeConfig import EndSpikeConfig
from vanilla_mcdoc.data.worldgen.feature.FillLayerConfig import FillLayerConfig
from vanilla_mcdoc.data.worldgen.feature.FossilConfig import FossilConfig
from vanilla_mcdoc.data.worldgen.feature.GeodeConfig import GeodeConfig
from vanilla_mcdoc.data.worldgen.feature.HugeFungusConfig import HugeFungusConfig
from vanilla_mcdoc.data.worldgen.feature.HugeMushroomConfig import HugeMushroomConfig
from vanilla_mcdoc.data.worldgen.feature.IcebergConfig import IcebergConfig
from vanilla_mcdoc.data.worldgen.feature.LakeConfig import LakeConfig
from vanilla_mcdoc.data.worldgen.feature.LargeSpeleothemConfig import LargeSpeleothemConfig
from vanilla_mcdoc.data.worldgen.feature.MultifaceGrowthConfig import MultifaceGrowthConfig
from vanilla_mcdoc.data.worldgen.feature.NetherrackReplaceBlobsConfig import NetherrackReplaceBlobsConfig
from vanilla_mcdoc.data.worldgen.feature.OreConfig import OreConfig
from vanilla_mcdoc.data.worldgen.feature.OverlayConfig import OverlayConfig
from vanilla_mcdoc.data.worldgen.feature.ProbabilityConfig import ProbabilityConfig
from vanilla_mcdoc.data.worldgen.feature.ProjectedSquareConfig import ProjectedSquareConfig
from vanilla_mcdoc.data.worldgen.feature.RandomBooleanSelector import RandomBooleanSelector
from vanilla_mcdoc.data.worldgen.feature.RandomNeighborSpreadConfig import RandomNeighborSpreadConfig
from vanilla_mcdoc.data.worldgen.feature.RandomPatchConfig import RandomPatchConfig
from vanilla_mcdoc.data.worldgen.feature.RandomSelector import RandomSelector
from vanilla_mcdoc.data.worldgen.feature.ReplaceSingleBlockConfig import ReplaceSingleBlockConfig
from vanilla_mcdoc.data.worldgen.feature.RootSystemConfig import RootSystemConfig
from vanilla_mcdoc.data.worldgen.feature.SculkPatchConfig import SculkPatchConfig
from vanilla_mcdoc.data.worldgen.feature.SequenceConfig import SequenceConfig
from vanilla_mcdoc.data.worldgen.feature.SimpleBlockConfig import SimpleBlockConfig
from vanilla_mcdoc.data.worldgen.feature.SimpleRandomSelectorConfig import SimpleRandomSelectorConfig
from vanilla_mcdoc.data.worldgen.feature.SingleBlockPillarConfig import SingleBlockPillarConfig
from vanilla_mcdoc.data.worldgen.feature.SpeleothemClusterConfig import SpeleothemClusterConfig
from vanilla_mcdoc.data.worldgen.feature.SpeleothemConfig import SpeleothemConfig
from vanilla_mcdoc.data.worldgen.feature.SpikeConfig import SpikeConfig
from vanilla_mcdoc.data.worldgen.feature.SpringConfig import SpringConfig
from vanilla_mcdoc.data.worldgen.feature.TemplateConfig import TemplateConfig
from vanilla_mcdoc.data.worldgen.feature.UnderwaterMagmaConfig import UnderwaterMagmaConfig
from vanilla_mcdoc.data.worldgen.feature.VegetationPatchConfig import VegetationPatchConfig
from vanilla_mcdoc.data.worldgen.feature.WeightedRandomFeatureConfig import WeightedRandomFeatureConfig
from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider
from vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeature import PlacedFeature
from vanilla_mcdoc.data.worldgen.feature.tree.FallenTreeConfig import FallenTreeConfig
from vanilla_mcdoc.data.worldgen.feature.tree.TreeConfig import TreeConfig
from vanilla_mcdoc.data.worldgen.material_condition.BiomeCondition import BiomeCondition
from vanilla_mcdoc.data.worldgen.material_condition.MaterialCondition import MaterialCondition
from vanilla_mcdoc.data.worldgen.material_condition.NoiseThresholdCondition import NoiseThresholdCondition
from vanilla_mcdoc.data.worldgen.material_condition.NotCondition import NotCondition
from vanilla_mcdoc.data.worldgen.material_condition.StoneDepthCondition import StoneDepthCondition
from vanilla_mcdoc.data.worldgen.material_condition.VerticalGradientCondition import VerticalGradientCondition
from vanilla_mcdoc.data.worldgen.material_condition.WaterCondition import WaterCondition
from vanilla_mcdoc.data.worldgen.material_condition.YAboveCondition import YAboveCondition
from vanilla_mcdoc.data.worldgen.material_rule.BlockRule import BlockRule
from vanilla_mcdoc.data.worldgen.material_rule.ConditionRule import ConditionRule
from vanilla_mcdoc.data.worldgen.material_rule.MaterialRule import MaterialRule
from vanilla_mcdoc.data.worldgen.material_rule.OreVeinifier import OreVeinifier
from vanilla_mcdoc.data.worldgen.material_rule.SequenceRule import SequenceRule
from vanilla_mcdoc.data.worldgen.noise_settings.NoiseGeneratorSettings import NoiseGeneratorSettings
from vanilla_mcdoc.data.worldgen.processor_list.ProcessorList import ProcessorList
from vanilla_mcdoc.data.worldgen.structure.BuriedTreasure import BuriedTreasure
from vanilla_mcdoc.data.worldgen.structure.Jigsaw import Jigsaw
from vanilla_mcdoc.data.worldgen.structure.Mineshaft import Mineshaft
from vanilla_mcdoc.data.worldgen.structure.NetherFossil import NetherFossil
from vanilla_mcdoc.data.worldgen.structure.OceanRuin import OceanRuin
from vanilla_mcdoc.data.worldgen.structure.RuinedPortal import RuinedPortal
from vanilla_mcdoc.data.worldgen.structure.Shipwreck import Shipwreck
from vanilla_mcdoc.data.worldgen.structure.Structure import Structure
from vanilla_mcdoc.data.worldgen.structure_set.StructureSet import StructureSet
from vanilla_mcdoc.data.worldgen.template_pool.TemplatePool import TemplatePool
from vanilla_mcdoc.data.worldgen.world_preset.FlatGeneratorPreset import FlatGeneratorPreset
from vanilla_mcdoc.data.worldgen.world_preset.WorldPreset import WorldPreset
from vanilla_mcdoc.assets.atlas.Atlas import Atlas
from vanilla_mcdoc.assets.block_state_definition.BlockStateDefinition import BlockStateDefinition
from vanilla_mcdoc.assets.credits.Credits import Credits
from vanilla_mcdoc.assets.equipment.Equipment import Equipment
from vanilla_mcdoc.assets.font.Font import Font
from vanilla_mcdoc.assets.gpu_warnlist.GpuWarnlist import GpuWarnlist
from vanilla_mcdoc.assets.item_definition.ItemDefinition import ItemDefinition
from vanilla_mcdoc.assets.lang.Lang import Lang
from vanilla_mcdoc.assets.lang.LangDeprecated import LangDeprecated
from vanilla_mcdoc.assets.model.Model import Model
from vanilla_mcdoc.assets.particle.Particle import Particle
from vanilla_mcdoc.assets.regional_compliancies.RegionalCompliancies import RegionalCompliancies
from vanilla_mcdoc.assets.shader.post.PostEffect import PostEffect
from vanilla_mcdoc.assets.shader.program.ShaderProgram import ShaderProgram
from vanilla_mcdoc.assets.sounds.Sounds import Sounds
from vanilla_mcdoc.assets.texture_meta.TextureMeta import TextureMeta
from vanilla_mcdoc.assets.waypoint_style.WaypointStyle import WaypointStyle

ROOT_DATAPACK_CLASSES = (
    Advancement,
    BlockSoundSet,
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
    TimelineAttributesTestEnvironment,
    WeatherTestEnvironment,
    ItemModifierRoot,
    LootTable,
    ContextFloatProvider,
    ContextIntProvider,
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
    DeltaConfig,
    DiskConfig,
    EmeraldOreConfig,
    EndGatewayConfig,
    EndPodiumConfig,
    EndSpikeConfig,
    FillLayerConfig,
    FossilConfig,
    GeodeConfig,
    HugeFungusConfig,
    HugeMushroomConfig,
    IcebergConfig,
    LakeConfig,
    LargeSpeleothemConfig,
    MultifaceGrowthConfig,
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
    SequenceConfig,
    SimpleBlockConfig,
    SimpleRandomSelectorConfig,
    SingleBlockPillarConfig,
    SpeleothemClusterConfig,
    SpeleothemConfig,
    SpikeConfig,
    SpringConfig,
    TemplateConfig,
    UnderwaterMagmaConfig,
    VegetationPatchConfig,
    WeightedRandomFeatureConfig,
    BlockStateProvider,
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

ROOT_RESOURCE_PACK_CLASSES = (
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

