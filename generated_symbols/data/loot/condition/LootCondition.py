"""
Generated from symbols.json for ::java::data::loot::condition::LootCondition
Local link to file: generated_symbols/data/loot/condition/LootCondition.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.advancement.predicate.BlockPredicate import BlockPredicate
from generated_symbols.data.loot.condition.AllOf import AllOf
from generated_symbols.data.loot.condition.AnyOf import AnyOf
from generated_symbols.data.loot.condition.DamageSourceProperties import DamageSourceProperties
from generated_symbols.data.loot.condition.EnchantmentActiveCheck import EnchantmentActiveCheck
from generated_symbols.data.loot.condition.EntityProperties import EntityProperties
from generated_symbols.data.loot.condition.EntityScores import EntityScores
from generated_symbols.data.loot.condition.EnvironmentAttributeCheck import EnvironmentAttributeCheck
from generated_symbols.data.loot.condition.Inverted import Inverted
from generated_symbols.data.loot.condition.KilledByPlayer import KilledByPlayer
from generated_symbols.data.loot.condition.LocationCheck import LocationCheck
from generated_symbols.data.loot.condition.MatchTool import MatchTool
from generated_symbols.data.loot.condition.RandomChance import RandomChance
from generated_symbols.data.loot.condition.RandomChanceWithEnchantedBonus import RandomChanceWithEnchantedBonus
from generated_symbols.data.loot.condition.TableBonus import TableBonus
from generated_symbols.data.loot.condition.TimeCheck import TimeCheck
from generated_symbols.data.loot.condition.ValueCheck import ValueCheck
from generated_symbols.data.loot.condition.WeatherCheck import WeatherCheck


@dataclass(kw_only=True)
class LootConditionAllOf(AllOf):
    type: Literal['minecraft:all_of']


@dataclass(kw_only=True)
class LootConditionAnyOf(AnyOf):
    type: Literal['minecraft:any_of']


@dataclass(kw_only=True)
class LootConditionDamageSourceProperties(DamageSourceProperties):
    type: Literal['minecraft:damage_source_properties']


@dataclass(kw_only=True)
class LootConditionEnchantmentActiveCheck(EnchantmentActiveCheck):
    type: Literal['minecraft:enchantment_active_check']


@dataclass(kw_only=True)
class LootConditionEntityProperties(EntityProperties):
    type: Literal['minecraft:entity_properties']


@dataclass(kw_only=True)
class LootConditionEntityScores(EntityScores):
    type: Literal['minecraft:entity_scores']


@dataclass(kw_only=True)
class LootConditionEnvironmentAttributeCheck(EnvironmentAttributeCheck):
    type: Literal['minecraft:environment_attribute_check']


@dataclass(kw_only=True)
class LootConditionInverted(Inverted):
    type: Literal['minecraft:inverted']


@dataclass(kw_only=True)
class LootConditionKilledByPlayer(KilledByPlayer):
    type: Literal['minecraft:killed_by_player']


@dataclass(kw_only=True)
class LootConditionLocationCheck(LocationCheck):
    type: Literal['minecraft:location_check']


@dataclass(kw_only=True)
class LootConditionMatchBlock(BlockPredicate):
    type: Literal['minecraft:match_block']


@dataclass(kw_only=True)
class LootConditionMatchTool(MatchTool):
    type: Literal['minecraft:match_tool']


@dataclass(kw_only=True)
class LootConditionRandomChance(RandomChance):
    type: Literal['minecraft:random_chance']


@dataclass(kw_only=True)
class LootConditionRandomChanceWithEnchantedBonus(RandomChanceWithEnchantedBonus):
    type: Literal['minecraft:random_chance_with_enchanted_bonus']


@dataclass(kw_only=True)
class LootConditionTableBonus(TableBonus):
    type: Literal['minecraft:table_bonus']


@dataclass(kw_only=True)
class LootConditionTimeCheck(TimeCheck):
    type: Literal['minecraft:time_check']


@dataclass(kw_only=True)
class LootConditionValueCheck(ValueCheck):
    type: Literal['minecraft:value_check']


@dataclass(kw_only=True)
class LootConditionWeatherCheck(WeatherCheck):
    type: Literal['minecraft:weather_check']


type LootCondition = LootConditionAllOf | LootConditionAnyOf | LootConditionDamageSourceProperties | LootConditionEnchantmentActiveCheck | LootConditionEntityProperties | LootConditionEntityScores | LootConditionEnvironmentAttributeCheck | LootConditionInverted | LootConditionKilledByPlayer | LootConditionLocationCheck | LootConditionMatchBlock | LootConditionMatchTool | LootConditionRandomChance | LootConditionRandomChanceWithEnchantedBonus | LootConditionTableBonus | LootConditionTimeCheck | LootConditionValueCheck | LootConditionWeatherCheck


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::LootCondition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "condition",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::loot::LootConditionType",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "id"
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "loot_condition_type"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "condition"
                            ]
                        }
                    ],
                    "registry": "minecraft:loot_condition"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "loot_condition_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:loot_condition"
                }
            }
        ]
    }
}

