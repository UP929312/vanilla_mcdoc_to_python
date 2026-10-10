"""
Generated from symbols.json for ::java::data::loot::function::SetLootTable
Local link to file: vanilla_mcdoc/data/loot/function/SetLootTable.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import IdSpec


class SetLootTable(Conditions):
    loot_table_id: Annotated[str, IdSpec(registry='loot_table')]  # The loot table to set to the container block item.
    seed: int | None = None  # The container seed to use. Defaults to a random seed.
