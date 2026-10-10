"""
Generated from symbols.json for ::java::data::advancement::trigger::FishingRodHookedTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/FishingRodHookedTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class FishingRodHookedTriggerTypeArg(PlayerConditions):
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.  Entity that was pulled. Or the hook itself if no entity was hooked.
    item: ItemPredicate | None = None  # Item that was caught.
    rod: ItemPredicate | None = None  # Fishing rod used.


FishingRodHookedTrigger = AllOptional[FishingRodHookedTriggerTypeArg]
