"""
Generated from symbols.json for ::java::data::advancement::trigger::UsedEnderEyeTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/UsedEnderEyeTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class UsedEnderEyeTriggerTypeArg(PlayerConditions):
    distance: MinMaxBounds[float] | float | None = None  # Horizontal distance between the player and the stronghold.


UsedEnderEyeTrigger = AllOptional[UsedEnderEyeTriggerTypeArg]
