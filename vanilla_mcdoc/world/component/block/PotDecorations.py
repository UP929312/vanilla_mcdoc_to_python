"""
Generated from symbols.json for ::java::world::component::block::PotDecorations
Local link to file: vanilla_mcdoc/world/component/block/PotDecorations.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class PotDecorations(GeneratedModel):
    back: ItemStackTemplate | None = None
    left: ItemStackTemplate | None = None
    right: ItemStackTemplate | None = None
    front: ItemStackTemplate | None = None
