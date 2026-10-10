"""
Generated from symbols.json for ::java::data::number_provider::legacy::LegacyNumberProvider
Local link to file: generated_symbols/data/number_provider/legacy/LegacyNumberProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from generated_symbols.data.number_provider.legacy.BinomialNumberProvider import BinomialNumberProvider
from generated_symbols.data.number_provider.legacy.ConstantNumberProvider import ConstantNumberProvider
from generated_symbols.data.number_provider.legacy.EnchantmentLevelProvider import EnchantmentLevelProvider
from generated_symbols.data.number_provider.legacy.EnvironmentAttributeNumberProvider import EnvironmentAttributeNumberProvider
from generated_symbols.data.number_provider.legacy.ScoreNumberProvider import ScoreNumberProvider
from generated_symbols.data.number_provider.legacy.StorageNumberProvider import StorageNumberProvider
from generated_symbols.data.number_provider.legacy.SumNumberProvider import SumNumberProvider
from generated_symbols.data.number_provider.legacy.UniformNumberProvider import UniformNumberProvider
from minecraft_registry import IdSpec


class LegacyNumberProviderStructNone(UniformNumberProvider):
    type: Annotated[str, IdSpec(registry='loot_number_provider_type')] | None = None  # Defaults to `minecraft:uniform`.


class LegacyNumberProviderStructBinomial(BinomialNumberProvider):
    type: Literal['minecraft:binomial', 'binomial'] | None = 'minecraft:binomial'  # Defaults to `minecraft:uniform`.


class LegacyNumberProviderStructConstant(ConstantNumberProvider):
    type: Literal['minecraft:constant', 'constant'] | None = 'minecraft:constant'  # Defaults to `minecraft:uniform`.


class LegacyNumberProviderStructEnchantmentLevel(EnchantmentLevelProvider):
    type: Literal['minecraft:enchantment_level', 'enchantment_level'] | None = 'minecraft:enchantment_level'  # Defaults to `minecraft:uniform`.


class LegacyNumberProviderStructEnvironmentAttribute(EnvironmentAttributeNumberProvider):
    type: Literal['minecraft:environment_attribute', 'environment_attribute'] | None = 'minecraft:environment_attribute'  # Defaults to `minecraft:uniform`.


class LegacyNumberProviderStructScore(ScoreNumberProvider):
    type: Literal['minecraft:score', 'score'] | None = 'minecraft:score'  # Defaults to `minecraft:uniform`.


class LegacyNumberProviderStructStorage(StorageNumberProvider):
    type: Literal['minecraft:storage', 'storage'] | None = 'minecraft:storage'  # Defaults to `minecraft:uniform`.


class LegacyNumberProviderStructSum(SumNumberProvider):
    type: Literal['minecraft:sum', 'sum'] | None = 'minecraft:sum'  # Defaults to `minecraft:uniform`.


class LegacyNumberProviderStructUniform(UniformNumberProvider):
    type: Literal['minecraft:uniform', 'uniform'] | None = 'minecraft:uniform'  # Defaults to `minecraft:uniform`.


type LegacyNumberProviderStruct = LegacyNumberProviderStructNone | LegacyNumberProviderStructBinomial | LegacyNumberProviderStructConstant | LegacyNumberProviderStructEnchantmentLevel | LegacyNumberProviderStructEnvironmentAttribute | LegacyNumberProviderStructScore | LegacyNumberProviderStructStorage | LegacyNumberProviderStructSum | LegacyNumberProviderStructUniform


type LegacyNumberProvider = float | LegacyNumberProviderStruct


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::legacy::LegacyNumberProvider": {
        "kind": "union",
        "members": [
            {
                "kind": "float"
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "desc": "Defaults to `minecraft:uniform`.",
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
                                            "value": "loot_number_provider_type"
                                        }
                                    }
                                }
                            ]
                        },
                        "optional": True
                    },
                    {
                        "kind": "spread",
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
                            "registry": "minecraft:number_provider"
                        }
                    }
                ]
            }
        ]
    }
}
