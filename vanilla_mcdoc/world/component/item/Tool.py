"""
Generated from symbols.json for ::java::world::component::item::Tool
Local link to file: vanilla_mcdoc/world/component/item/Tool.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.ToolRule import ToolRule


class Tool(GeneratedModel):
    rules: list[ToolRule]  # Blocks that this tool has a special behavior with.
    default_mining_speed: float | None = None  # Used if no rules override it. Defaults to 1.0.
    damage_per_block: int | None = None  # Amount of durability to remove each time a block is broken with this tool. Must be a non-negative integer.
    can_destroy_blocks_in_creative: bool | None = None  # If `false`, players cannot break blocks while holding this tool in creative mode. Defaults to `true`.
