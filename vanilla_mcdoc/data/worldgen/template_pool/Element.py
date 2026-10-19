"""
Generated from symbols.json for ::java::data::worldgen::template_pool::Element
Local link to file: vanilla_mcdoc/data/worldgen/template_pool/Element.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.worldgen.template_pool.FeatureElement import FeatureElement
from vanilla_mcdoc.data.worldgen.template_pool.ListElement import ListElement
from vanilla_mcdoc.data.worldgen.template_pool.SingleElement import SingleElement


class ElementFeaturePoolElement(FeatureElement):
    element_type: Literal['minecraft:feature_pool_element', 'feature_pool_element'] = 'minecraft:feature_pool_element'


class ElementLegacySinglePoolElement(SingleElement):
    element_type: Literal['minecraft:legacy_single_pool_element', 'legacy_single_pool_element'] = 'minecraft:legacy_single_pool_element'


class ElementListPoolElement(ListElement):
    element_type: Literal['minecraft:list_pool_element', 'list_pool_element'] = 'minecraft:list_pool_element'


class ElementSinglePoolElement(SingleElement):
    element_type: Literal['minecraft:single_pool_element', 'single_pool_element'] = 'minecraft:single_pool_element'


class ElementEmptyPoolElement(GeneratedModel):
    element_type: Literal['minecraft:empty_pool_element', 'empty_pool_element'] = 'minecraft:empty_pool_element'


type Element = Annotated[
    Annotated[ElementFeaturePoolElement, Tag('minecraft:feature_pool_element')]
    | Annotated[ElementLegacySinglePoolElement, Tag('minecraft:legacy_single_pool_element')]
    | Annotated[ElementListPoolElement, Tag('minecraft:list_pool_element')]
    | Annotated[ElementSinglePoolElement, Tag('minecraft:single_pool_element')]
    | Annotated[ElementEmptyPoolElement, Tag('minecraft:empty_pool_element')],
    Discriminator(tag_of('element_type')),
]
