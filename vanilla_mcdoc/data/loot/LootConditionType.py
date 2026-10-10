"""
Generated from symbols.json for ::java::data::loot::LootConditionType
Local link to file: vanilla_mcdoc/data/loot/LootConditionType.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class LootConditionType(StrEnum):
    ALTERNATIVE = "alternative"
    BLOCKSTATEPROPERTY = "block_state_property"
    DAMAGESOURCEPROPERTIES = "damage_source_properties"
    ENTITYPROPERTIES = "entity_properties"
    ENTITYSCORES = "entity_scores"
    INVERTED = "inverted"
    KILLEDBYPLAYER = "killed_by_player"
    LOCATIONCHECK = "location_check"
    MATCHTOOL = "match_tool"
    RANDOMCHANCE = "random_chance"
    RANDOMCHANCEWITHLOOTING = "random_chance_with_looting"
    REFERENCE = "reference"
    SURVIVESEXPLOSION = "survives_explosion"
    TABLEBONUS = "table_bonus"
    TIMECHECK = "time_check"
    WEATHERCHECK = "weather_check"
