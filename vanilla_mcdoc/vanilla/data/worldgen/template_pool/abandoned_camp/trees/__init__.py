"""Vanilla's data/worldgen/template_pool/abandoned_camp/trees/ files"""
from vanilla_mcdoc.data.worldgen.template_pool.Element import ElementFeaturePoolElement
from vanilla_mcdoc.data.worldgen.template_pool.Projection import Projection
from vanilla_mcdoc.data.worldgen.template_pool.TemplatePool import TemplatePool
from vanilla_mcdoc.data.worldgen.template_pool.WeightedElement import WeightedElement

ACACIA = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:acacia_checked',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

BAMBOO = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:bamboo_in_structure',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

BIRCH = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:birch_checked',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

BIRCH_BEES = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:birch_bees_002',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

CHERRY = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:cherry_checked',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

CHERRY_BEES = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:cherry_bees_005',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

FANCY_OAK = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:fancy_oak_checked',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

FANCY_OAK_BEES = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:fancy_oak_bees_002',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

JUNGLE = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:jungle_tree',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

MEGA_JUNGLE = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:mega_jungle_tree_checked',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

MEGA_PINE = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:mega_pine_checked',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

OAK = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:oak_checked',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

ORANGE_POPLAR = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:orange_poplar',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

PALE_OAK = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:pale_oak_checked',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

PINE = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:pine_checked',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

RED_POPLAR = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:red_poplar',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

SPRUCE = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:spruce_checked',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

SPRUCE_ON_SNOW = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:spruce_on_snow',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

SUPER_BIRCH_BEES = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:super_birch_bees_0002',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

THICK_SPRUCE = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:mega_spruce_checked',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)

YELLOW_POPLAR = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementFeaturePoolElement(
                projection=Projection.RIGID,
                feature='minecraft:yellow_poplar',
                element_type='minecraft:feature_pool_element',
            ),
        ),
    ],
)
