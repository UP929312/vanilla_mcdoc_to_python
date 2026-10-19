"""Vanilla's data/worldgen/template_pool/bastion/ files"""
from vanilla_mcdoc.data.worldgen.template_pool.Element import ElementSinglePoolElement
from vanilla_mcdoc.data.worldgen.template_pool.Projection import Projection
from vanilla_mcdoc.data.worldgen.template_pool.TemplatePool import TemplatePool
from vanilla_mcdoc.data.worldgen.template_pool.WeightedElement import WeightedElement

STARTS = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/units/air_base',
                processors='minecraft:bastion_generic_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/hoglin_stable/air_base',
                processors='minecraft:bastion_generic_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/treasure/big_air_full',
                processors='minecraft:bastion_generic_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/bridge/starting_pieces/entrance_base',
                processors='minecraft:bastion_generic_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)
