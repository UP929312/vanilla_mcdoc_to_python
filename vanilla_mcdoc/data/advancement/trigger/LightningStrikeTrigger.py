"""
Generated from symbols.json for ::java::data::advancement::trigger::LightningStrikeTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/LightningStrikeTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class LightningStrikeTriggerTypeArg(PlayerConditions):
    lightning: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    bystander: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.  Evaluates to false if no entities are nearby.


LightningStrikeTrigger = AllOptional[LightningStrikeTriggerTypeArg]
