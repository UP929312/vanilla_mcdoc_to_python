"""
Generated from symbols.json for ::java::data::loot::function::CopyComponents
Local link to file: vanilla_mcdoc/data/loot/function/CopyComponents.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.BlockEntityTarget import BlockEntityTarget
    from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
    from vanilla_mcdoc.data.loot.ItemStackTarget import ItemStackTarget


class CopyComponents(Conditions):
    source: BlockEntityTarget | EntityTarget | ItemStackTarget
    include: list[Annotated[str, IdSpec(registry='data_component_type')]] | None = None  # If omitted, all components present are included
    exclude: list[Annotated[str, IdSpec(registry='data_component_type')]] | None = None  # Defaults to none.
