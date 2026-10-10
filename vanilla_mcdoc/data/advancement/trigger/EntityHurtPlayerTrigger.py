"""
Generated from symbols.json for ::java::data::advancement::trigger::EntityHurtPlayerTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/EntityHurtPlayerTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.DamagePredicate import DamagePredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class EntityHurtPlayerTriggerTypeArg(PlayerConditions):
    damage: DamagePredicate | None = None


EntityHurtPlayerTrigger = AllOptional[EntityHurtPlayerTriggerTypeArg]
