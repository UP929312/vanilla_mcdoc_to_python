"""
Generated from symbols.json for ::java::data::worldgen::feature::ConfiguredFeature
Local link to file: generated_symbols/data/worldgen/feature/ConfiguredFeature.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import ClassVar, Literal

from generated_symbols.data.worldgen.feature.BlockBlobConfig import BlockBlobConfig
from generated_symbols.data.worldgen.feature.BlockColumnConfig import BlockColumnConfig
from generated_symbols.data.worldgen.feature.BlockPileConfig import BlockPileConfig
from generated_symbols.data.worldgen.feature.ColumnsConfig import ColumnsConfig
from generated_symbols.data.worldgen.feature.CoralConfig import CoralConfig
from generated_symbols.data.worldgen.feature.DeltaConfig import DeltaConfig
from generated_symbols.data.worldgen.feature.DiskConfig import DiskConfig
from generated_symbols.data.worldgen.feature.EmeraldOreConfig import EmeraldOreConfig
from generated_symbols.data.worldgen.feature.EndGatewayConfig import EndGatewayConfig
from generated_symbols.data.worldgen.feature.EndPodiumConfig import EndPodiumConfig
from generated_symbols.data.worldgen.feature.EndSpikeConfig import EndSpikeConfig
from generated_symbols.data.worldgen.feature.FillLayerConfig import FillLayerConfig
from generated_symbols.data.worldgen.feature.FossilConfig import FossilConfig
from generated_symbols.data.worldgen.feature.GeodeConfig import GeodeConfig
from generated_symbols.data.worldgen.feature.HugeFungusConfig import HugeFungusConfig
from generated_symbols.data.worldgen.feature.HugeMushroomConfig import HugeMushroomConfig
from generated_symbols.data.worldgen.feature.IcebergConfig import IcebergConfig
from generated_symbols.data.worldgen.feature.LakeConfig import LakeConfig
from generated_symbols.data.worldgen.feature.LargeDripstoneConfig import LargeDripstoneConfig
from generated_symbols.data.worldgen.feature.MultifaceGrowthConfig import MultifaceGrowthConfig
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
from generated_symbols.data.worldgen.feature.SequenceConfig import SequenceConfig
from generated_symbols.data.worldgen.feature.SimpleBlockConfig import SimpleBlockConfig
from generated_symbols.data.worldgen.feature.SimpleRandomSelectorConfig import SimpleRandomSelectorConfig
from generated_symbols.data.worldgen.feature.SingleBlockPillarConfig import SingleBlockPillarConfig
from generated_symbols.data.worldgen.feature.SpeleothemClusterConfig import SpeleothemClusterConfig
from generated_symbols.data.worldgen.feature.SpeleothemConfig import SpeleothemConfig
from generated_symbols.data.worldgen.feature.SpikeConfig import SpikeConfig
from generated_symbols.data.worldgen.feature.SpringConfig import SpringConfig
from generated_symbols.data.worldgen.feature.TemplateConfig import TemplateConfig
from generated_symbols.data.worldgen.feature.UnderwaterMagmaConfig import UnderwaterMagmaConfig
from generated_symbols.data.worldgen.feature.VegetationPatchConfig import VegetationPatchConfig
from generated_symbols.data.worldgen.feature.WeightedRandomFeatureConfig import WeightedRandomFeatureConfig
from generated_symbols.data.worldgen.feature.tree.FallenTreeConfig import FallenTreeConfig
from generated_symbols.data.worldgen.feature.tree.TreeConfig import TreeConfig


@dataclass(kw_only=True)
class ConfiguredFeatureBamboo(ProbabilityConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    type: Literal['minecraft:bamboo']


@dataclass(kw_only=True)
class ConfiguredFeatureBlockBlob(BlockBlobConfig):
    type: Literal['minecraft:block_blob']


@dataclass(kw_only=True)
class ConfiguredFeatureBlockColumn(BlockColumnConfig):
    type: Literal['minecraft:block_column']


@dataclass(kw_only=True)
class ConfiguredFeatureBlockPile(BlockPileConfig):
    type: Literal['minecraft:block_pile']


@dataclass(kw_only=True)
class ConfiguredFeatureCoralClaw(CoralConfig):
    type: Literal['minecraft:coral_claw']


@dataclass(kw_only=True)
class ConfiguredFeatureCoralTree(CoralConfig):
    type: Literal['minecraft:coral_tree']


@dataclass(kw_only=True)
class ConfiguredFeatureDeltaFeature(DeltaConfig):
    type: Literal['minecraft:delta_feature']


@dataclass(kw_only=True)
class ConfiguredFeatureDisk(DiskConfig):
    type: Literal['minecraft:disk']


@dataclass(kw_only=True)
class ConfiguredFeatureEmeraldOre(EmeraldOreConfig):
    type: Literal['minecraft:emerald_ore']


@dataclass(kw_only=True)
class ConfiguredFeatureEndGateway(EndGatewayConfig):
    type: Literal['minecraft:end_gateway']


@dataclass(kw_only=True)
class ConfiguredFeatureEndPodium(EndPodiumConfig):
    type: Literal['minecraft:end_podium']


@dataclass(kw_only=True)
class ConfiguredFeatureEndSpike(EndSpikeConfig):
    type: Literal['minecraft:end_spike']


@dataclass(kw_only=True)
class ConfiguredFeatureFallenTree(FallenTreeConfig):
    type: Literal['minecraft:fallen_tree']


@dataclass(kw_only=True)
class ConfiguredFeatureFillLayer(FillLayerConfig):
    type: Literal['minecraft:fill_layer']


@dataclass(kw_only=True)
class ConfiguredFeatureFlower(RandomPatchConfig):
    type: Literal['minecraft:flower']


@dataclass(kw_only=True)
class ConfiguredFeatureFossil(FossilConfig):
    type: Literal['minecraft:fossil']


@dataclass(kw_only=True)
class ConfiguredFeatureGeode(GeodeConfig):
    type: Literal['minecraft:geode']


@dataclass(kw_only=True)
class ConfiguredFeatureGlowLichen(MultifaceGrowthConfig):
    type: Literal['minecraft:glow_lichen']


@dataclass(kw_only=True)
class ConfiguredFeatureHugeBrownMushroom(HugeMushroomConfig):
    type: Literal['minecraft:huge_brown_mushroom']


@dataclass(kw_only=True)
class ConfiguredFeatureHugeFungus(HugeFungusConfig):
    type: Literal['minecraft:huge_fungus']


@dataclass(kw_only=True)
class ConfiguredFeatureHugeRedMushroom(HugeMushroomConfig):
    type: Literal['minecraft:huge_red_mushroom']


@dataclass(kw_only=True)
class ConfiguredFeatureIcePatch(DiskConfig):
    type: Literal['minecraft:ice_patch']


@dataclass(kw_only=True)
class ConfiguredFeatureIceberg(IcebergConfig):
    type: Literal['minecraft:iceberg']


@dataclass(kw_only=True)
class ConfiguredFeatureLake(LakeConfig):
    type: Literal['minecraft:lake']


@dataclass(kw_only=True)
class ConfiguredFeatureLargeDripstone(LargeDripstoneConfig):
    type: Literal['minecraft:large_dripstone']


@dataclass(kw_only=True)
class ConfiguredFeatureMultifaceGrowth(MultifaceGrowthConfig):
    type: Literal['minecraft:multiface_growth']


@dataclass(kw_only=True)
class ConfiguredFeatureNetherrackReplaceBlobs(NetherrackReplaceBlobsConfig):
    type: Literal['minecraft:netherrack_replace_blobs']


@dataclass(kw_only=True)
class ConfiguredFeatureNoBonemealFlower(RandomPatchConfig):
    type: Literal['minecraft:no_bonemeal_flower']


@dataclass(kw_only=True)
class ConfiguredFeatureNoSurfaceOre(OreConfig):
    type: Literal['minecraft:no_surface_ore']


@dataclass(kw_only=True)
class ConfiguredFeatureOre(OreConfig):
    type: Literal['minecraft:ore']


@dataclass(kw_only=True)
class ConfiguredFeatureOverlay(OverlayConfig):
    type: Literal['minecraft:overlay']


@dataclass(kw_only=True)
class ConfiguredFeatureProjectedRandomPatchySquare(ProjectedSquareConfig):
    type: Literal['minecraft:projected_random_patchy_square']


@dataclass(kw_only=True)
class ConfiguredFeatureRandomBooleanSelector(RandomBooleanSelector):
    type: Literal['minecraft:random_boolean_selector']


@dataclass(kw_only=True)
class ConfiguredFeatureRandomNeighborSpread(RandomNeighborSpreadConfig):
    type: Literal['minecraft:random_neighbor_spread']


@dataclass(kw_only=True)
class ConfiguredFeatureRandomPatch(RandomPatchConfig):
    type: Literal['minecraft:random_patch']


@dataclass(kw_only=True)
class ConfiguredFeatureRandomSelector(RandomSelector):
    type: Literal['minecraft:random_selector']


@dataclass(kw_only=True)
class ConfiguredFeatureReplaceSingleBlock(ReplaceSingleBlockConfig):
    type: Literal['minecraft:replace_single_block']


@dataclass(kw_only=True)
class ConfiguredFeatureRootSystem(RootSystemConfig):
    type: Literal['minecraft:root_system']


@dataclass(kw_only=True)
class ConfiguredFeatureScatteredOre(OreConfig):
    type: Literal['minecraft:scattered_ore']


@dataclass(kw_only=True)
class ConfiguredFeatureSculkPatch(SculkPatchConfig):
    type: Literal['minecraft:sculk_patch']


@dataclass(kw_only=True)
class ConfiguredFeatureSequence(SequenceConfig):
    type: Literal['minecraft:sequence']


@dataclass(kw_only=True)
class ConfiguredFeatureSimpleBlock(SimpleBlockConfig):
    type: Literal['minecraft:simple_block']


@dataclass(kw_only=True)
class ConfiguredFeatureSimpleRandomSelector(SimpleRandomSelectorConfig):
    type: Literal['minecraft:simple_random_selector']


@dataclass(kw_only=True)
class ConfiguredFeatureSingleBlockPillar(SingleBlockPillarConfig):
    type: Literal['minecraft:single_block_pillar']


@dataclass(kw_only=True)
class ConfiguredFeatureSpeleothem(SpeleothemConfig):
    type: Literal['minecraft:speleothem']


@dataclass(kw_only=True)
class ConfiguredFeatureSpeleothemCluster(SpeleothemClusterConfig):
    type: Literal['minecraft:speleothem_cluster']


@dataclass(kw_only=True)
class ConfiguredFeatureSpike(SpikeConfig):
    type: Literal['minecraft:spike']


@dataclass(kw_only=True)
class ConfiguredFeatureSpringFeature(SpringConfig):
    type: Literal['minecraft:spring_feature']


@dataclass(kw_only=True)
class ConfiguredFeatureSteppedColumnCluster(ColumnsConfig):
    type: Literal['minecraft:stepped_column_cluster']


@dataclass(kw_only=True)
class ConfiguredFeatureTemplate(TemplateConfig):
    type: Literal['minecraft:template']


@dataclass(kw_only=True)
class ConfiguredFeatureTree(TreeConfig):
    type: Literal['minecraft:tree']


@dataclass(kw_only=True)
class ConfiguredFeatureUnderwaterMagma(UnderwaterMagmaConfig):
    type: Literal['minecraft:underwater_magma']


@dataclass(kw_only=True)
class ConfiguredFeatureVegetationPatch(VegetationPatchConfig):
    type: Literal['minecraft:vegetation_patch']


@dataclass(kw_only=True)
class ConfiguredFeatureWaterloggedVegetationPatch(VegetationPatchConfig):
    type: Literal['minecraft:waterlogged_vegetation_patch']


@dataclass(kw_only=True)
class ConfiguredFeatureWeightedRandomSelector(WeightedRandomFeatureConfig):
    type: Literal['minecraft:weighted_random_selector']


type ConfiguredFeature = ConfiguredFeatureBamboo | ConfiguredFeatureBlockBlob | ConfiguredFeatureBlockColumn | ConfiguredFeatureBlockPile | ConfiguredFeatureCoralClaw | ConfiguredFeatureCoralTree | ConfiguredFeatureDeltaFeature | ConfiguredFeatureDisk | ConfiguredFeatureEmeraldOre | ConfiguredFeatureEndGateway | ConfiguredFeatureEndPodium | ConfiguredFeatureEndSpike | ConfiguredFeatureFallenTree | ConfiguredFeatureFillLayer | ConfiguredFeatureFlower | ConfiguredFeatureFossil | ConfiguredFeatureGeode | ConfiguredFeatureGlowLichen | ConfiguredFeatureHugeBrownMushroom | ConfiguredFeatureHugeFungus | ConfiguredFeatureHugeRedMushroom | ConfiguredFeatureIcePatch | ConfiguredFeatureIceberg | ConfiguredFeatureLake | ConfiguredFeatureLargeDripstone | ConfiguredFeatureMultifaceGrowth | ConfiguredFeatureNetherrackReplaceBlobs | ConfiguredFeatureNoBonemealFlower | ConfiguredFeatureNoSurfaceOre | ConfiguredFeatureOre | ConfiguredFeatureOverlay | ConfiguredFeatureProjectedRandomPatchySquare | ConfiguredFeatureRandomBooleanSelector | ConfiguredFeatureRandomNeighborSpread | ConfiguredFeatureRandomPatch | ConfiguredFeatureRandomSelector | ConfiguredFeatureReplaceSingleBlock | ConfiguredFeatureRootSystem | ConfiguredFeatureScatteredOre | ConfiguredFeatureSculkPatch | ConfiguredFeatureSequence | ConfiguredFeatureSimpleBlock | ConfiguredFeatureSimpleRandomSelector | ConfiguredFeatureSingleBlockPillar | ConfiguredFeatureSpeleothem | ConfiguredFeatureSpeleothemCluster | ConfiguredFeatureSpike | ConfiguredFeatureSpringFeature | ConfiguredFeatureSteppedColumnCluster | ConfiguredFeatureTemplate | ConfiguredFeatureTree | ConfiguredFeatureUnderwaterMagma | ConfiguredFeatureVegetationPatch | ConfiguredFeatureWaterloggedVegetationPatch | ConfiguredFeatureWeightedRandomSelector


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::ConfiguredFeature": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/feature"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/feature_type"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "config",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:feature_config"
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:feature_config"
                }
            }
        ]
    }
}

