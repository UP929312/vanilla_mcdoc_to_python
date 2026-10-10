"""
Generated from symbols.json for ::java::data::loot::condition::RandomChance
Local link to file: vanilla_mcdoc/data/loot/condition/RandomChance.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.FloatNumberProviderRef import FloatNumberProviderRef


class RandomChance(GeneratedModel):
    chance: FloatNumberProviderRef  # Accepts a value between `0` & `1` (inclusive).


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::RandomChance": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Accepts a value between `0` & `1` (inclusive).",
                "key": "chance",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "float",
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 1
                            },
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::number_provider::FloatNumberProviderRef",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}
