"""
Generated from symbols.json for ::java::data::advancement::trigger::DefaultBlockInteractionTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/DefaultBlockInteractionTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AdvancementLocationPredicate import AdvancementLocationPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class DefaultBlockInteractionTriggerTypeArg(PlayerConditions):
    location: AdvancementLocationPredicate | None = None  # Predicate context: Block Use.


DefaultBlockInteractionTrigger = AllOptional[DefaultBlockInteractionTriggerTypeArg]
