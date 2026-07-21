# Generated from symbols.json for ::java::data::loot::condition::RandomChance
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef


@dataclass(kw_only=True)
class RandomChance:
    chance: NumberProviderRef  # Clamps to a float between `0` & `1` (inclusive).


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::RandomChance": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Clamps to a float between `0` & `1` (inclusive).",
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
                            "path": "::java::data::number_provider::NumberProviderRef",
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

