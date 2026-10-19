"""Vanilla's data/worldgen/template_pool/trial_chambers/spawner/slow_ranged/ files"""
from vanilla_mcdoc.data.worldgen.processor_list.ProcessorList import ProcessorListStruct
from vanilla_mcdoc.data.worldgen.template_pool.Element import ElementSinglePoolElement
from vanilla_mcdoc.data.worldgen.template_pool.Projection import Projection
from vanilla_mcdoc.data.worldgen.template_pool.TemplatePool import TemplatePool
from vanilla_mcdoc.data.worldgen.template_pool.WeightedElement import WeightedElement

POISON_SKELETON = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:trial_chambers/spawner/slow_ranged/poison_skeleton',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

SKELETON = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:trial_chambers/spawner/slow_ranged/skeleton',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)

STRAY = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:trial_chambers/spawner/slow_ranged/stray',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)
