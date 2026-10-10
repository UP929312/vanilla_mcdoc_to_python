"""
Generated from symbols.json for ::java::world::item::ItemStackTemplate
Local link to file: vanilla_mcdoc/world/item/ItemStackTemplate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


type ItemStackTemplate = ItemStack | Annotated[str, IdSpec(registry='item', exclude=('air',))]
