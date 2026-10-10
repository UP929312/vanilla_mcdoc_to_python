"""
Generated from symbols.json for ::java::world::component::item::DebugStickState
Local link to file: vanilla_mcdoc/world/component/item/DebugStickState.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


type DebugStickState = dict[Annotated[str, IdSpec(registry='block')] | KnownBlockId, str]
