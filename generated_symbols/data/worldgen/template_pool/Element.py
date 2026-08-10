"""
Generated from symbols.json for ::java::data::worldgen::template_pool::Element
Local link to file: generated_symbols/data/worldgen/template_pool/Element.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.worldgen.template_pool.ElementBase import ElementBase
from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef
    from generated_symbols.data.worldgen.processor_list.ProcessorListRef import ProcessorListRef
    from generated_symbols.data.worldgen.structure.LiquidSettings import LiquidSettings


@dataclass(kw_only=True)
class ElementFeaturePoolElement(ElementBase):
    element_type: Literal['minecraft:feature_pool_element']
    feature: PlacedFeatureRef


@dataclass(kw_only=True)
class ElementLegacySinglePoolElement(ElementBase):
    element_type: Literal['minecraft:legacy_single_pool_element']
    location: Annotated[str, IdSpec(registry='structure')]
    processors: ProcessorListRef
    override_liquid_settings: LiquidSettings | None = None


@dataclass(kw_only=True)
class ElementListPoolElement(ElementBase):
    element_type: Literal['minecraft:list_pool_element']
    elements: list[Element]


@dataclass(kw_only=True)
class ElementSinglePoolElement(ElementBase):
    element_type: Literal['minecraft:single_pool_element']
    location: Annotated[str, IdSpec(registry='structure')]
    processors: ProcessorListRef
    override_liquid_settings: LiquidSettings | None = None


type Element = ElementFeaturePoolElement | ElementLegacySinglePoolElement | ElementListPoolElement | ElementSinglePoolElement


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

