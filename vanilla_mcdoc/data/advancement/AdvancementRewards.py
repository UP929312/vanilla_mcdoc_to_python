"""
Generated from symbols.json for ::java::data::advancement::AdvancementRewards
Local link to file: vanilla_mcdoc/data/advancement/AdvancementRewards.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.LootTableListRef import LootTableListRef


class AdvancementRewards(GeneratedModel):
    experience: int | None = None  # XP to add.
    loot: LootTableListRef | None = None  # Loot tables to give.
    recipes: list[Annotated[str, IdSpec(registry='recipe')]] | None = None  # Recipes to unlock.
    function: Annotated[str, IdSpec(registry='function')] | None = None  # Function to run as and at the player. Function tags are not allowed.
