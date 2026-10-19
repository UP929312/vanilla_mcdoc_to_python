"""Vanilla's data/worldgen/template_pool/bastion/treasure/corners/ files"""
from vanilla_mcdoc.data.worldgen.template_pool.Element import ElementSinglePoolElement
from vanilla_mcdoc.data.worldgen.template_pool.Projection import Projection
from vanilla_mcdoc.data.worldgen.template_pool.TemplatePool import TemplatePool
from vanilla_mcdoc.data.worldgen.template_pool.WeightedElement import WeightedElement

BOTTOM = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/corners/bottom/corner_0',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/corners/bottom/corner_1',
                processors='minecraft:treasure_rooms',
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
                location='minecraft:bastion/treasure/corners/edges/bottom',
                processors='minecraft:high_wall',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/corners/edges/middle',
                processors='minecraft:high_wall',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/corners/edges/top',
                processors='minecraft:high_wall',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

MIDDLE = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/corners/middle/corner_0',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/corners/middle/corner_1',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

TOP = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/corners/top/corner_0',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/corners/top/corner_1',
                processors='minecraft:treasure_rooms',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)
