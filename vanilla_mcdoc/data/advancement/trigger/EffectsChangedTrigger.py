"""
Generated from symbols.json for ::java::data::advancement::trigger::EffectsChangedTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/EffectsChangedTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.EntityEffectsPredicate import EntityEffectsPredicate
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class EffectsChangedTriggerTypeArg(PlayerConditions):
    effects: EntityEffectsPredicate | None = None
    source: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.  Entity may not exist.


EffectsChangedTrigger = AllOptional[EffectsChangedTriggerTypeArg]
