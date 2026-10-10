"""
Generated from symbols.json for ::java::data::advancement::trigger::CuredZombieVillagerTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/CuredZombieVillagerTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class CuredZombieVillagerTriggerTypeArg(PlayerConditions):
    zombie: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    villager: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.


CuredZombieVillagerTrigger = AllOptional[CuredZombieVillagerTriggerTypeArg]
