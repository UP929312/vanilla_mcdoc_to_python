"""
Generated from symbols.json for ::java::data::loot::function::EnchantedCountIncrease
Local link to file: vanilla_mcdoc/data/loot/function/EnchantedCountIncrease.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.data.loot.function.EnchantedCountBase import EnchantedCountBase
from vanilla_mcdoc.minecraft_types import IdSpec


class EnchantedCountIncrease(Conditions, EnchantedCountBase):
    enchantment: Annotated[str, IdSpec(registry='enchantment')]  # Enchantment that increases yields.


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
