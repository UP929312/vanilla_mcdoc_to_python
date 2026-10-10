"""
Generated from symbols.json for ::java::data::advancement::trigger::EnterBlockTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/EnterBlockTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.BlockStateConditions import BlockStateConditions
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class EnterBlockTriggerTypeArg(BlockStateConditions, PlayerConditions):
    pass


EnterBlockTrigger = AllOptional[EnterBlockTriggerTypeArg]
