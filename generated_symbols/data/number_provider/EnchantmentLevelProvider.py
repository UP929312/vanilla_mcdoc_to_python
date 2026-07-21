# Generated from symbols.json for ::java::data::number_provider::EnchantmentLevelProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class EnchantmentLevelProvider:
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

