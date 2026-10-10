"""
Generated from symbols.json for ::java::data::advancement::trigger::ItemDurabilityTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/ItemDurabilityTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class ItemDurabilityTriggerTypeArg(PlayerConditions):
    delta: MinMaxBounds[int] | int | None = None  # Change in durability (negative numbers are used to indicate a decrease in durability).
    durability: MinMaxBounds[int] | int | None = None  # The resulting durability.
    item: ItemPredicate | None = None  # The item before its durability changed.


ItemDurabilityTrigger = AllOptional[ItemDurabilityTriggerTypeArg]
