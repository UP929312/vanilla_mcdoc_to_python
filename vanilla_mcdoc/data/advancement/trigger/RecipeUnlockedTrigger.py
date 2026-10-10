"""
Generated from symbols.json for ::java::data::advancement::trigger::RecipeUnlockedTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/RecipeUnlockedTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.ParitalRequired import ParitalRequired
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.recipe.RecipeListRef import RecipeListRef


class RecipeUnlockedTriggerTypeArg(PlayerConditions):
    recipes: RecipeListRef


RecipeUnlockedTrigger = ParitalRequired[RecipeUnlockedTriggerTypeArg]
