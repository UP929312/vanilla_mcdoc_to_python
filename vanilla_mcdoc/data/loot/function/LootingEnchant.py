"""
Generated from symbols.json for ::java::data::loot::function::LootingEnchant
Local link to file: generated_symbols/data/loot/function/LootingEnchant.py
"""
# ~~~ CODE ~~~
from generated_symbols.data.loot.function.Conditions import Conditions
from generated_symbols.data.loot.function.EnchantedCountBase import EnchantedCountBase


class LootingEnchant(Conditions, EnchantedCountBase):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::LootingEnchant": {
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
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}
