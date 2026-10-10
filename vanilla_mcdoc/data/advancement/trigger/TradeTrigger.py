"""
Generated from symbols.json for ::java::data::advancement::trigger::TradeTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/TradeTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class TradeTriggerTypeArg(PlayerConditions):
    villager: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    item: ItemPredicate | None = None  # Item that was purchased.  `count` tag checks the item count from one trade, not the total amount traded for.


TradeTrigger = AllOptional[TradeTriggerTypeArg]
