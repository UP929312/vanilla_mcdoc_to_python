"""
Generated from symbols.json for ::java::data::loot::condition::TableBonus
Local link to file: generated_symbols/data/loot/condition/TableBonus.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class TableBonus:
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    chances: list[Annotated[float, 'Range | `0`-`1` | both inclusive']]  # Probabilities for each enchantment level


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::TableBonus": {
        "kind": "struct",
        "fields": [
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
            },
            {
                "kind": "pair",
                "desc": "Probabilities for each enchantment level",
                "key": "chances",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float",
                        "valueRange": {
                            "kind": 0,
                            "min": 0,
                            "max": 1
                        }
                    }
                }
            }
        ]
    }
}

