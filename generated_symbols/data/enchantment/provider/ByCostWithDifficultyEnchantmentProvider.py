"""
Generated from symbols.json for ::java::data::enchantment::provider::ByCostWithDifficultyEnchantmentProvider
Local link to file: generated_symbols/data/enchantment/provider/ByCostWithDifficultyEnchantmentProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.provider.EnchantmentsType import EnchantmentsType


class ByCostWithDifficultyEnchantmentProvider(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'enchantment_provider'

    enchantments: EnchantmentsType
    min_cost: Annotated[int, Field(ge=0)]  # Positive integer representing the minimum possible cost
    max_cost_span: Annotated[int, Field(ge=0)]  # Span of the cost randomization when the special factor is at its maximum.


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

