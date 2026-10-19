"""Vanilla's data/worldgen/template_pool/bastion/treasure/ files"""
from vanilla_mcdoc.data.worldgen.template_pool.Element import ElementSinglePoolElement
from vanilla_mcdoc.data.worldgen.template_pool.Projection import Projection
from vanilla_mcdoc.data.worldgen.template_pool.TemplatePool import TemplatePool
from vanilla_mcdoc.data.worldgen.template_pool.WeightedElement import WeightedElement

BASES = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/bases/lava_basin',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

BRAINS = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/brains/center_brain',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

CONNECTORS = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/connectors/center_to_wall_middle',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/connectors/center_to_wall_top',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/connectors/center_to_wall_top_entrance',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

ENTRANCES = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/entrances/entrance_0',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

RAMPARTS = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/ramparts/mid_wall_main',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/ramparts/mid_wall_side',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/ramparts/bottom_wall_0',
                processors='minecraft:bottom_rampart',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/ramparts/top_wall',
                processors='minecraft:high_rampart',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/ramparts/lava_basin_side',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/ramparts/lava_basin_main',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

ROOFS = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/roofs/wall_roof',
                processors='minecraft:roof',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/roofs/corner_roof',
                processors='minecraft:roof',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/roofs/center_roof',
                processors='minecraft:roof',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

STAIRS = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/stairs/lower_stairs',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

WALLS = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/walls/lava_wall',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/walls/entrance_wall',
                processors='minecraft:high_wall',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)
