# Generated from symbols.json for ::java::world::component::item::BrewingFuel
from dataclasses import dataclass


@dataclass(kw_only=True)
class BrewingFuel:
    uses: str
    speed_multiplier: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::BrewingFuel": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "uses",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "number_provider"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "speed_multiplier",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "number_provider"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

