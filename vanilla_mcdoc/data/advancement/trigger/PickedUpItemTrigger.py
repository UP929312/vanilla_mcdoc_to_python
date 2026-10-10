"""
Generated from symbols.json for ::java::data::advancement::trigger::PickedUpItemTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/PickedUpItemTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class PickedUpItemTriggerTypeArg(PlayerConditions):
    item: ItemPredicate | None = None
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.  Entity may not exist.


PickedUpItemTrigger = AllOptional[PickedUpItemTriggerTypeArg]
