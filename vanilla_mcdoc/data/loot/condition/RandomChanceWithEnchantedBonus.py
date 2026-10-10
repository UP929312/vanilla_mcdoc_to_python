"""
Generated from symbols.json for ::java::data::loot::condition::RandomChanceWithEnchantedBonus
Local link to file: vanilla_mcdoc/data/loot/condition/RandomChanceWithEnchantedBonus.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.LevelBasedValue import LevelBasedValue


class RandomChanceWithEnchantedBonus(GeneratedModel):
    unenchanted_chance: Annotated[float, Field(ge=0, le=1)]
    enchanted_chance: LevelBasedValue
    enchantment: Annotated[str, IdSpec(registry='enchantment')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::RandomChanceWithEnchantedBonus": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "unenchanted_chance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "enchanted_chance",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            },
            {
                "kind": "pair",
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
            }
        ]
    }
}
