"""
Generated from symbols.json for ::java::data::loot::condition::LootCondition
Local link to file: vanilla_mcdoc/data/loot/condition/LootCondition.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.data.advancement.predicate.BlockPredicate import BlockPredicate
from vanilla_mcdoc.data.loot.condition.AllOf import AllOf
from vanilla_mcdoc.data.loot.condition.AnyOf import AnyOf
from vanilla_mcdoc.data.loot.condition.DamageSourceProperties import DamageSourceProperties
from vanilla_mcdoc.data.loot.condition.EnchantmentActiveCheck import EnchantmentActiveCheck
from vanilla_mcdoc.data.loot.condition.EntityProperties import EntityProperties
from vanilla_mcdoc.data.loot.condition.EntityScores import EntityScores
from vanilla_mcdoc.data.loot.condition.EnvironmentAttributeCheck import EnvironmentAttributeCheck
from vanilla_mcdoc.data.loot.condition.FloatValueCheck import FloatValueCheck
from vanilla_mcdoc.data.loot.condition.IntegerValueCheck import IntegerValueCheck
from vanilla_mcdoc.data.loot.condition.Inverted import Inverted
from vanilla_mcdoc.data.loot.condition.KilledByPlayer import KilledByPlayer
from vanilla_mcdoc.data.loot.condition.LocationCheck import LocationCheck
from vanilla_mcdoc.data.loot.condition.MatchTool import MatchTool
from vanilla_mcdoc.data.loot.condition.RandomChance import RandomChance
from vanilla_mcdoc.data.loot.condition.RandomChanceWithEnchantedBonus import RandomChanceWithEnchantedBonus
from vanilla_mcdoc.data.loot.condition.TableBonus import TableBonus
from vanilla_mcdoc.data.loot.condition.TimeCheck import TimeCheck
from vanilla_mcdoc.data.loot.condition.WeatherCheck import WeatherCheck


class LootConditionAllOf(AllOf):
    type: Literal['minecraft:all_of', 'all_of'] = 'minecraft:all_of'


class LootConditionAnyOf(AnyOf):
    type: Literal['minecraft:any_of', 'any_of'] = 'minecraft:any_of'


class LootConditionDamageSourceProperties(DamageSourceProperties):
    type: Literal['minecraft:damage_source_properties', 'damage_source_properties'] = 'minecraft:damage_source_properties'


class LootConditionEnchantmentActiveCheck(EnchantmentActiveCheck):
    type: Literal['minecraft:enchantment_active_check', 'enchantment_active_check'] = 'minecraft:enchantment_active_check'


class LootConditionEntityProperties(EntityProperties):
    type: Literal['minecraft:entity_properties', 'entity_properties'] = 'minecraft:entity_properties'


class LootConditionEntityScores(EntityScores):
    type: Literal['minecraft:entity_scores', 'entity_scores'] = 'minecraft:entity_scores'


class LootConditionEnvironmentAttributeCheck(EnvironmentAttributeCheck):
    type: Literal['minecraft:environment_attribute_check', 'environment_attribute_check'] = 'minecraft:environment_attribute_check'


class LootConditionFloatValueCheck(FloatValueCheck):
    type: Literal['minecraft:float_value_check', 'float_value_check'] = 'minecraft:float_value_check'


class LootConditionIntValueCheck(IntegerValueCheck):
    type: Literal['minecraft:int_value_check', 'int_value_check'] = 'minecraft:int_value_check'


class LootConditionInverted(Inverted):
    type: Literal['minecraft:inverted', 'inverted'] = 'minecraft:inverted'


class LootConditionKilledByPlayer(KilledByPlayer):
    type: Literal['minecraft:killed_by_player', 'killed_by_player'] = 'minecraft:killed_by_player'


class LootConditionLocationCheck(LocationCheck):
    type: Literal['minecraft:location_check', 'location_check'] = 'minecraft:location_check'


class LootConditionMatchBlock(BlockPredicate):
    type: Literal['minecraft:match_block', 'match_block'] = 'minecraft:match_block'


class LootConditionMatchTool(MatchTool):
    type: Literal['minecraft:match_tool', 'match_tool'] = 'minecraft:match_tool'


class LootConditionRandomChance(RandomChance):
    type: Literal['minecraft:random_chance', 'random_chance'] = 'minecraft:random_chance'


class LootConditionRandomChanceWithEnchantedBonus(RandomChanceWithEnchantedBonus):
    type: Literal['minecraft:random_chance_with_enchanted_bonus', 'random_chance_with_enchanted_bonus'] = 'minecraft:random_chance_with_enchanted_bonus'


class LootConditionTableBonus(TableBonus):
    type: Literal['minecraft:table_bonus', 'table_bonus'] = 'minecraft:table_bonus'


class LootConditionTimeCheck(TimeCheck):
    type: Literal['minecraft:time_check', 'time_check'] = 'minecraft:time_check'


class LootConditionWeatherCheck(WeatherCheck):
    type: Literal['minecraft:weather_check', 'weather_check'] = 'minecraft:weather_check'


type LootCondition = Annotated[
    LootConditionAllOf | LootConditionAnyOf | LootConditionDamageSourceProperties | LootConditionEnchantmentActiveCheck | LootConditionEntityProperties | LootConditionEntityScores | LootConditionEnvironmentAttributeCheck | LootConditionFloatValueCheck | LootConditionIntValueCheck | LootConditionInverted | LootConditionKilledByPlayer | LootConditionLocationCheck | LootConditionMatchBlock | LootConditionMatchTool | LootConditionRandomChance | LootConditionRandomChanceWithEnchantedBonus | LootConditionTableBonus | LootConditionTimeCheck | LootConditionWeatherCheck,
    Field(discriminator='type'),
]
