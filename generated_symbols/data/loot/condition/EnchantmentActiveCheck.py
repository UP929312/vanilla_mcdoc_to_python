"""
Generated from symbols.json for ::java::data::loot::condition::EnchantmentActiveCheck
Local link to file: generated_symbols/data/loot/condition/EnchantmentActiveCheck.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass


@dataclass(kw_only=True)
class EnchantmentActiveCheck:
    active: bool


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::EnchantmentActiveCheck": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "active",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}

