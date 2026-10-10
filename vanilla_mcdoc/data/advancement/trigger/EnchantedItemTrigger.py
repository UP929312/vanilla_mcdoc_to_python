"""
Generated from symbols.json for ::java::data::advancement::trigger::EnchantedItemTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/EnchantedItemTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class EnchantedItemTriggerTypeArg(PlayerConditions):
    item: ItemPredicate | None = None
    levels: MinMaxBounds[int] | int | None = None


EnchantedItemTrigger = AllOptional[EnchantedItemTriggerTypeArg]
