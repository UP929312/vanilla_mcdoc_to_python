"""
Generated from symbols.json for ::java::util::registry_ref::ItemListRef
Local link to file: vanilla_mcdoc/util/registry_ref/ItemListRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownItemId import KnownItemId


type ItemListRef = Annotated[str, IdSpec(registry='item', tags='allowed')] | KnownItemId | list[Annotated[str, IdSpec(registry='item')] | KnownItemId]
