"""
Generated from symbols.json for ::java::data::advancement::trigger::FilledBucketTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/FilledBucketTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class FilledBucketTriggerTypeArg(PlayerConditions):
    item: ItemPredicate | None = None


FilledBucketTrigger = AllOptional[FilledBucketTriggerTypeArg]
