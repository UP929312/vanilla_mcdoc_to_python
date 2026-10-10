"""
Generated from symbols.json for ::java::data::advancement::trigger::ShotCrossbowTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/ShotCrossbowTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class ShotCrossbowTriggerTypeArg(PlayerConditions):
    item: ItemPredicate | None = None  # Crossbow that was used.


ShotCrossbowTrigger = AllOptional[ShotCrossbowTriggerTypeArg]
