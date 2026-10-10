"""
Generated from symbols.json for ::java::data::worldgen::feature::ConfiguredFeature
Local link to file: vanilla_mcdoc/data/worldgen/feature/ConfiguredFeature.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar, Literal

from pydantic import Field

from vanilla_mcdoc.data.worldgen.feature.BlockBlobConfig import BlockBlobConfig
from vanilla_mcdoc.data.worldgen.feature.BlockColumnConfig import BlockColumnConfig
from vanilla_mcdoc.data.worldgen.feature.BlockPileConfig import BlockPileConfig
from vanilla_mcdoc.data.worldgen.feature.ColumnsConfig import ColumnsConfig
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
from vanilla_mcdoc.data.worldgen.feature.tree.FallenTreeConfig import FallenTreeConfig
from vanilla_mcdoc.data.worldgen.feature.tree.TreeConfig import TreeConfig


class ConfiguredFeatureBamboo(ProbabilityConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:bamboo', 'bamboo'] = 'minecraft:bamboo'


class ConfiguredFeatureBlockBlob(BlockBlobConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:block_blob', 'block_blob'] = 'minecraft:block_blob'


class ConfiguredFeatureBlockColumn(BlockColumnConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:block_column', 'block_column'] = 'minecraft:block_column'


class ConfiguredFeatureBlockPile(BlockPileConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:block_pile', 'block_pile'] = 'minecraft:block_pile'


class ConfiguredFeatureCoralClaw(CoralConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:coral_claw', 'coral_claw'] = 'minecraft:coral_claw'


class ConfiguredFeatureCoralTree(CoralConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:coral_tree', 'coral_tree'] = 'minecraft:coral_tree'


class ConfiguredFeatureDeltaFeature(DeltaConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:delta_feature', 'delta_feature'] = 'minecraft:delta_feature'


class ConfiguredFeatureDisk(DiskConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:disk', 'disk'] = 'minecraft:disk'


class ConfiguredFeatureEmeraldOre(EmeraldOreConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:emerald_ore', 'emerald_ore'] = 'minecraft:emerald_ore'


class ConfiguredFeatureEndGateway(EndGatewayConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:end_gateway', 'end_gateway'] = 'minecraft:end_gateway'


class ConfiguredFeatureEndPodium(EndPodiumConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:end_podium', 'end_podium'] = 'minecraft:end_podium'


class ConfiguredFeatureEndSpike(EndSpikeConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:end_spike', 'end_spike'] = 'minecraft:end_spike'


class ConfiguredFeatureFallenTree(FallenTreeConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:fallen_tree', 'fallen_tree'] = 'minecraft:fallen_tree'


class ConfiguredFeatureFillLayer(FillLayerConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:fill_layer', 'fill_layer'] = 'minecraft:fill_layer'


class ConfiguredFeatureFlower(RandomPatchConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:flower', 'flower'] = 'minecraft:flower'


class ConfiguredFeatureFossil(FossilConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:fossil', 'fossil'] = 'minecraft:fossil'


class ConfiguredFeatureGeode(GeodeConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:geode', 'geode'] = 'minecraft:geode'


class ConfiguredFeatureGlowLichen(MultifaceGrowthConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:glow_lichen', 'glow_lichen'] = 'minecraft:glow_lichen'


class ConfiguredFeatureHugeBrownMushroom(HugeMushroomConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:huge_brown_mushroom', 'huge_brown_mushroom'] = 'minecraft:huge_brown_mushroom'


class ConfiguredFeatureHugeFungus(HugeFungusConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:huge_fungus', 'huge_fungus'] = 'minecraft:huge_fungus'


class ConfiguredFeatureHugeRedMushroom(HugeMushroomConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:huge_red_mushroom', 'huge_red_mushroom'] = 'minecraft:huge_red_mushroom'


class ConfiguredFeatureIcePatch(DiskConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:ice_patch', 'ice_patch'] = 'minecraft:ice_patch'


class ConfiguredFeatureIceberg(IcebergConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:iceberg', 'iceberg'] = 'minecraft:iceberg'


class ConfiguredFeatureLake(LakeConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:lake', 'lake'] = 'minecraft:lake'


class ConfiguredFeatureLargeSpeleothem(LargeSpeleothemConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:large_speleothem', 'large_speleothem'] = 'minecraft:large_speleothem'


class ConfiguredFeatureMultifaceGrowth(MultifaceGrowthConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:multiface_growth', 'multiface_growth'] = 'minecraft:multiface_growth'


class ConfiguredFeatureNetherrackReplaceBlobs(NetherrackReplaceBlobsConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:netherrack_replace_blobs', 'netherrack_replace_blobs'] = 'minecraft:netherrack_replace_blobs'


class ConfiguredFeatureNoBonemealFlower(RandomPatchConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:no_bonemeal_flower', 'no_bonemeal_flower'] = 'minecraft:no_bonemeal_flower'


class ConfiguredFeatureNoSurfaceOre(OreConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:no_surface_ore', 'no_surface_ore'] = 'minecraft:no_surface_ore'


class ConfiguredFeatureOre(OreConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:ore', 'ore'] = 'minecraft:ore'


class ConfiguredFeatureOverlay(OverlayConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:overlay', 'overlay'] = 'minecraft:overlay'


class ConfiguredFeatureProjectedRandomPatchySquare(ProjectedSquareConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:projected_random_patchy_square', 'projected_random_patchy_square'] = 'minecraft:projected_random_patchy_square'


class ConfiguredFeatureRandomBooleanSelector(RandomBooleanSelector):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:random_boolean_selector', 'random_boolean_selector'] = 'minecraft:random_boolean_selector'


class ConfiguredFeatureRandomNeighborSpread(RandomNeighborSpreadConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:random_neighbor_spread', 'random_neighbor_spread'] = 'minecraft:random_neighbor_spread'


class ConfiguredFeatureRandomPatch(RandomPatchConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:random_patch', 'random_patch'] = 'minecraft:random_patch'


class ConfiguredFeatureRandomSelector(RandomSelector):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:random_selector', 'random_selector'] = 'minecraft:random_selector'


class ConfiguredFeatureReplaceSingleBlock(ReplaceSingleBlockConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:replace_single_block', 'replace_single_block'] = 'minecraft:replace_single_block'


class ConfiguredFeatureRootSystem(RootSystemConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:root_system', 'root_system'] = 'minecraft:root_system'


class ConfiguredFeatureScatteredOre(OreConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:scattered_ore', 'scattered_ore'] = 'minecraft:scattered_ore'


class ConfiguredFeatureSculkPatch(SculkPatchConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:sculk_patch', 'sculk_patch'] = 'minecraft:sculk_patch'


class ConfiguredFeatureSequence(SequenceConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:sequence', 'sequence'] = 'minecraft:sequence'


class ConfiguredFeatureSimpleBlock(SimpleBlockConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:simple_block', 'simple_block'] = 'minecraft:simple_block'


class ConfiguredFeatureSimpleRandomSelector(SimpleRandomSelectorConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:simple_random_selector', 'simple_random_selector'] = 'minecraft:simple_random_selector'


class ConfiguredFeatureSingleBlockPillar(SingleBlockPillarConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:single_block_pillar', 'single_block_pillar'] = 'minecraft:single_block_pillar'


class ConfiguredFeatureSpeleothem(SpeleothemConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:speleothem', 'speleothem'] = 'minecraft:speleothem'


class ConfiguredFeatureSpeleothemCluster(SpeleothemClusterConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:speleothem_cluster', 'speleothem_cluster'] = 'minecraft:speleothem_cluster'


class ConfiguredFeatureSpike(SpikeConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:spike', 'spike'] = 'minecraft:spike'


class ConfiguredFeatureSpringFeature(SpringConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:spring_feature', 'spring_feature'] = 'minecraft:spring_feature'


class ConfiguredFeatureSteppedColumnCluster(ColumnsConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:stepped_column_cluster', 'stepped_column_cluster'] = 'minecraft:stepped_column_cluster'


class ConfiguredFeatureTemplate(TemplateConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:template', 'template'] = 'minecraft:template'


class ConfiguredFeatureTree(TreeConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:tree', 'tree'] = 'minecraft:tree'


class ConfiguredFeatureUnderwaterMagma(UnderwaterMagmaConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:underwater_magma', 'underwater_magma'] = 'minecraft:underwater_magma'


class ConfiguredFeatureVegetationPatch(VegetationPatchConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:vegetation_patch', 'vegetation_patch'] = 'minecraft:vegetation_patch'


class ConfiguredFeatureWaterloggedVegetationPatch(VegetationPatchConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:waterlogged_vegetation_patch', 'waterlogged_vegetation_patch'] = 'minecraft:waterlogged_vegetation_patch'


class ConfiguredFeatureWeightedRandomSelector(WeightedRandomFeatureConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:weighted_random_selector', 'weighted_random_selector'] = 'minecraft:weighted_random_selector'


type ConfiguredFeature = Annotated[
    ConfiguredFeatureBamboo | ConfiguredFeatureBlockBlob | ConfiguredFeatureBlockColumn | ConfiguredFeatureBlockPile | ConfiguredFeatureCoralClaw | ConfiguredFeatureCoralTree | ConfiguredFeatureDeltaFeature | ConfiguredFeatureDisk | ConfiguredFeatureEmeraldOre | ConfiguredFeatureEndGateway | ConfiguredFeatureEndPodium | ConfiguredFeatureEndSpike | ConfiguredFeatureFallenTree | ConfiguredFeatureFillLayer | ConfiguredFeatureFlower | ConfiguredFeatureFossil | ConfiguredFeatureGeode | ConfiguredFeatureGlowLichen | ConfiguredFeatureHugeBrownMushroom | ConfiguredFeatureHugeFungus | ConfiguredFeatureHugeRedMushroom | ConfiguredFeatureIcePatch | ConfiguredFeatureIceberg | ConfiguredFeatureLake | ConfiguredFeatureLargeSpeleothem | ConfiguredFeatureMultifaceGrowth | ConfiguredFeatureNetherrackReplaceBlobs | ConfiguredFeatureNoBonemealFlower | ConfiguredFeatureNoSurfaceOre | ConfiguredFeatureOre | ConfiguredFeatureOverlay | ConfiguredFeatureProjectedRandomPatchySquare | ConfiguredFeatureRandomBooleanSelector | ConfiguredFeatureRandomNeighborSpread | ConfiguredFeatureRandomPatch | ConfiguredFeatureRandomSelector | ConfiguredFeatureReplaceSingleBlock | ConfiguredFeatureRootSystem | ConfiguredFeatureScatteredOre | ConfiguredFeatureSculkPatch | ConfiguredFeatureSequence | ConfiguredFeatureSimpleBlock | ConfiguredFeatureSimpleRandomSelector | ConfiguredFeatureSingleBlockPillar | ConfiguredFeatureSpeleothem | ConfiguredFeatureSpeleothemCluster | ConfiguredFeatureSpike | ConfiguredFeatureSpringFeature | ConfiguredFeatureSteppedColumnCluster | ConfiguredFeatureTemplate | ConfiguredFeatureTree | ConfiguredFeatureUnderwaterMagma | ConfiguredFeatureVegetationPatch | ConfiguredFeatureWaterloggedVegetationPatch | ConfiguredFeatureWeightedRandomSelector,
    Field(discriminator='type'),
]
