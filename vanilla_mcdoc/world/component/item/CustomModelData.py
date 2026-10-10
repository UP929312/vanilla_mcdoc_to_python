"""
Generated from symbols.json for ::java::world::component::item::CustomModelData
Local link to file: vanilla_mcdoc/world/component/item/CustomModelData.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.RGB import RGB


class CustomModelData(GeneratedModel):
    floats: list[float] | None = None
    flags: list[bool] | None = None
    strings: list[str] | None = None
    colors: list[RGB] | None = None
