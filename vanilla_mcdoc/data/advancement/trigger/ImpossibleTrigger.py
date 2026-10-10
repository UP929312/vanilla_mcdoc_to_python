"""
Generated from symbols.json for ::java::data::advancement::trigger::ImpossibleTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/ImpossibleTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional


class ImpossibleTriggerTypeArg(GeneratedModel):
    pass


ImpossibleTrigger = AllOptional[ImpossibleTriggerTypeArg]
