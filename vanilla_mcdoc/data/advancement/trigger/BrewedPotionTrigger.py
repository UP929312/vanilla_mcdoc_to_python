"""
Generated from symbols.json for ::java::data::advancement::trigger::BrewedPotionTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/BrewedPotionTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.world.component.predicate.PotionsPredicate import PotionsPredicate


class BrewedPotionTriggerTypeArg(PlayerConditions):
    potion: PotionsPredicate | None = None


BrewedPotionTrigger = AllOptional[BrewedPotionTriggerTypeArg]
