"""
Generated from symbols.json for ::java::data::advancement::trigger::PlayerInteractTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/PlayerInteractTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class PlayerInteractTriggerTypeArg(PlayerConditions):
    item: ItemPredicate | None = None
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.


PlayerInteractTrigger = AllOptional[PlayerInteractTriggerTypeArg]
