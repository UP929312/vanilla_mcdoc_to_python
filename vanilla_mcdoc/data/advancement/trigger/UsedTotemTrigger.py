"""
Generated from symbols.json for ::java::data::advancement::trigger::UsedTotemTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/UsedTotemTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class UsedTotemTriggerTypeArg(PlayerConditions):
    item: ItemPredicate | None = None


UsedTotemTrigger = AllOptional[UsedTotemTriggerTypeArg]
