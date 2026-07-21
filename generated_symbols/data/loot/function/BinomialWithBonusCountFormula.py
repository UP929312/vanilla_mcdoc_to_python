# Generated from symbols.json for ::java::data::loot::function::BinomialWithBonusCountFormula
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class BinomialWithBonusCountFormula:
    parameters: Any


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::BinomialWithBonusCountFormula": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "parameters",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "extra",
                            "type": {
                                "kind": "int"
                            }
                        },
                        {
                            "kind": "pair",
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
        ]
    }
}

