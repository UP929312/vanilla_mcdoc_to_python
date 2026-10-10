"""
Generated from symbols.json for ::java::data::advancement::trigger::LootTableTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/LootTableTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.ParitalRequired import ParitalRequired
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.loot.LootTableListRef import LootTableListRef


class LootTableTriggerTypeArg(PlayerConditions):
    loot_tables: LootTableListRef


LootTableTrigger = ParitalRequired[LootTableTriggerTypeArg]
