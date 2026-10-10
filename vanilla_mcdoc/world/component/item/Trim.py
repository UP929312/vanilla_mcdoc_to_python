"""
Generated from symbols.json for ::java::world::component::item::Trim
Local link to file: vanilla_mcdoc/world/component/item/Trim.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.trim.TrimMaterial import TrimMaterial
    from vanilla_mcdoc.data.trim.TrimPattern import TrimPattern


class Trim(GeneratedModel):
    material: Annotated[str, IdSpec(registry='trim_material')] | TrimMaterial  # The trim material of this item..
    pattern: Annotated[str, IdSpec(registry='trim_pattern')] | TrimPattern  # The trim pattern of this item.
