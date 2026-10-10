"""
Generated from symbols.json for ::java::data::advancement::trigger::AnyBlockInteractionTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/AnyBlockInteractionTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AdvancementLocationPredicate import AdvancementLocationPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class AnyBlockInteractionTriggerTypeArg(PlayerConditions):
    location: AdvancementLocationPredicate | None = None  # Predicate context: Advancement Location.


AnyBlockInteractionTrigger = AllOptional[AnyBlockInteractionTriggerTypeArg]
