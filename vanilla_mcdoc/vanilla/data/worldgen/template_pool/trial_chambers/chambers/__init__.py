"""Vanilla's data/worldgen/template_pool/trial_chambers/chambers/ files"""
from vanilla_mcdoc.data.worldgen.template_pool.Element import ElementSinglePoolElement
from vanilla_mcdoc.data.worldgen.template_pool.Projection import Projection
from vanilla_mcdoc.data.worldgen.template_pool.TemplatePool import TemplatePool
from vanilla_mcdoc.data.worldgen.template_pool.WeightedElement import WeightedElement

END = TemplatePool(
    fallback='minecraft:trial_chambers/hallway/fallback',
    elements=[
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:trial_chambers/chamber/chamber_1',
                processors='minecraft:trial_chambers_copper_bulb_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:trial_chambers/chamber/assembly',
                processors='minecraft:trial_chambers_copper_bulb_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:trial_chambers/chamber/eruption',
                processors='minecraft:trial_chambers_copper_bulb_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
        WeightedElement(
            weight=1,
            element=ElementSinglePoolElement(
                projection=Projection.RIGID,
                location='minecraft:trial_chambers/chamber/slanted',
                processors='minecraft:trial_chambers_copper_bulb_degradation',
                element_type='minecraft:single_pool_element',
            ),
        ),
    ],
)
