"""
Generated from symbols.json for ::java::assets::item_definition::ShulkerBox
Local link to file: vanilla_mcdoc/assets/item_definition/ShulkerBox.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class ShulkerBox(GeneratedModel):
    texture: Annotated[str, IdSpec(registry='texture', path='entity/shulker/')]
    openness: Annotated[float, Field(ge=0, le=1)] | None = None
