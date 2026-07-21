# Generated from symbols.json for ::java::data::enchantment::provider::ByCostWithDifficultyEnchantmentProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.provider.EnchantmentsType import EnchantmentsType


@dataclass(kw_only=True)
class ByCostWithDifficultyEnchantmentProvider:
    enchantments: EnchantmentsType
    min_cost: Annotated[int, 'Range | Min `0` and above | inclusive']  # Positive integer representing the minimum possible cost
    max_cost_span: Annotated[int, 'Range | Min `0` and above | inclusive']  # Span of the cost randomization when the special factor is at its maximum.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::provider::ByCostWithDifficultyEnchantmentProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "enchantments",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::provider::EnchantmentsType"
                }
            },
            {
                "kind": "pair",
                "desc": "Positive integer representing the minimum possible cost",
                "key": "min_cost",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Span of the cost randomization when the special factor is at its maximum.",
                "key": "max_cost_span",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            }
        ]
    }
}

