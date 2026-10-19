"""Vanilla's data/worldgen/template_pool/bastion/bridge/ files"""
from vanilla_mcdoc.data.worldgen.template_pool.Element import ElementSinglePoolElement
from vanilla_mcdoc.data.worldgen.template_pool.Projection import Projection
from vanilla_mcdoc.data.worldgen.template_pool.TemplatePool import TemplatePool
from vanilla_mcdoc.data.worldgen.template_pool.WeightedElement import WeightedElement

BRIDGE_PIECES = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/bridge/bridge_pieces/bridge',
                processors='minecraft:bridge',
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
                location='minecraft:bastion/bridge/connectors/back_bridge_top',
                processors='minecraft:bastion_generic_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/bridge/connectors/back_bridge_bottom',
                processors='minecraft:bastion_generic_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

LEGS = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/bridge/legs/leg_0',
                processors='minecraft:bastion_generic_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/bridge/legs/leg_1',
                processors='minecraft:bastion_generic_degradation',
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
                location='minecraft:bastion/bridge/ramparts/rampart_0',
                processors='minecraft:rampart_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/bridge/ramparts/rampart_1',
                processors='minecraft:rampart_degradation',
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
                location='minecraft:bastion/bridge/rampart_plates/plate_0',
                processors='minecraft:rampart_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

STARTING_PIECES = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/bridge/starting_pieces/entrance',
                processors='minecraft:entrance_replacement',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/bridge/starting_pieces/entrance_face',
                processors='minecraft:bastion_generic_degradation',
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
                location='minecraft:bastion/bridge/walls/wall_base_0',
                processors='minecraft:rampart_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/bridge/walls/wall_base_1',
                processors='minecraft:rampart_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)
