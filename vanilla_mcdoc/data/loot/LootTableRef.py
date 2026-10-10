"""
Generated from symbols.json for ::java::data::loot::LootTableRef
Local link to file: vanilla_mcdoc/data/loot/LootTableRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.LootTable import LootTable


type LootTableRef = LootTable | Annotated[str, IdSpec(registry='loot_table')]
