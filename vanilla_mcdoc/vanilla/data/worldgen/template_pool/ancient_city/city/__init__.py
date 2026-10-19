"""Vanilla's data/worldgen/template_pool/ancient_city/city/ files"""
from vanilla_mcdoc.data.worldgen.template_pool.Element import ElementSinglePoolElement
from vanilla_mcdoc.data.worldgen.template_pool.Projection import Projection
from vanilla_mcdoc.data.worldgen.template_pool.TemplatePool import TemplatePool
from vanilla_mcdoc.data.worldgen.template_pool.WeightedElement import WeightedElement

ENTRANCE = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:ancient_city/city/entrance/entrance_connector',
                processors='minecraft:ancient_city_generic_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:ancient_city/city/entrance/entrance_path_1',
                processors='minecraft:ancient_city_generic_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:ancient_city/city/entrance/entrance_path_2',
                processors='minecraft:ancient_city_generic_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:ancient_city/city/entrance/entrance_path_3',
                processors='minecraft:ancient_city_generic_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:ancient_city/city/entrance/entrance_path_4',
                processors='minecraft:ancient_city_generic_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:ancient_city/city/entrance/entrance_path_5',
                processors='minecraft:ancient_city_generic_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)
