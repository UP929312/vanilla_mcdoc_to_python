"""
Generated from symbols.json for ::java::data::loot::condition::TableBonus
Local link to file: generated_symbols/data/loot/condition/TableBonus.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec
from pydantic import Field


class TableBonus(GeneratedModel):
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    chances: list[Annotated[float, Field(ge=0, le=1)]]  # Probabilities for each enchantment level


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

