"""
Generated from symbols.json for ::java::data::enchantment::provider::EnchantmentProvider
Local link to file: generated_symbols/data/enchantment/provider/EnchantmentProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.provider.EnchantmentsType import EnchantmentsType
    from generated_symbols.data.worldgen.IntProvider import IntProvider


@dataclass(kw_only=True)
class EnchantmentProviderByCost:
    type: Literal['minecraft:by_cost']
    enchantments: EnchantmentsType
    cost: IntProvider[int] | int  # Cost to use for the Enchanting process.


@dataclass(kw_only=True)
class EnchantmentProviderByCostWithDifficulty:
    type: Literal['minecraft:by_cost_with_difficulty']
    enchantments: EnchantmentsType
    min_cost: Annotated[int, 'Range | Min `0` and above | inclusive']  # Positive integer representing the minimum possible cost
    max_cost_span: Annotated[int, 'Range | Min `0` and above | inclusive']  # Span of the cost randomization when the special factor is at its maximum.


@dataclass(kw_only=True)
class EnchantmentProviderSingle:
    type: Literal['minecraft:single']
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    level: IntProvider[int] | int


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

