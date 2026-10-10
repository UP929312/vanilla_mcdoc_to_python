"""
Generated from symbols.json for ::java::data::advancement::trigger::SummonedEntityTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/SummonedEntityTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class SummonedEntityTriggerTypeArg(PlayerConditions):
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.


SummonedEntityTrigger = AllOptional[SummonedEntityTriggerTypeArg]
