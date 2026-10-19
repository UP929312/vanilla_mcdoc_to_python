"""Vanilla's data/worldgen/template_pool/bastion/mobs/ files"""
from vanilla_mcdoc.data.worldgen.processor_list.ProcessorList import ProcessorListStruct
from vanilla_mcdoc.data.worldgen.template_pool.Element import ElementSinglePoolElement
from vanilla_mcdoc.data.worldgen.template_pool.Projection import Projection
from vanilla_mcdoc.data.worldgen.template_pool.TemplatePool import TemplatePool
from vanilla_mcdoc.data.worldgen.template_pool.WeightedElement import WeightedElement

HOGLIN = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=2,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/mobs/hoglin',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/mobs/empty',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

PIGLIN = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/mobs/melee_piglin',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=4,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/mobs/sword_piglin',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=4,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/mobs/crossbow_piglin',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/mobs/empty',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

PIGLIN_MELEE = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/mobs/melee_piglin_always',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=5,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/mobs/melee_piglin',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:bastion/mobs/sword_piglin',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)
