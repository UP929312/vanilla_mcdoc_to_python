"""
Generated from symbols.json for ::java::data::advancement::trigger::TameAnimalTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/TameAnimalTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class TameAnimalTriggerTypeArg(PlayerConditions):
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.


TameAnimalTrigger = AllOptional[TameAnimalTriggerTypeArg]
