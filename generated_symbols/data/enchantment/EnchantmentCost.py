# Generated from symbols.json for ::java::data::enchantment::EnchantmentCost
from dataclasses import dataclass


@dataclass(kw_only=True)
class EnchantmentCost:
    base: int  # Base cost at level 1.
    per_level_above_first: int  # Cost increase per level above 1.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::EnchantmentCost": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Base cost at level 1.",
                "key": "base",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "desc": "Cost increase per level above 1.",
                "key": "per_level_above_first",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}

