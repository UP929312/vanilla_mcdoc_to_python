"""
Generated from symbols.json for ::java::world::component::item::AttributeDisplay
Local link to file: vanilla_mcdoc/world/component/item/AttributeDisplay.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.world.component.item.AttributeDisplayTextOverride import AttributeDisplayTextOverride


class AttributeDisplayDefault(GeneratedModel):
    type: Literal['minecraft:default', 'default'] = 'minecraft:default'


class AttributeDisplayHidden(GeneratedModel):
    type: Literal['minecraft:hidden', 'hidden'] = 'minecraft:hidden'


class AttributeDisplayOverride(AttributeDisplayTextOverride):
    type: Literal['minecraft:override', 'override'] = 'minecraft:override'


type AttributeDisplay = Annotated[
    AttributeDisplayDefault | AttributeDisplayHidden | AttributeDisplayOverride,
    Field(discriminator='type'),
]
