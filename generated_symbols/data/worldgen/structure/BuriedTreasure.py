# Generated from symbols.json for ::java::data::worldgen::structure::BuriedTreasure
from dataclasses import dataclass


@dataclass(kw_only=True)
class BuriedTreasure:
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::BuriedTreasure": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}

