"""
Generated from symbols.json for ::java::data::number_provider::EnchantmentLevelProvider
Local link to file: generated_symbols/data/number_provider/EnchantmentLevelProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


class EnchantmentLevelProvider(GeneratedModel):
    amount: LevelBasedValue


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::EnchantmentLevelProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "amount",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            }
        ]
    }
}

