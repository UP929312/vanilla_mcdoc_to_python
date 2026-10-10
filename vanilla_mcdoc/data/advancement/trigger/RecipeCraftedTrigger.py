"""
Generated from symbols.json for ::java::data::advancement::trigger::RecipeCraftedTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/RecipeCraftedTrigger.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.ParitalRequired import ParitalRequired
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.recipe.RecipeListRef import RecipeListRef


class RecipeCraftedTriggerTypeArg(PlayerConditions):
    recipes: RecipeListRef
    ingredients: Annotated[list[ItemPredicate], Field(min_length=1, max_length=9)] | None = None


RecipeCraftedTrigger = ParitalRequired[RecipeCraftedTriggerTypeArg]
