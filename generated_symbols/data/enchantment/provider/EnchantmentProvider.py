"""
Generated from symbols.json for ::java::data::enchantment::provider::EnchantmentProvider
Local link to file: generated_symbols/data/enchantment/provider/EnchantmentProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar, Literal

from generated_symbols.data.enchantment.provider.ByCostEnchantmentProvider import ByCostEnchantmentProvider
from generated_symbols.data.enchantment.provider.ByCostWithDifficultyEnchantmentProvider import ByCostWithDifficultyEnchantmentProvider
from generated_symbols.data.enchantment.provider.SingleProvider import SingleProvider
from pydantic import Field


class EnchantmentProviderByCost(ByCostEnchantmentProvider):
    __resource_dir__: ClassVar[str] = 'enchantment_provider'

    type: Literal['minecraft:by_cost', 'by_cost'] = 'minecraft:by_cost'


class EnchantmentProviderByCostWithDifficulty(ByCostWithDifficultyEnchantmentProvider):
    __resource_dir__: ClassVar[str] = 'enchantment_provider'

    type: Literal['minecraft:by_cost_with_difficulty', 'by_cost_with_difficulty'] = 'minecraft:by_cost_with_difficulty'


class EnchantmentProviderSingle(SingleProvider):
    __resource_dir__: ClassVar[str] = 'enchantment_provider'

    type: Literal['minecraft:single', 'single'] = 'minecraft:single'


type EnchantmentProvider = Annotated[
    EnchantmentProviderByCost | EnchantmentProviderByCostWithDifficulty | EnchantmentProviderSingle,
    Field(discriminator='type'),
]


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

