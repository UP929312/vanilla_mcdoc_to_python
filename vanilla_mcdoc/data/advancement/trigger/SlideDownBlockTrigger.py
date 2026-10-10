"""
Generated from symbols.json for ::java::data::advancement::trigger::SlideDownBlockTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/SlideDownBlockTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.BlockStateConditions import BlockStateConditions
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class SlideDownBlockTriggerTypeArg(BlockStateConditions, PlayerConditions):
    pass


SlideDownBlockTrigger = AllOptional[SlideDownBlockTriggerTypeArg]
