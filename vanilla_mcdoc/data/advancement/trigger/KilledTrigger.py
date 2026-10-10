"""
Generated from symbols.json for ::java::data::advancement::trigger::KilledTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/KilledTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.DamageSourcePredicate import DamageSourcePredicate
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class KilledTriggerTypeArg(PlayerConditions):
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    killing_blow: DamageSourcePredicate | None = None


KilledTrigger = AllOptional[KilledTriggerTypeArg]
