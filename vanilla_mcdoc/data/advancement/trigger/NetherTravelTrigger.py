"""
Generated from symbols.json for ::java::data::advancement::trigger::NetherTravelTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/NetherTravelTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.DistancePredicate import DistancePredicate
from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class NetherTravelTriggerTypeArg(PlayerConditions):
    start_position: LocationPredicate | None = None  # Where in the Overworld the player was when they travelled to the Nether.
    distance: DistancePredicate | None = None  # How far the player now is from the coordinate they started at in the Overworld before travelling.


NetherTravelTrigger = AllOptional[NetherTravelTriggerTypeArg]
