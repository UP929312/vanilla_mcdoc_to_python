"""
Generated from symbols.json for ::java::data::advancement::trigger::DistanceTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/DistanceTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.DistancePredicate import DistancePredicate
from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class DistanceTriggerTypeArg(PlayerConditions):
    start_position: LocationPredicate | None = None  # Where the player started to travel.
    distance: DistancePredicate | None = None  # How far the player travels.


DistanceTrigger = AllOptional[DistanceTriggerTypeArg]
