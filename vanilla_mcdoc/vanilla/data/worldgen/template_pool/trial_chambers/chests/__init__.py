"""Vanilla's data/worldgen/template_pool/trial_chambers/chests/ files"""
from vanilla_mcdoc.data.worldgen.processor_list.ProcessorList import ProcessorListStruct
from vanilla_mcdoc.data.worldgen.template_pool.Element import ElementSinglePoolElement
from vanilla_mcdoc.data.worldgen.template_pool.Projection import Projection
from vanilla_mcdoc.data.worldgen.template_pool.TemplatePool import TemplatePool
from vanilla_mcdoc.data.worldgen.template_pool.WeightedElement import WeightedElement

SUPPLY = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:trial_chambers/chests/connectors/supply',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)
