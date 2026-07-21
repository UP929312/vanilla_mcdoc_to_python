# Generated from symbols.json for ::java::data::loot::condition::RandomChanceWithEnchantedBonus
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class RandomChanceWithEnchantedBonus:
    unenchanted_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    enchanted_chance: LevelBasedValue
    enchantment: str


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

