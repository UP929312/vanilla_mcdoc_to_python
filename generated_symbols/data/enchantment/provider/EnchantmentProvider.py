"""
Generated from symbols.json for ::java::data::enchantment::provider::EnchantmentProvider
Local link to file: generated_symbols/data/enchantment/provider/EnchantmentProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import ClassVar, Literal

from generated_symbols.data.enchantment.provider.ByCostEnchantmentProvider import ByCostEnchantmentProvider
from generated_symbols.data.enchantment.provider.ByCostWithDifficultyEnchantmentProvider import ByCostWithDifficultyEnchantmentProvider
from generated_symbols.data.enchantment.provider.SingleProvider import SingleProvider


@dataclass(kw_only=True)
class EnchantmentProviderByCost(ByCostEnchantmentProvider):
    __resource_dir__: ClassVar[str] = 'enchantment_provider'

    type: Literal['minecraft:by_cost']


@dataclass(kw_only=True)
class EnchantmentProviderByCostWithDifficulty(ByCostWithDifficultyEnchantmentProvider):
    type: Literal['minecraft:by_cost_with_difficulty']


@dataclass(kw_only=True)
class EnchantmentProviderSingle(SingleProvider):
    type: Literal['minecraft:single']


type EnchantmentProvider = EnchantmentProviderByCost | EnchantmentProviderByCostWithDifficulty | EnchantmentProviderSingle


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::provider::EnchantmentProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
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
                                    "value": "enchantment_provider_type"
                                }
                            }
                        }
                    ]
                }
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
                    "registry": "minecraft:enchantment_provider"
                }
            }
        ]
    }
}

