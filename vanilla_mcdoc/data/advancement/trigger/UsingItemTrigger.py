"""
Generated from symbols.json for ::java::data::advancement::trigger::UsingItemTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/UsingItemTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class UsingItemTriggerTypeArg(PlayerConditions):
    item: ItemPredicate | None = None


UsingItemTrigger = AllOptional[UsingItemTriggerTypeArg]
