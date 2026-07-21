# Generated from symbols.json for ::java::data::loot::function::EnchantedCountIncrease
from dataclasses import dataclass
from generated_symbols.data.loot.function.Conditions import Conditions
from generated_symbols.data.loot.function.EnchantedCountBase import EnchantedCountBase


@dataclass(kw_only=True)
class EnchantedCountIncrease(EnchantedCountBase, Conditions):
    enchantment: str  # Enchantment that increases yields.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::EnchantedCountIncrease": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::EnchantedCountBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Enchantment that increases yields.",
                "key": "enchantment",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "enchantment"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}

