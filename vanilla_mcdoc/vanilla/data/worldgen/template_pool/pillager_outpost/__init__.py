"""Vanilla's data/worldgen/template_pool/pillager_outpost/ files"""
from vanilla_mcdoc.data.worldgen.processor_list.ProcessorList import ProcessorListStruct
from vanilla_mcdoc.data.worldgen.template_pool.Element import ElementEmptyPoolElement, ElementLegacySinglePoolElement, ElementListPoolElement
from vanilla_mcdoc.data.worldgen.template_pool.Projection import Projection
from vanilla_mcdoc.data.worldgen.template_pool.TemplatePool import TemplatePool
from vanilla_mcdoc.data.worldgen.template_pool.WeightedElement import WeightedElement

BASE_PLATES = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementLegacySinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:pillager_outpost/base_plate',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:legacy_single_pool_element',
            ),
        ),
    ],
)

FEATURES = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementLegacySinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:pillager_outpost/feature_cage1',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:legacy_single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementLegacySinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:pillager_outpost/feature_cage2',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:legacy_single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementLegacySinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:pillager_outpost/feature_cage_with_allays',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:legacy_single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementLegacySinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:pillager_outpost/feature_logs',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:legacy_single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementLegacySinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:pillager_outpost/feature_tent1',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:legacy_single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementLegacySinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:pillager_outpost/feature_tent2',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:legacy_single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementLegacySinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:pillager_outpost/feature_targets',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:legacy_single_pool_element',
            ),
        ),
        WeightedElement(weight=6, element=ElementEmptyPoolElement(element_type='minecraft:empty_pool_element')),
    ],
)

FEATURE_PLATES = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementLegacySinglePoolElement(
                projection=Projection.TERRAINMATCHING,
                location='minecraft:pillager_outpost/feature_plate',
                processors=ProcessorListStruct(processors=[]),
                element_type='minecraft:legacy_single_pool_element',
            ),
        ),
    ],
)

TOWERS = TemplatePool(
    fallback='minecraft:empty',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementListPoolElement(
                projection=Projection.RIGID,
                elements=[
                    ElementLegacySinglePoolElement(
                        projection=Projection.RIGID,
                        location='minecraft:pillager_outpost/watchtower',
                        processors=ProcessorListStruct(processors=[]),
                        element_type='minecraft:legacy_single_pool_element',
                    ),
                    ElementLegacySinglePoolElement(
                        projection=Projection.RIGID,
                        location='minecraft:pillager_outpost/watchtower_overgrown',
                        processors='minecraft:outpost_rot',
                        element_type='minecraft:legacy_single_pool_element',
                    ),
                ],
                element_type='minecraft:list_pool_element',
            ),
        ),
    ],
)
