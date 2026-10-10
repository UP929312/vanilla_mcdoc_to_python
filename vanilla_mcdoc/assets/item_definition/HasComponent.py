"""
Generated from symbols.json for ::java::assets::item_definition::HasComponent
Local link to file: vanilla_mcdoc/assets/item_definition/HasComponent.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class HasComponent(GeneratedModel):
    component: Annotated[str, IdSpec(registry='data_component_type')]
    ignore_default: bool | None = None  # Whether the default components should be handled as "no component". Defaults to false.
