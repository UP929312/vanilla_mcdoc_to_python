"""
Generated from symbols.json for ::java::data::loot::LootTable
Local link to file: vanilla_mcdoc/data/loot/LootTable.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.item_modifier.ItemModifier import ItemModifier
    from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
    from vanilla_mcdoc.data.loot.LootPool import LootPool


class LootTable(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'loot_table'

    type: LootContextParamSets | None = None
    pools: list[LootPool] | None = None
    modifier: ItemModifier | None = None
    random_sequence: Annotated[str, IdSpec(registry='random_sequence', definition=True)] | None = None
