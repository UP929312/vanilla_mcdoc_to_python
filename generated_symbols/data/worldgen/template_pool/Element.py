"""
Generated from symbols.json for ::java::data::worldgen::template_pool::Element
Local link to file: generated_symbols/data/worldgen/template_pool/Element.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from generated_symbols.data.worldgen.template_pool.FeatureElement import FeatureElement
from generated_symbols.data.worldgen.template_pool.ListElement import ListElement
from generated_symbols.data.worldgen.template_pool.SingleElement import SingleElement


class ElementFeaturePoolElement(FeatureElement):
    element_type: Literal['minecraft:feature_pool_element', 'feature_pool_element'] = 'minecraft:feature_pool_element'


class ElementLegacySinglePoolElement(SingleElement):
    element_type: Literal['minecraft:legacy_single_pool_element', 'legacy_single_pool_element'] = 'minecraft:legacy_single_pool_element'


class ElementListPoolElement(ListElement):
    element_type: Literal['minecraft:list_pool_element', 'list_pool_element'] = 'minecraft:list_pool_element'


class ElementSinglePoolElement(SingleElement):
    element_type: Literal['minecraft:single_pool_element', 'single_pool_element'] = 'minecraft:single_pool_element'


type Element = Annotated[
    ElementFeaturePoolElement | ElementLegacySinglePoolElement | ElementListPoolElement | ElementSinglePoolElement,
    Field(discriminator='element_type'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::template_pool::Element": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "element_type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/structure_pool_element"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "element_type"
                            ]
                        }
                    ],
                    "registry": "minecraft:template_pool_element"
                }
            }
        ]
    }
}

