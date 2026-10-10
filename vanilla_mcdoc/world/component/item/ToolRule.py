"""
Generated from symbols.json for ::java::world::component::item::ToolRule
Local link to file: vanilla_mcdoc/world/component/item/ToolRule.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class ToolRule(GeneratedModel):
    blocks: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]
    speed: float | None = None  # Overrides the default mining speed.
    correct_for_drops: bool | None = None  # Overrides whether or not this tool is considered correct to mine at its most efficient speed, and to drop items if the block's loot table requires it.
