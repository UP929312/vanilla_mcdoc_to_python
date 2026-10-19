"""Vanilla's data/worldgen/template_pool/bastion/hoglin_stable/small_stables/ files"""
from vanilla_mcdoc.data.worldgen.template_pool.Element import ElementSinglePoolElement
from vanilla_mcdoc.data.worldgen.template_pool.Projection import Projection
from vanilla_mcdoc.data.worldgen.template_pool.TemplatePool import TemplatePool
from vanilla_mcdoc.data.worldgen.template_pool.WeightedElement import WeightedElement

INNER = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/hoglin_stable/small_stables/inner_0',
                processors='minecraft:stable_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/hoglin_stable/small_stables/inner_1',
                processors='minecraft:stable_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/hoglin_stable/small_stables/inner_2',
                processors='minecraft:stable_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/hoglin_stable/small_stables/inner_3',
                processors='minecraft:stable_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

OUTER = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/hoglin_stable/small_stables/outer_0',
                processors='minecraft:stable_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/hoglin_stable/small_stables/outer_1',
                processors='minecraft:stable_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/hoglin_stable/small_stables/outer_2',
                processors='minecraft:stable_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/hoglin_stable/small_stables/outer_3',
                processors='minecraft:stable_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)
