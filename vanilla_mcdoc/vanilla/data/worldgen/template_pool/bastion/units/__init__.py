"""Vanilla's data/worldgen/template_pool/bastion/units/ files"""
from vanilla_mcdoc.data.worldgen.template_pool.Element import ElementSinglePoolElement
from vanilla_mcdoc.data.worldgen.template_pool.Projection import Projection
from vanilla_mcdoc.data.worldgen.template_pool.TemplatePool import TemplatePool
from vanilla_mcdoc.data.worldgen.template_pool.WeightedElement import WeightedElement

CENTER_PIECES = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/units/center_pieces/center_0',
                processors='minecraft:housing',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/units/center_pieces/center_1',
                processors='minecraft:housing',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/units/center_pieces/center_2',
                processors='minecraft:housing',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

EDGES = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/units/edges/edge_0',
                processors='minecraft:housing',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

EDGE_WALL_UNITS = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/units/wall_units/edge_0_large',
                processors='minecraft:housing',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

LARGE_RAMPARTS = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/units/ramparts/ramparts_0',
                processors='minecraft:housing',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

PATHWAYS = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/units/pathways/pathway_0',
                processors='minecraft:housing',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/units/pathways/pathway_wall_0',
                processors='minecraft:housing',
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
                location='minecraft:bastion/units/ramparts/ramparts_0',
                processors='minecraft:housing',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/units/ramparts/ramparts_1',
                processors='minecraft:housing',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/units/ramparts/ramparts_2',
                processors='minecraft:housing',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

RAMPART_PLATES = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/units/rampart_plates/plate_0',
                processors='minecraft:housing',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

WALL_UNITS = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/units/wall_units/unit_0',
                processors='minecraft:housing',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)
