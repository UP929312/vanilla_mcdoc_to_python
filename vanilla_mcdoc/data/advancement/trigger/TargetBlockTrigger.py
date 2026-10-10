"""
Generated from symbols.json for ::java::data::advancement::trigger::TargetBlockTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/TargetBlockTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class TargetBlockTriggerTypeArg(PlayerConditions):
    projectile: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    signal_strength: MinMaxBounds[int] | int | None = None


TargetBlockTrigger = AllOptional[TargetBlockTriggerTypeArg]
