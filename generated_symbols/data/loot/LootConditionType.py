# Generated from symbols.json for ::java::data::loot::LootConditionType
from enum import Enum


class LootConditionType(Enum):
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


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::LootConditionType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Alternative",
                "value": "alternative"
            },
            {
                "identifier": "BlockStateProperty",
                "value": "block_state_property"
            },
            {
                "identifier": "DamageSourceProperties",
                "value": "damage_source_properties"
            },
            {
                "identifier": "EntityProperties",
                "value": "entity_properties"
            },
            {
                "identifier": "EntityScores",
                "value": "entity_scores"
            },
            {
                "identifier": "Inverted",
                "value": "inverted"
            },
            {
                "identifier": "KilledByPlayer",
                "value": "killed_by_player"
            },
            {
                "identifier": "LocationCheck",
                "value": "location_check"
            },
            {
                "identifier": "MatchTool",
                "value": "match_tool"
            },
            {
                "identifier": "RandomChance",
                "value": "random_chance"
            },
            {
                "identifier": "RandomChanceWithLooting",
                "value": "random_chance_with_looting"
            },
            {
                "identifier": "Reference",
                "value": "reference"
            },
            {
                "identifier": "SurvivesExplosion",
                "value": "survives_explosion"
            },
            {
                "identifier": "TableBonus",
                "value": "table_bonus"
            },
            {
                "identifier": "TimeCheck",
                "value": "time_check"
            },
            {
                "identifier": "WeatherCheck",
                "value": "weather_check"
            }
        ]
    }
}

