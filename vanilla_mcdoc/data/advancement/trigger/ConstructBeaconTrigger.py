"""
Generated from symbols.json for ::java::data::advancement::trigger::ConstructBeaconTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/ConstructBeaconTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class ConstructBeaconTriggerTypeArg(PlayerConditions):
    level: MinMaxBounds[int] | int | None = None  # Tier of the updated beacon base.


ConstructBeaconTrigger = AllOptional[ConstructBeaconTriggerTypeArg]
