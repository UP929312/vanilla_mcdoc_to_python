"""
Generated from symbols.json for ::java::data::advancement::trigger::ConsumeItemTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/ConsumeItemTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class ConsumeItemTriggerTypeArg(PlayerConditions):
    item: ItemPredicate | None = None


ConsumeItemTrigger = AllOptional[ConsumeItemTriggerTypeArg]
