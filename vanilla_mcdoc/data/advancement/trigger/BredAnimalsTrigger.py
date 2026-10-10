"""
Generated from symbols.json for ::java::data::advancement::trigger::BredAnimalsTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/BredAnimalsTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class BredAnimalsTriggerTypeArg(PlayerConditions):
    parent: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    partner: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    child: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.  Entity may not exist.


BredAnimalsTrigger = AllOptional[BredAnimalsTriggerTypeArg]
