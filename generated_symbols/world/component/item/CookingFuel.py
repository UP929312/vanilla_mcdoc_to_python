# Generated from symbols.json for ::java::world::component::item::CookingFuel
from dataclasses import dataclass


@dataclass(kw_only=True)
class CookingFuel:
    burn_time: str
    speed_multiplier: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::CookingFuel": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "burn_time",
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

