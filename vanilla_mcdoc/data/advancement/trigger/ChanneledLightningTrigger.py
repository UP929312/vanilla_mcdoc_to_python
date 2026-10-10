"""
Generated from symbols.json for ::java::data::advancement::trigger::ChanneledLightningTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/ChanneledLightningTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class ChanneledLightningTriggerTypeArg(PlayerConditions):
    victims: list[AdvancementEntityPredicate] | None = None  # Predicate context: Advancement Entity.  Evaluates to true if every predicate in the list matches some victims.


ChanneledLightningTrigger = AllOptional[ChanneledLightningTriggerTypeArg]
