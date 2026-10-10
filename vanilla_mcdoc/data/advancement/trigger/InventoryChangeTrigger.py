"""
Generated from symbols.json for ::java::data::advancement::trigger::InventoryChangeTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/InventoryChangeTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class SlotsStruct(GeneratedModel):
    empty: MinMaxBounds[int] | int | None = None  # Amount of empty slots.
    occupied: MinMaxBounds[int] | int | None = None  # Amount of occupied slots.
    full: MinMaxBounds[int] | int | None = None  # Amount of slots that are a full stack.


class InventoryChangeTriggerTypeArg(PlayerConditions):
    slots: SlotsStruct | None = None
    items: list[ItemPredicate] | None = None


InventoryChangeTrigger = AllOptional[InventoryChangeTriggerTypeArg]
