"""
Generated from symbols.json for ::java::data::advancement::trigger::LevitationTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/LevitationTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.DistancePredicate import DistancePredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class LevitationTriggerTypeArg(PlayerConditions):
    distance: DistancePredicate | None = None
    duration: MinMaxBounds[int] | int | None = None


LevitationTrigger = AllOptional[LevitationTriggerTypeArg]
