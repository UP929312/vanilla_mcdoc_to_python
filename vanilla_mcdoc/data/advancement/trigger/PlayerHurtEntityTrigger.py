"""
Generated from symbols.json for ::java::data::advancement::trigger::PlayerHurtEntityTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/PlayerHurtEntityTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.DamagePredicate import DamagePredicate
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class PlayerHurtEntityTriggerTypeArg(PlayerConditions):
    damage: DamagePredicate | None = None
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.


PlayerHurtEntityTrigger = AllOptional[PlayerHurtEntityTriggerTypeArg]
