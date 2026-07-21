# Generated from symbols.json for ::java::data::enchantment::provider::ByCostEnchantmentProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.provider.EnchantmentsType import EnchantmentsType
    from generated_symbols.data.worldgen.IntProvider import IntProvider


@dataclass(kw_only=True)
class ByCostEnchantmentProvider:
    enchantments: EnchantmentsType
    cost: IntProvider[int] | int  # Cost to use for the Enchanting process.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::provider::ByCostEnchantmentProvider": {
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
                "desc": "Cost to use for the Enchanting process.",
                "key": "cost",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int"
                        }
                    ]
                }
            }
        ]
    }
}

